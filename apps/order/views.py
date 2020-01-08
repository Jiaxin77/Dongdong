from django.shortcuts import render

# Create your views here.
import json
import random

from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse
from django.shortcuts import render

from needs.models import Needs
from order.models import Order
from order.serializer import OrderSerializer
import time

# Create your views here.

# 金额分配比例
# 给app的
from user.models import FarmersMember
from user.serializer import FarmersMemberSerializer, FarmersSerializer

price_to_app = 0.2
price_total = 1.0972

# 订单id生成
def create_order_id(needid, userid):
    """

    :return:
    """
    # ###print(time.localtime())
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
    :return: 订单列表（订单id，订单编号、交易时间、工头名字、人员姓名、、身份证号、联系方式，订单总额）+所有订单总额
    """

    # 根据需求id查订单序列化列表
    needid = request.GET.get('id') #需求id
    need = Needs.objects.get(id=needid)
    orders = Order.objects.filter(needId=need).order_by('-beginTime')
    orders_ser = OrderSerializer(orders, many=True)
    allMoney = 0
    allMoneyToFarmers = 0
    allMoneyToApp = 0
    allMoneyNum = 0
    allMoneyToFarmersNum = 0
    allMoneyToAppNum = 0
    orderList = []
    for order in orders:
        group = order.farmers.get(order=order)
        members = FarmersMember.objects.filter(group=group)
        members_ser = FarmersMemberSerializer(members,many=True)
        thisOrder={'id':order.id,'pid':order.p_id,'lastModified':str(order.lastModified),'money':round(order.money,2),'moneyToFarmers':round(order.moneyToFarmers,2),'moneyToApp':round(order.moneyToApp,2),'status':order.status,'group_leader':group.leader.name,'members':members_ser.data}
        allMoney=allMoney+round(order.money,2)
        allMoneyToFarmers=allMoneyToFarmers+round(order.moneyToFarmers,2)
        allMoneyToApp=allMoneyToApp+round(order.moneyToApp,2)
        orderList.append(thisOrder)
    allMoneyNum = allMoney * price_total
    allMoneyToAppNum = allMoney *(price_total - 1)
    allMoneyToFarmersNum = allMoney * 1
    mydict = {'result': SUCCESS,'msg':'成功获取','data':orderList,'allMoney':round(allMoneyNum,2),'allMoneyToFarmers':round(allMoneyToFarmersNum,2),'allMoneyToApp':round(allMoneyToAppNum,2)}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def pay_for_orders(request):  # 支付订单
    """
    置订单状态为交易完成
    POST
    :param request:订单id列表
    :return:
    """
    req = json.loads(request.body)
    needid = req['needid']
    need = Needs.objects.get(id=needid)
    #idList = req['idList']  # 流水号
    orderList = Order.objects.filter(needId=need).order_by('-beginTime')
    #AllOrders = Order.objects.all()
    for order in orderList:
        #order = Order.objects.get(id=id)
        order.status = "已完成"
        order.save()
        #如果需求的订单全部支付，则状态为已完成
        need = order.needId
        myOrderList = Order.objects.filter(needId=need).order_by('-beginTime')
        flag = True
        for myOrder in myOrderList:
            if myOrder.status != "已完成":
                flag = False
        if flag:
            need.needsType = "交易成功"
            need.save()

    #对某个需求来说！
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
    id = request.GET.get("pid") #订单pid
    order = Order.objects.get(p_id=id)
    order_ser = OrderSerializer(order)
    group = order.farmers.get(order=order)
    group_ser = FarmersSerializer(group)
    members = FarmersMember.objects.filter(group=group)
    members_ser = FarmersMemberSerializer(members,many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功！','order_data':order_ser.data,'group_data':group_ser.data,'member_data':members_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

#  订单下载


def get_all_orders(request):  # 获取所有订单列表——管理员用
    """
    get
    :param request:
    :return: 订单列表，总收益？
    """
    orders = Order.objects.all().order_by('-beginTime')
    order_ser = OrderSerializer(orders, many=True)
    mydict = {'result': SUCCESS, 'msg': '成功获取！', 'data': order_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def get_need_orders(request): #获取按需求的订单信息列表
    """
    GET
    :param request:
    :return:
    """
    needs = Needs.objects.all()
    needsList = []
    orderList = []
    order_count = 1
    for need in needs:
        orders = Order.objects.filter(needId=need).order_by('-beginTime')
        ordernum = 0
        orderMoney = 0
        orderMoneytoApp = 0
        orderMoneytoFarmers = 0

        orderFlag = "交易成功"
        for order in orders:
            ordernum = ordernum+1
            orderMoney = orderMoney+round(order.money,2)
            orderMoneytoApp = orderMoneytoApp+round(order.moneyToApp,2)
            orderMoneytoFarmers = orderMoneytoFarmers+round(order.moneyToFarmers,2)
            groups = order.farmers.all()
            for person in groups:
                thisGroup = person

            thisOrder = {'numid':order_count,'enterName':need.enterId.enterName,'needName':need.enterId.nowProject,'needsFarmerType':need.needsFarmerType,'orderStatus':order.status,'orderid':order.id,'orderMoney':round(order.money,2),'orderMoneyToFarmer':round(order.moneyToFarmers,2),'foreman':thisGroup.leader.name,'bank':thisGroup.leader.Bank,'banknum':thisGroup.leader.BankNumber,'idcard':thisGroup.leader.IDCard}
            orderList.append(thisOrder)
            order_count = order_count+1
            if order.status == "交易中":
                orderFlag = "待支付"
        orderMoneyNum = orderMoney * price_total
        orderMoneyToAppNum = orderMoney * (price_total - 1)
        orderMoneyToFarmersNum = orderMoney * 1
        thisNeed = {'id':need.id,'enterName':need.enterId.enterName,'needDes':need.needsDes,'needsFarmerType':need.needsFarmerType,'needsType':need.needsType,'orderNum':ordernum,'orderMoney':round(orderMoneyNum,2),'orderMoneyToApp':round(orderMoneyToAppNum,2),'orderMoneyToFarmers':round(orderMoneyToFarmersNum,2),'needsPayStatus':orderFlag}
        if need.needsType == "匹配完成待支付" or need.needsType == "交易成功":
            needsList.append(thisNeed)

    mydict = {'result': SUCCESS, 'msg': '成功获取！', 'data': needsList,'orderData':orderList}
    return HttpResponse(json.dumps(mydict), content_type="application/json")