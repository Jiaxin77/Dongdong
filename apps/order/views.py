import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def save_orders(): #开工时产生订单
    """

    :return: 成功/失败
    """
    #新建订单字段，记录当前时间

def cacel_orders(): #取消订单
    """
    订单号？
    :return:成功/失败
    """

    #订单状态设为已取消（并不删除）

def cancel_farmer_order(request): #企业取消某包工头订单
    """
    POST
    :param request: 需求ID、包工头id（或直接给订单ID？）
    :return: 成功/失败

    """
    # 调用取消订单函数


def get_orders(request):  # 获取需求对应订单
    """
    GET
    :param request: 需求id
    :return: 订单列表
    """

    # 根据需求id查订单序列化列表

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_all_money(request): # 获取总金额
    """

    :param request: 企业id
    :return: 总金额、总给app金额、给包工头金额
    """

    # 获取已完成订单金额的和
    # 按比例计算返回前端
    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def get_all_orders(request): # 获取总订单 -- 管理员用
    """
    GET
    :param request: none
    :return: 所有订单简要序列化信息

    """

def get_order_info(request): # 根据某订单id获取某订单信息 -- 管理员用
    """
    GET
    :param request: 订单id
    :return: 某订单序列化信息
    """
