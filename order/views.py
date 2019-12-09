from django.shortcuts import render

# Create your views here.
import json
import random

from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse
from django.shortcuts import render
from order.models import Order
from order.serializer import OrderSerializer
import time

# Create your views here.

# 金额分配比例
# 给app的
price_to_app = 0.2


# 订单id生成
def create_order_id(needid, userid):
    """

    :return:
    """
    # print(time.localtime())
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec

    year_str = str(year).zfill(4)
    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2)
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    second_str = str(second).zfill(2)

    random_str = str(random.randint(0, 99)).zfill(2)
    time_str = year_str + month_str + day_str + hour_str + minute_str + second_str
    orderid = time_str + random_str + str(needid) + str(userid)
    return orderid


def save_orders():  # 开工时产生订单
    """

    :return: 成功/失败
    """
    # 新建订单字段，记录当前时间


def cacel_orders():  # 取消订单
    """
    订单号？
    :return:成功/失败
    """

    # 订单状态设为已取消（并不删除）


def cancel_farmer_order(request):  # 企业取消某包工头订单
    """
    POST
    :param request: 需求ID、包工头id（或直接给订单ID？）
    :return: 成功/失败

    """
    # 调用取消订单函数


def get_orders(request):  # 获取需求对应订单!!!!!!【！！！】
    """
    GET
    :param request: 需求id
    :return: 订单列表（订单id，订单编号、交易实践、工头名字、人员姓名、编号？、身份证号、联系方式，订单总额）+所有订单总额
    """

    # 根据需求id查订单序列化列表

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def pay_for_orders(request):  # 支付订单
    """
    置订单状态为交易完成
    POST
    :param request:订单id列表
    :return:
    """
    req = json.loads(request.body)
    idList = req['idList']  # 流水号
    for id in idList:
        order = Order.objects.get(id=id)
        order.status = "已完成"
        order.save()
    mydict = {'result': SUCCESS, 'msg': '交易完成！'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


# def get_all_money(request):  # 获取总金额
#     """
#
#     :param request: 企业id
#     :return: 总金额、总给app金额、给包工头金额
#     """
#
#     # 获取已完成订单金额的和
#     # 按比例计算返回前端
#     mydict = {'msg': ''}
#     return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_order_info(request):  # 根据某订单id获取某订单信息 -- 管理员用
    """
    GET
    :param request: 订单id
    :return: 某订单序列化信息
    """


#  订单下载


def get_all_orders(requests):  # 获取所有订单列表——管理员用
    """
    get
    :param requests:
    :return: 订单列表，总收益？
    """
    orders = Order.objects.all()
    order_ser = OrderSerializer(orders, many=True)
    mydict = {'result': SUCCESS, 'msg': '成功获取！', 'data': order_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")