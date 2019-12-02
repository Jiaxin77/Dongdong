from django.contrib.messages import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from needs.models import Needs, needType
from needs.serializer import NeedsSerializer
from user.models import Enterprise, farmerType, Foreman, Farmers
from datetime import datetime, date
import time
from django.utils import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
#定时检测！
#开启定时工作
try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # 设置定时任务，选择方式为interval，时间间隔为10s
    # 另一种方式为每天固定时间执行任务，对应代码为：
    @register_job(scheduler, 'cron', day_of_week='mon-sun', hour='8', minute='01', second='00',id='task_time')
    # @register_job(scheduler,"interval", seconds=10)
    def my_job():
        # 这里写你要执行的任务
        # 检测时间
        print("定时器开始")
        auto_begin_needs()
        pass
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()


def post_needs(request):  # 企业发布需求
    """
    POST
    :param request: 企业id、需求信息们
    :return: 成功/失败
    """
    
    # 需求序列化信息存储
    # （暂时不用的匹配）
    print(request.body)
    req = json.loads(request.body)
    print(req)
    enterid = req['id']
    req_form = req['parameter']
    needsDes = req_form['needsDes']
    needsFarmerType = req_form['needsFarmerType']
    needsNum = req_form['needsNum']
    price = req_form['price']
    needsBeginTime = req_form['buildTime'][0][0:10]

    needsLocation = req_form['province']+req_form['centre']+req_form['local']
    needsEndTime = req_form['buildTime'][1][0:10]

    #remarks = req_form['remarks']
    enter = Enterprise.objects.get(id = enterid)

    data_dict = {"enterId":enter.id,"needsDes":needsDes,"needsFarmerType":needsFarmerType,
                 'needsNum':needsNum, 'price': price,'needsBeginTime':needsBeginTime,'needsLocation':needsLocation,'needsEndTime':needsEndTime,'needsType':"匹配中" }###删掉了remarks，des

    serializer = NeedsSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    serializer.save()  # 数据库新增信息

    # 分配需求



    mydict = {'result':SUCCESS,'msg': '需求发布成功！'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")



def get_needs(request): #  企业查看需求列表
    """
    GET
    :param request: 企业id
    :return: 企业当前需求们（已发布、已取消等）
    """

    #根据企业id获取

    # req = json.loads(request.body)
    # enterid = req['id']
    enterid = request.GET.get('id')
    enter = Enterprise.objects.get(id=enterid)
    allneeds =  Needs.objects.all()
    needList = []
    for need in allneeds:
        if need.enterId == enter: #  获取属于该企业的
            serializer = NeedsSerializer(need)
            needList.append(serializer.data)

    mydict = {'result':SUCCESS,'msg': '获取成功','data':{'enterid':enterid,'needList':needList}}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def get_need_info(request): #  企业查看具体某需求信息
    """

    :param request: 需求id
    :return: 需求信息们
    """

    req = json.loads(request.body)
    needid = req['id']
    need = Needs.objects.get(id = needid)
    serializer = NeedsSerializer(need)
    mydict = {'result':SUCCESS,'msg': '获取成功', 'data': serializer.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_self_needs(request): # 农民工获取待接受需求
    """
    GET
    :param request: 农民工id
    :return: 需求列表
    """

    farid = request.GET.get('id')
    foreman = Foreman.objects.get(id = farid)

    allfarmers = Farmers.objects.filter(leader=foreman)#属于此包工头的小组
    farmerTypeList = []
    for farmers in allfarmers:
        farmerTypeList.append(farmers.type)
    print(farmerTypeList)
    allneeds = Needs.objects.all()
    needsList = []
    for need in allneeds:
        if need.needsType == '匹配中':
            if need.needsFarmerType in farmerTypeList:
                serializer = NeedsSerializer(need)
                needsList.append(serializer.data)

    mydict = {'result': SUCCESS, 'msg': '获取成功', 'needsList': needsList}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def deal_needs(request):#  包工头接受/拒绝需求
    """
    POST

    :param request:包工头id，是每接受一个 传一下 、传过来哪个组接受需求
    :return:成功/失败
    """
    #记得将需求中 已匹配人数+1、这些组的ing需求置上需求号
    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def begin_needs(request):#  企业开始需求（提前开工）

    """
    POST
    :param request: 需求id
    :return: 成功/失败
    """

    # 查找对应需求id
    # 置需求状态
    # 新增到此需求对应各个包工头的订单
    req = json.load(request.body)
    id = req['id'] #需求id



    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def auto_begin_needs():#  自动开始需求（根据系统时间）
    """

    :return:
    """
    # 定期检测调用此函数
    # 置需求状态
    # 新增到此需求对应各个包工头的订单
    needs = Needs.objects.all()
    for need in needs:
        beginTime = need.needsBeginTime
        #today = datetime.date.today()
        #nowTime_str = datetime.
        nowTime_str = timezone.now().strftime('%Y-%m-%d')
        print(nowTime_str)
        e_time = time.mktime(time.strptime(nowTime_str, "%Y-%m-%d"))
        print(e_time)
        try:
            print(beginTime)
            s_time = time.mktime(time.strptime(str(beginTime), '%Y-%m-%d'))
            print(s_time)
            # 日期转化为int比较
            diff = int(s_time) - int(e_time)
            print(diff)
            if diff <= 0:
                print("到时间了！需求"+need.needsDes+"已经开始！")
                if need.needsNum <= need.nowNum:
                    need.needsType ="匹配完成待支付"
                    need.save()
                else: #未匹配成功
                    need.needsType = "匹配失败"

                    need.save()

        except Exception as e:
            print(e)
            return 0







def cancel_needs(request):#  企业取消需求
    """

    :param request: 需求id
    :return: 成功/失败
    """

    # 查找对应需求，置需求状态
    # ？？？存在已开工情况吗 若已开工需要取消订单
    # 置农民工正在需求状态

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def auto_cancel_needs():# 系统自动取消需求（到开工时间未招齐）
    """

    :return:
    """
    # 定期检测调用此函数
    # 置需求状态
    # 置农民工正在需求状态


# def auto_time(): #  时间定期检测
#     """
#     时间检测，每过一天检测一次。需求开工or取消
#     :return:
#     """