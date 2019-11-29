from django.contrib.messages import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from needs.models import Needs, needType
from needs.serializer import NeedsSerializer
from user.models import Enterprise, farmerType, Foreman, Farmers


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
    needsDes = req['needsDes']
    needsFarmerType = req['needsFarmerType']
    needsNum = req['needsNum']
    price = req['price']
    needsBeginTime = req['needsBeginTime']
    needsLocation = req['needsLocation']
    needsEndTime = req['needsEndTime']
    remarks = req['remarks']
    enter = Enterprise.objects.get(id = enterid)

    data_dict = {"enterId":enter.id,"needsDes":needsDes,"needsFarmerType":needsFarmerType,
                 'needsNum':needsNum, 'price': price,'needsBeginTime':needsBeginTime,'needsLocation':needsLocation,'needsEndTime':needsEndTime,'remarks':remarks,'needsType':2 }

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

    req = json.loads(request.body)
    enterid = req['id']
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

    :param request: 农民工id
    :return: 需求列表
    """
    req = json.loads(request.body)
    farid = req['id']
    foreman = Foreman.objects.get(id = farid)
    allfarmers = Farmers.objects.all()
    farmerTypeList = []
    for farmers in allfarmers:
        farmerTypeList.append(farmers.type)
    allneeds = Needs.objects.all()
    needsList = []
    for need in allneeds:
        if need.needsType == 2:
            if need.needsFarmerType in farmerTypeList:
                serializer = NeedsSerializer(need)
                needsList.append(serializer.data)

    mydict = {'result': SUCCESS, 'msg': '获取成功', 'needsList': needsList}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def deal_needs(request):#  包工头接受/拒绝需求
    """
    POST

    :param request:包工头id，列表（需求id，接受/拒绝）
    :return:成功/失败
    """

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

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def auto_begin_needs():#  自动开始需求（根据系统时间）
    """

    :return:
    """
    # 定期检测调用此函数
    # 置需求状态
    # 新增到此需求对应各个包工头的订单



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


def auto_time(): #  时间定期检测
    """
    时间检测，每过一天检测一次。需求开工or取消
    :return:
    """