from django.contrib.messages import SUCCESS, ERROR
from django.contrib.sites import requests
from django.http import JsonResponse, HttpResponse, request
from django.shortcuts import render

import requests
# Create your views here.
import json

from rest_framework.views import APIView

from user.models import Enterprise, Farmers, Administrator, Foreman
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from user.serializer import EnterpriseSerializer, FarmersSerializer, AdministratorSerializer, ForemanSerializer
#from user.forms import InfoForm
import logging as log

URL = "https://api.weixin.qq.com/sns/jscode2session"
APPID = "wx2e0f6900788aba6c"
APPSECRET = "63a7faa02d7434f166b14cfe0dd75e92"

def index(request):
    # return render(request,"index.html")
    return HttpResponse(json.dumps("hhh"), content_type="application/json")

# 注册(企业1、农民工2)[小程序返回给哪里？]
def register(request):
    """
    POST
    :param request: 用户名、密码、web/mini
    :return:注册成功or失败
    """
    print(request.body)
    if request.method == "POST":
        print(request.body)
        req = json.loads(request.body)
        print(req)
        username = req['username']
        password = req['password']
        status = req['user_type']  # ent/man/far

        if status == "ent":  # 来自web端的数据  ——————企业

            if Enterprise.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'result': ERROR,'msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
            else:
                userPassword = make_password(password, None, 'pbkdf2_sha256') #密码加密
                data_dict = {'name': username, 'password': userPassword}
                # serializer = EnterpriseSerializer(data=data_dict)
                # serializer.is_valid(raise_exception=True)
                # serializer.save()  # 数据库新增信息
                Enterprise.objects.create(name=username, password=userPassword)
                # messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'result': SUCCESS,'msg': msg}
                print("注册成功")
                # return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return HttpResponse(serializer.data, content_type="application/json")
                # return render(request,'login.html',{'msg':'注册成功'}
        if status == "far": #  小程序端民工
            # code = req['code']
            if Foreman.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
            else:
                # myid = get_openid(code)
                # if myid != -1 :
                    userPassword = make_password(password, None, 'pbkdf2_sha256')
                    # userName = username
                    data_dict = {'name': username, 'password': userPassword, 'openid':'null'}

                    # serializer = ForemanSerializer(data=data_dict)
                    # serializer.is_valid(raise_exception=True)
                    # serializer.save()  # 数据库新增信息
                    Foreman.objects.create(name=username,password=userPassword)

                    # messages.success(request, "注册成功")
                    msg = "注册成功"
                    mydict = {'msg': msg}
                    print("注册成功")
                    # return render(request,"register",{'data': json.dumps(mydict)})
                    return HttpResponse(json.dumps(mydict), content_type="application/json")
                # else:
                #     msg = "微信授权失败"
                #     mydict = {'msg': msg}
                #     print(msg)
                #     # return render(request,"register",{'data': json.dumps(mydict)})
                #     return HttpResponse(json.dumps(mydict), content_type="application/json")





def login(request):  # 登录   ——目前登录改成了SUCCESS和ERROR，看能不能行
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
        print(username)
        password = req['password']
        print(password)
        status = req['user_type']
        print(status)
        if status == 'ent':
            thisUser = Enterprise.objects.filter(name=username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret:
                        serializer = EnterpriseSerializer(user)
                        msg = "登录成功"

                        mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data}
                        print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                        print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',json.dumps(mydict))
        if status == 'far':  #小程序农民工
            code = req['code']
            thisUser = Foreman.objects.filter(name=username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret:
                        serializer = ForemanSerializer(user)
                        #msg = "登录成功"
                        myid = get_openid(code)

                        if user.openid == myid and myid != -1 :
                            msg = "登录成功"
                            mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data}
                            print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        elif user.openid == 'null':
                            msg = "登录成功"
                            mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data}
                            user.openid = myid
                            user.save()
                            print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        else:
                            msg = "微信授权失败"
                            mydict = {'result': ERROR, 'msg': msg, 'user': serializer.data}
                            print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                        print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',json.dumps(mydict))


# class OpenidUtils(object):
#     def __init__(self,jscode):
#         self.url = "https://api.weixin.qq.com/sns/jscode2session"
#         self.appid = APPID  #从小程序要
#         self.secret = APPSECRET
#         self.jscode = jscode  # 前端传回的动态jscode

def get_openid(jscode):

    url = URL + "?appid=" +APPID + "&secret=" + APPSECRET + "&js_code=" + jscode + "&grant_type=authorization_code"
    r = requests.get(url)
    print(r)
    print("rrrrr")
    print(r.json())
    if 'openid' in r.json():
        openid = r.json()['openid']
        return openid
    else :
        errmsg = r.json()['errmsg']
        return -1

def change_password(request): #修改密码 --登录时
    """

    :param request: 用户名、新密码
    :return:成功/失败
    """

    req = json.loads(request.body)
    print(req)
    status = req['user_type'] #身份
    username = req['username']
    password = req['password']
    if status == 'far':
        foreman = Foreman.objects.filter(name=username)
        if foreman.exists():
            for user in foreman:
                user.password = make_password(password, None, 'pbkdf2_sha256')
                user.save()
                mydict = {'result': SUCCESS, 'msg': '修改成功！'}
                print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
        else:
            mydict = {'result': ERROR, 'msg': '用户不存在！'}
            print(mydict)
            return HttpResponse(json.dumps(mydict), content_type="application/json")



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


def foreman_info_get(request):  # 包工头信息获取(查看自己的个人资料)
    """
    GET
    :param request: 包工头id
    :return: 包工头个人姓名、身份证。组内人数。名下农工列表姓名、身份证。需求们（已完成、正在进行）
    """
    id = request.GET.get('id')
    # 根据包工头id获取包工头信息序列化（嵌套序列化？）
    # print(request.body)
    # req = json.loads(request.body)
    # print(req)
    # id = req['id']
    user= Foreman.objects.get(id=id)
    serializer = ForemanSerializer(user)
    data=serializer.data

    mydict = {'result':SUCCESS,'data':data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def foreman_info_post(request):  # 包工头信息提交
    """
    POST
    :param request: 包工头id，包工头个人姓名、身份证。组内人数。名下农工列表姓名、身份证。
    :return: 成功/失败
    """
    # 包工头信息序列化save

    req=json.loads(request.body)
    id=req['id']

    name = req['name']
    IDCard = req['idcard']
    foreman = Foreman.objects.get(id=id)
    foreman.name = name
    foreman.IDCard = IDCard
    foreman.save()
    mydict = {'result':SUCCESS,'msg':"提交成功！"}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def foreman_add_group(request): #包工头添加小组
    """

    :param request: 包工头id、小组信息
    :return: 成功/失败
    """
    req = json.loads(request.body)
    id = req['id'] #包工头id
    type = req['type']
    #memberNumber = req['memberNumber']
    #当前该工种有多少组
    groupList = Farmers.objects.filter(type=type)
    numberLen = len(groupList)
    number = numberLen+1
    foreman = Foreman.objects.get(id=id)
    Farmers.objects.create(classNumber=number,type=type,leader=foreman)
    data={'groupName':type+str(number)}
    mydict = {'result':SUCCESS,'msg': '添加成功','data':data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")















def register_manager(request):
    """
    POST
    :param request: 管理员用户名、密码
    :return: 成功/失败 —— 当前管理员列表？
    """
    if request.method == "POST":
        print(request.body)
        req = json.loads(request.body)
        print(req)
        username = req['username']
        password = req['password']
        if Administrator.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'result': 'false','msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")

        else:
                userPassword = make_password(password, None, 'pbkdf2_sha256')
                # userName = username
                data_dict = {'name': username, 'password': userPassword}

                serializer = AdministratorSerializer(data=data_dict)
                serializer.is_valid(raise_exception=True)
                serializer.save()  # 数据库新增信息
                # messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'result': 'true','msg': msg}
                print("注册成功")
                # return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',{'msg':'注册成功'}

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


def get_enter_auth_info(request): #  获取审核某个企业-管理员用 （提供下载功能）
    """
    GET
    :param request: 企业id
    :return: 企业信息
    """


def post_auth_result(request): #  提交审核结果-管理员用
    """
    POST
    :param request: 列表：每项为：企业id、审核结果、审核意见
    :return: 成功/失败
    """

    # 置该企业审核字段

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")
