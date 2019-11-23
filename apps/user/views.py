from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
import json
from user.models import Enterprise, Farmers
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from user.serializer import EnterpriseSerializer, FarmersSerializer
#from user.forms import InfoForm
import logging as log


def index(request):
    return render(request,"index.html")

# 注册(企业1、农民工2)[小程序返回给哪里？]
def register(request):
    """
    POST
    :param request: 用户名、密码、web/mini
    :return:注册成功or失败
    """
    print(request.body)
    #print(aaa)
    log.info(request.body)
    if request.method == "POST":
        print(request.body)
        req = json.loads(request.body)
        print(req)
        username = req['username']
        password = req['password']
        status = req['user_type']  ## web or mini

        if status == "web" :  # 来自web端的数据  ——————企业

            if Enterprise.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
            else:
                userPassword = make_password(password, None, 'pbkdf2_sha256')
                # userName = username
                data_dict = {'name': username, 'password': userPassword}

                serializer = EnterpriseSerializer(data=data_dict)
                serializer.is_valid(raise_exception=True)
                serializer.save()  # 数据库新增信息
                # messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'msg': msg}
                print("注册成功")
                # return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return HttpResponse(serializer.data, content_type="application/json")
                # return render(request,'login.html',{'msg':'注册成功'}
        if status == "mini": #  小程序端民工
            if Farmers.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
            else:
                userPassword = make_password(password, None, 'pbkdf2_sha256')
                # userName = username
                data_dict = {'name': username, 'password': userPassword}

                serializer = FarmersSerializer(data=data_dict)
                serializer.is_valid(raise_exception=True)
                serializer.save()  # 数据库新增信息
                # messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'msg': msg}
                print("注册成功")
                # return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")


def login(request):  # 登录
    """
    POST
    :param request: 用户名、密码、mag/ent/far
    :return:——此处结合前端刚登入的界面！
            mag:管理人员id，待审核列表？
             ent:企业id，需求列表？审核状态？
             far：包工头id，需求邀请？
    """
    result = ""
    print(request.body)
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        username = req['username']
        password = req['password']
        status = req['user_type']
        if status == 'web':
            thisUser = Enterprise.objects.filter(name=username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret:
                        serializer = EnterpriseSerializer(user)
                        msg = "登录成功"
                        return HttpResponse(json.dumps(serializer.data))
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'msg': msg}
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'msg': msg}
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',json.dumps(mydict))

def change_password(request): #修改密码 --登录时
    """

    :param request: 用户名、新密码
    :return:成功/失败
    """

    # 判断数据库中是否有这个用户
    # 若有 修改密码
    # 若没有 修改失败

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def ent_info_post(request):  # 企业信息提交
    """
    POST
    :param request: 企业id，企业各资质信息图片、企业名称等信息
    :return: 成功/失败
    """

    enterid = "1"
    #form = InfoForm(request.POST, request.FILES)
    print(request.body)

    images = request.FILES
    print(images)

    enter = Enterprise.objects.get(id=enterid)
    enter.icon = images['icon']
    enter.save();

    return HttpResponse("success")


    # print(request.body)
    # req = json.loads(request.body)
    # enterid = req['id']
    # images = request.FILES
    # icon = images['icon']
    # enter = Enterprise.objects.get(id=enterid)
    #
    # enter.icon = icon
    # enter.save()



    # 数据库新增信息

    # 将各信息存入数据库 序列化save
    # 状态设为待审核

    mydict = {'msg': 'success'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def ent_info_get(request):  # 企业信息获取（企业资料、审核结果）
    """
    GET
    :param request: 企业id
    :return:企业资料、审核结果、审核意见

    """

    # 根据企业id获取企业信息序列化

    enterid = "1"
    enter = Enterprise.objects.get(id=enterid)
    img = enter.icon
    print(img)
    #mydict = {'msg': ''}
    #return HttpResponse(json.dumps(mydict), content_type="application/json")
    return render(request,'show.html',{'icon':img})


def farmer_info_get(request):  # 包工头信息获取(查看自己的个人资料)
    """
    GET
    :param request: 包工头id
    :return: 包工头个人姓名、身份证。组内人数。名下农工列表姓名、身份证。需求们（已完成、正在进行）
    """

    # 根据包工头id获取包工头信息序列化（嵌套序列化？）

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def farmer_info_post(request):  # 包工头信息提交
    """
    POST
    :param request: 包工头id，包工头个人姓名、身份证。组内人数。名下农工列表姓名、身份证。
    :return: 成功/失败
    """
    # 包工头信息序列化save


    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def register_manager(request):
    """
    POST
    :param request: 管理员用户名、密码
    :return: 成功/失败 —— 当前管理员列表？
    """

def all_manager(request):
    """
    GET
    :param request:
    :return: 管理员用户列表（id、用户名）
    """


def get_auth_enterprise(request):#  获取企业审核列表-管理员用
    """
    GET
    :param request: 管理员登录状态？
    :return: 企业列表+各审核状态
    """

    # 获取所有企业列表和审核状态
    # （前端首先显示待审核企业）

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def post_auth_result(request): #  提交审核结果-管理员用
    """
    POST
    :param request: 列表：每项为：企业id、审核结果、审核意见
    :return: 成功/失败
    """

    # 置该企业审核字段

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")
