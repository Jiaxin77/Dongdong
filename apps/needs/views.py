from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse
import json

# Create your views here.
from needs.models import Needs
from needs.serializer import NeedsSerializer

from order.models import Order
from order.views import create_order_id, price_to_app, price_total

from user.models import Enterprise, Foreman, Farmers, FarmersMember
import time
from django.utils import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# 定时检测！
# 开启定时工作
from user.serializer import FarmersMemberSerializer

try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")


    # 设置定时任务，选择方式为interval，时间间隔为10s
    # 另一种方式为每天固定时间执行任务，对应代码为：
    @register_job(scheduler, 'cron', day_of_week='mon-sun', hour='8', minute='01', second='00', id='task_time')
    # @register_job(scheduler,"interval", seconds=10)
    def my_job():
        # 这里写你要执行的任务
        # 检测时间
        #print("定时器开始")
        auto_begin_needs()
        pass


    register_events(scheduler)
    scheduler.start()
except Exception as e:
    #print(e)
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
    #print(request.body)
    req = json.loads(request.body)
    #print(req)
    enterid = req['id']
    req_form = req['parameter']
    #needsDes = req_form['needsDes']
    needsFarmerType = req_form['needsFarmerType']
    needsNum = req_form['needsNum']
    price = req_form['price']
    needsBeginTime = req_form['buildTime'][0][0:10]

    needsLocation = req_form['province'] + req_form['centre'] + req_form['local']
    needsEndTime = req_form['buildTime'][1][0:10]

    remarks = req_form['description']
    enter = Enterprise.objects.get(id=enterid)

    data_dict = {"enterId": enter.id, "needsDes": enter.nowProject, "needsFarmerType": needsFarmerType,
                 'needsNum': needsNum, 'price': price, 'needsBeginTime': needsBeginTime, 'needsLocation': needsLocation,
                 'needsEndTime': needsEndTime, 'needsType': "匹配中"}  ###删掉了remarks，des
    #
    # serializer = NeedsSerializer(data=data_dict)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()  # 数据库新增信息

    Needs.objects.create(enterId=enter,needsDes=enter.nowProject,needsFarmerType=needsFarmerType,needsNum=needsNum,
                         price=price,needsBeginTime=needsBeginTime,needsLocation=needsLocation,needsEndTime=needsEndTime,needsType='匹配中',remarks=remarks)
    # 分配需求

    mydict = {'result': SUCCESS, 'msg': '需求发布成功！'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_needs(request):  # 企业查看需求列表
    """
    GET
    :param request: 企业id
    :return: 企业当前需求们（已发布、已取消等）
    """

    # 根据企业id获取

    # req = json.loads(request.body)
    # enterid = req['id']
    enterid = request.GET.get('id')
    enter = Enterprise.objects.get(id=enterid)
    allneeds = Needs.objects.all().order_by('-id')
    needList = []
    for need in allneeds:
        if need.enterId == enter:  # 获取属于该企业的
            serializer = NeedsSerializer(need)
            needList.append(serializer.data)

    mydict = {'result': SUCCESS, 'msg': '获取成功', 'data': {'enterid': enterid, 'needList': needList}}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_need_info(request):  # 企业查看具体某需求信息
    """
    GET
    :param request: 需求id
    :return: 需求信息们
    """

    needid = request.GET.get('id')  # 需求id
    # needid = req['id']
    need = Needs.objects.get(id=needid)
    serializer = NeedsSerializer(need)

    match = []

    # 匹配成员信息
    matchResult = need.matchResult.all()
    # matchResult = Needs.objects.filter(matc)
    #print(matchResult)
    foremans = Foreman.objects.all()
    for foreman in foremans:
        haveFlag = False
        matchGroups = []
        groups = Farmers.objects.filter(leader=foreman)
        for group in groups:
            if group in matchResult:
                member = FarmersMember.objects.filter(group_id=group)
                member_ser = FarmersMemberSerializer(member, many=True)
                thisgroup = {'id': group.id, 'name': str(group.type) + str(group.classNumber),
                             'memberNumber': group.memberNumber, 'authState': group.authState,
                             'members': member_ser.data}
                matchGroups.append(thisgroup)
                haveFlag = True
        foremanInfo = {'id': foreman.id, 'name': foreman.name, 'IDCard': foreman.IDCard,
                       'phonenumber': foreman.phonenumber, 'Bank': foreman.Bank, 'BankNumber': foreman.BankNumber,
                       'groups': matchGroups}
        if haveFlag == True:
            match.append(foremanInfo)

    # groupList=[]
    # for group in matchResult:
    #     member =  FarmersMember.objects.filter(group_id=group)
    #     member_ser = FarmersMemberSerializer(member,many=True)
    #     thisGroup ={'id':group.id,'name':str(group.type)+str(group.classNumber),'memberNumber':group.memberNumber,}
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'need': serializer.data, 'matchPeople': match}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_self_needs(request):  # 农民工获取待接受需求
    """
    GET
    :param request: 农民工id
    :return: 需求列表
    """

    farid = request.GET.get('id')
    foreman = Foreman.objects.get(id=farid)

    allfarmers = Farmers.objects.filter(leader=foreman)  # 属于此包工头的小组
    farmerTypeList = []
    for farmers in allfarmers:
        farmerTypeList.append(farmers.type)
    #print(farmerTypeList)
    allneeds = Needs.objects.all().order_by('-needsTime')
    needsList = []
    for need in allneeds:
        if need.needsType == '匹配中':
            if need.needsFarmerType in farmerTypeList:
                serializer = NeedsSerializer(need)
                needsList.append(serializer.data)

    mydict = {'result': SUCCESS, 'msg': '获取成功', 'needsList': needsList}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def foreman_get_need(request):  # 包工头获取单个需求，和人员列表
    """
    GET
    :param request: 需求id
    :return: 单个需求详情和人员列表
    """

    needId = request.GET.get('needid')
    foremanId = request.GET.get('foremanid')
    need = Needs.objects.get(id=needId)
    need_ser = NeedsSerializer(need)

    foreman = Foreman.objects.get(id=foremanId)
    myFarmers = []
    farmers_list = Farmers.objects.all()
    members = FarmersMember.objects.all()
    for group in farmers_list:
        # #print(group.id)
        # #print(group.ingNeed == None)
        # #print(group.leader_id)
        # #print(group.type == need.needsFarmerType)
        # #print(group.authState == "审核通过")
        if group.ingNeed == None and group.leader_id == foreman.id and group.type == need.needsFarmerType and group.authState == "审核通过":
            #print("有符合需求的")
            member_list = []
            for member in members:
                if member.group_id == group.id:
                    member_ser = FarmersMemberSerializer(member)
                    member_list.append(member_ser.data)
            group_dict = {'id': group.id, 'name': str(group.type) + str(group.classNumber), 'member': member_list}
            myFarmers.append(group_dict)

    mydict = {'result': SUCCESS, 'msg': '获取成功', 'need': need_ser.data, 'farmers': myFarmers}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def foreman_now_need(request):  # 农民工查看当前已经接受（正在进行）的需求
    """
    GET
    :param request:农民工id
    :return:
    """
    foremanid = request.GET.get('id')  # 农民工id
    foreman = Foreman.objects.get(id=foremanid)
    groups = Farmers.objects.filter(leader=foreman)
    needsList = []
    for group in groups:
        if group.ingNeed != None:
            needsList.append(group.ingNeed)
    need_ser = NeedsSerializer(needsList, many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'need': need_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def deal_needs(request):  # 包工头接受/拒绝需求
    """
    POST

    :param request:需求id，是每接受一个 传一下 、传过来哪个组接受需求
    :return:成功/失败
    """
    req = json.loads(request.body)
    needid = req['needid']
    need = Needs.objects.get(id=needid)
    groupid_list = req['groupList']
    totalnum = 0  # 计算这次提交的总人数
    for groupid in groupid_list:
        group = Farmers.objects.get(id=groupid)
        totalnum = totalnum + group.memberNumber
    if totalnum + need.nowNum > need.needsNum:
        mydict = {'result': ERROR, 'msg': '人数超过需求人数，请重新选择！'}
        return HttpResponse(json.dumps(mydict), content_type="application/json")
    else:
        need.nowNum = need.nowNum + totalnum  # 当前需求已匹配人数
        if need.nowNum == need.needsNum:
            need.needsType = "匹配完成待支付"
        for groupid in groupid_list:
            group = Farmers.objects.get(id=groupid)
            group.ingNeed = need
            group.save()
            need.matchResult.add(group)  # 多对多字段
        need.save()
        # 此时产生订单？
        # for group in need.matchResult.all():
        # for group in need.matchResult.all():
        #     orderid = create_order_id(need.id, group.id)
        #     money = need.price * (group.memberNumber / need.needsNum)
        #     ##print(money)
        #
        #     Order.objects.create(id=orderid, money=round(money,2),
        #                         moneyToFarmers=round(money * (1 - price_to_app),2), moneyToApp=round(money * price_to_app,2), needId=need,
        #                         status="交易中")
        #     order = Order.objects.get(id=orderid)
        #     order.farmers.add(group)
        #     order.save()
    mydict = {'result': SUCCESS, 'msg': '已成功接受需求'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

    # 记得将需求中 已匹配人数+1、这些组的ing需求置上需求号


def begin_needs(request):  # 企业开始需求（提前开工）

    """
    POST
    :param request: 需求id
    :return: 成功/失败
    """

    # 查找对应需求id
    # 置需求状态
    # 新增到此需求对应各个包工头的订单

    req = json.loads(request.body)
    id = req['id']  # 需求id
    need = Needs.objects.get(id=id)
    if need.needsType == "匹配完成待支付":
        need.needsType = "匹配完成待支付"
        need.save()
        # 创建订单
        ##print(need.matchResult.all())
        for group in need.matchResult.all():
            orderid = create_order_id(need.id, group.id)
            #money = need.price * (group.memberNumber / need.needsNum)
            money = need.price * (group.memberNumber / need.needsNum)
            Order.objects.create(id=orderid, money=round(money,2),
                                moneyToFarmers=round(money ,2), moneyToApp=0, needId=need,
                                status="交易中")
            order = Order.objects.get(id=orderid)
            order.farmers.add(group)
            order.save()
        mydict = {'result':SUCCESS,'msg': '成功开工！'}
        return HttpResponse(json.dumps(mydict), content_type="application/json")
    else:
        need.needsType = "匹配失败"
        need.save()
        for farmer in Farmers.objects.all():
            if farmer.ingNeed == need:
                farmer.ingNeed = None
                farmer.save()
        mydict = {'result': ERROR, 'msg': '匹配失败！'}
        return HttpResponse(json.dumps(mydict), content_type="application/json")



def auto_begin_needs():  # 自动开始需求（根据系统时间）
    """

    :return:
    """
    # 定期检测调用此函数
    # 置需求状态
    # 新增到此需求对应各个包工头的订单
    needs = Needs.objects.all().order_by('-needsTime')
    for need in needs:
        beginTime = need.needsBeginTime
        # today = datetime.date.today()
        # nowTime_str = datetime.
        nowTime_str = timezone.now().strftime('%Y-%m-%d')
        #print(nowTime_str)
        e_time = time.mktime(time.strptime(nowTime_str, "%Y-%m-%d"))
        #print(e_time)
        try:
            #print(beginTime)
            s_time = time.mktime(time.strptime(str(beginTime), '%Y-%m-%d'))
            #print(s_time)
            # 日期转化为int比较
            diff = int(s_time) - int(e_time)
            #print(diff)
            if diff <= 0:

                if need.needsNum <= need.nowNum and  need.needsType != "交易成功":  # 开工！
                    #print("到时间了！需求" + need.needsDes + "已经开始！")
                    need.needsType = "匹配完成待支付"
                    need.save()
                    order = Order.objects.filter(needId=need)

                    # 创建订单
                    #print(Needs.objects.get(id=need.id).matchResult.all())
                    #print(need.matchResult.all())
                    if (order == None): #不存在订单 -- 没执行过
                        for group in need.matchResult.all():
                            orderid = create_order_id(need.id, group.id)
                            money = need.price * (group.memberNumber / need.needsNum)
                            Order.objects.create(id=orderid, money=round(money, 2),
                                                 moneyToFarmers=round(money, 2), moneyToApp=0, needId=need,
                                                 status="交易中")
                            order = Order.objects.get(id=orderid)
                            order.farmers.add(group)
                            order.save()
                    else: #存在订单 已经执行过了
                        need.save()
                else:  # 未匹配成功
                    need.needsType = "匹配失败"
                    need.save()
                    for farmer in Farmers.objects.all():
                        if farmer.ingNeed == need:
                            farmer.ingNeed = None
                            farmer.save()
                    #print("到时间了！需求" + need.needsDes + "匹配失败！")


        except Exception as e:
            #print(e)
            return 0


# def cancel_needs(request):  # 企业取消需求
#     """
#
#     :param request: 需求id
#     :return: 成功/失败
#     """
#
#     # 查找对应需求，置需求状态
#     # ？？？存在已开工情况吗 若已开工需要取消订单
#     # 置农民工正在需求状态
#
#     mydict = {'msg': ''}
#     return HttpResponse(json.dumps(mydict), content_type="application/json")


# def auto_cancel_needs():  # 系统自动取消需求（到开工时间未招齐）
#     """
#
#     :return:
#     """
#     # 定期检测调用此函数
#     # 置需求状态
#     # 置农民工正在需求状态
#
# # def auto_time(): #  时间定期检测
# #     """
# #     时间检测，每过一天检测一次。需求开工or取消
# #     :return:
# #     """


def get_all_needs(requests):  # 获取所有需求列表——管理员用
    """
    GET
    :return: 需求列表序列化信息
    """
    needs = Needs.objects.all().order_by("-id")
    needs_ser = NeedsSerializer(needs, many=True)
    mydict = {'result': SUCCESS, 'msg': '成功获取！','data':needs_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

