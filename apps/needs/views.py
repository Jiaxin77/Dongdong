from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


def post_needs(request):  # 企业发布需求
    """
    POST
    :param request: 企业id、需求信息们
    :return: 成功/失败
    """

    # 需求序列化信息存储
    # （暂时不用的匹配）


    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_needs(request): #  企业查看需求列表
    """
    GET
    :param request: 企业id
    :return: 企业当前需求们（已发布、已取消等）
    """

    #根据企业id获取
    mydict = {'msg': ''}
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
    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def auto_begin_needs():#  自动开始需求（根据系统时间）
    """

    :return:
    """



def cancel_needs(request):#  企业取消需求
    """

    :param request: 需求id
    :return: 成功/失败
    """
    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def auto_cancel_needs():# 系统自动取消需求（到开工时间未招齐）
    """

    :return:
    """