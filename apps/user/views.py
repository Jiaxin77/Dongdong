from django.contrib.messages import SUCCESS, ERROR
#from django.contrib.sites import requests
import requests
from django.http import JsonResponse, HttpResponse, request
from django.shortcuts import render


# Create your views here.
import json

#from rest_framework.views import APIView

from user.models import Enterprise, Farmers, Administrator, Foreman, FarmersMember
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from user.serializer import EnterpriseSerializer, FarmersSerializer, AdministratorSerializer, ForemanSerializer, \
    FarmersMemberSerializer
#from user.forms import InfoForm
import logging as log

URL = "https://api.weixin.qq.com/sns/jscode2session"
APPID = "wx2e0f6900788aba6c"
APPSECRET = "63a7faa02d7434f166b14cfe0dd75e92"

def test(request):
    req = json.loads(request.body)
    id = req['id']
    foreman = Foreman.objects.get(id=id)
    fore_ser = ForemanSerializer(foreman)
    mydict = {'msg': fore_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")





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
    ##print(request.body)
    if request.method == "POST":
        #print(request.body)
        req = json.loads(request.body)
        #print(req)
        username = req['username']
        password = req['password']
        status = req['user_type']  # ent/man/far

        if status == "ent":  # 来自web端的数据  ——————企业
            if Enterprise.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'result': ERROR,'msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                #print("用户名已存在")
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
                #print("注册成功")
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
                #print("用户名已存在")
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
                    #print("注册成功")
                    # return render(request,"register",{'data': json.dumps(mydict)})
                    return HttpResponse(json.dumps(mydict), content_type="application/json")
                # else:
                #     msg = "微信授权失败"
                #     mydict = {'msg': msg}
                #     #print(msg)
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
    #print(request.body)
    if request.method == "POST":
        req = json.loads(request.body)
        #print(req)
        username = req['username']
        #print(username)
        password = req['password']
        #print(password)
        status = req['user_type']
        #print(status)
        if status == 'ent':
            thisUser = Enterprise.objects.filter(name=username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret:
                        serializer = EnterpriseSerializer(user)
                        msg = "登录成功"

                        mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data,'user_type':'ent'}
                        #print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                        #print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                #print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',json.dumps(mydict))
        if status == 'mag':
            #print("magggg")
            thisUser = Administrator.objects.filter(name=username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret:
                        serializer = AdministratorSerializer(user)
                        msg = "登录成功"

                        mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data,'user_type':'mag'}
                        #print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                        #print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                #print(mydict)
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
                            #print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        elif user.openid == 'null':
                            msg = "登录成功"
                            mydict = {'result': SUCCESS, 'msg': msg, 'user': serializer.data}
                            user.openid = myid
                            user.save()
                            #print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        else:
                            msg = "微信授权失败"
                            mydict = {'result': ERROR, 'msg': msg, 'user': serializer.data}
                            #print(mydict)
                            return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
                    else:
                        msg = "密码错误，登录失败"
                        mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                        #print(mydict)
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
                        # return render(request,'login.html',json.dumps(mydict))
            else:
                msg = "用户名不存在"
                mydict = {'result': ERROR, 'msg': msg, 'user': '-1'}  # 前端不读user
                #print(mydict)
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
    #print(r)
    #print("rrrrr")
    #print(r.json())
    if 'openid' in r.json():
        openid = r.json()['openid']
        return openid
    else :
        errmsg = r.json()['errmsg']
        return -1


def change_password(request):  # 修改密码 --登录时
    """

    :param request: 用户名、新密码
    :return:成功/失败
    """

    req = json.loads(request.body)
    #print(req)
    status = req['user_type']  # 身份 far/ent/mag
    username = req['username']
    password = req['password']
    if status == 'far':
        foreman = Foreman.objects.filter(name=username)
        if foreman.exists():
            for user in foreman:
                user.password = make_password(password, None, 'pbkdf2_sha256')
                user.save()
                mydict = {'result': SUCCESS, 'msg': '修改成功！'}
                #print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
        else:
            mydict = {'result': ERROR, 'msg': '用户不存在！'}
            #print(mydict)
            return HttpResponse(json.dumps(mydict), content_type="application/json")

    if status == 'ent':
        enterprise = Enterprise.objects.filter(name=username)
        if enterprise.exists():
            for user in enterprise:
                user.password = make_password(password, None, 'pbkdf2_sha256')
                user.save()
                mydict = {'result': SUCCESS, 'msg': '修改成功！'}
                #print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
        else:
            mydict = {'result': ERROR, 'msg': '用户不存在！'}
            #print(mydict)
            return HttpResponse(json.dumps(mydict), content_type="application/json")
    if status == 'mag':
        manager = Administrator.objects.filter(name=username)
        if manager.exists():
            for user in manager:
                user.password = make_password(password, None, 'pbkdf2_sha256')
                user.save()
                mydict = {'result': SUCCESS, 'msg': '修改成功！'}
                #print(mydict)
                return HttpResponse(json.dumps(mydict), content_type="application/json")
        else:
            mydict = {'result': ERROR, 'msg': '用户不存在！'}
            #print(mydict)
            return HttpResponse(json.dumps(mydict), content_type="application/json")




    # 判断数据库中是否有这个用户
    # 若有 修改密码
    # 若没有 修改失败

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def ent_basicinfo_post(request): #  企业基本信息提交
    """
    POST
    :param request:企业id，用户名、在建工程名称、经营范围、企业介绍
    :return:
    """
    #print(request.body)
    req = json.loads(request.body)
    #print(req)
    id = req['id']
    #enterName = req['enterName']
    scope = req['scope']
    nowProject = req['nowProject']
    enterDes = req['enterDes']

    enter = Enterprise.objects.get(id=id)
    #enter.enterName = enterName
    enter.scope = scope
    enter.nowProject = nowProject
    enter.enterDes = enterDes
    enter.save()

    mydict = {'result': SUCCESS, 'msg': "提交成功！"}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def ent_name_post(request): #提交企业名称
    """
    POST
    :param request:
    :return:
    """
    req = json.loads(request.body)
    id = req['id']
    enterName = req['enterName']
    enter = Enterprise.objects.get(id=id)
    enter.enterName = enterName
    enter.authState = "审核中"
    enter.save()
    mydict = {'result': SUCCESS, 'msg': "提交成功！"}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def ent_info_post(request):  # 企业资质信息提交
    # （营业执照、建筑资质、安全许可证、社保缴费证明、拟用工项目中标通知书或其他文件、商业项目保险、无纳税异常声明、规划许可证、施工许可证、土地使用证、开工报告）
    """
    POST
    :param request: 企业id，企业各资质信息图片
    :return: 成功/失败
    """

    #print(request)
    ##print(request.body)
    # req = request.body
    # id = req['id']
    #print(request.POST)
    files = request.FILES
    #print(files)
    id = request.POST.get('id') #企业id
    #print(id)

    enter = Enterprise.objects.get(id=id)

    files = request.FILES
    #print(files)
    if 'businessLicense' in files.keys():
        businessLicense = files['businessLicense']
        enter.businessLicense = businessLicense
    if 'constructionQUAL' in files.keys():
        constructionQUAL = files['constructionQUAL']
        enter.constructionQUAL = constructionQUAL
    if 'securityLicense' in files.keys():
        securityLicense = files['securityLicense']
        enter.securityLicense = securityLicense
    if 'socialSecurityCert' in files.keys():
        socialSecurityCert = files['socialSecurityCert']
        enter.socialSecurityCert = socialSecurityCert
    if 'noticeOfBid' in files.keys():
        noticeOfBid = files['noticeOfBid']
        enter.noticeOfBid = noticeOfBid
    if 'businessItemInsurance' in files.keys():
        businessItemInsurance = files['businessItemInsurance']
        enter.businessItemInsurance = businessItemInsurance
    if 'noTaxExpStatement' in files.keys():
        noTaxExpStatement = files['noTaxExpStatement']
        enter.noTaxExpStatement = noTaxExpStatement
    if 'planningPermit' in files.keys():
        planningPermit = files['planningPermit']
        enter.planningPermit = planningPermit
    if 'constructionPermit' in files.keys():
        constructionPermit = files['constructionPermit']
        enter.constructionPermit = constructionPermit
    if 'landUseCert' in files.keys():
        landUseCert = files['landUseCert']
        enter.landUseCert = landUseCert
    if 'startReport' in files.keys():
        startReport = files['startReport']
        enter.startReport = startReport
    enter.authState = "审核中"
    enter.save()
    mydict = {'result': SUCCESS, 'msg': "提交成功！"}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


    # #print(request.body)
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
    :return:企业资料（基本信息+资质信息）、审核结果、审核意见

    """

    # 根据企业id获取企业信息序列化

    enterid = request.GET.get('id') ####get用！

    #enterid = "1"
    enter = Enterprise.objects.get(id=enterid)
    #img = enter.icon
    ##print(img)
    enter_ser = EnterpriseSerializer(enter)

    mydict = {'msg': 'success','result':enter_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")
    #return render(request,'show.html',{'icon':img})



def foreman_info_get(request):  # 包工头信息获取(查看自己的个人资料)
    """
    GET
    :param request: 包工头id
    :return: 包工头个人姓名、身份证。组内人数。名下农工列表姓名、身份证。需求们（已完成、正在进行）
    """
    id = request.GET.get('id')
    # 根据包工头id获取包工头信息序列化（嵌套序列化？）
    # #print(request.body)
    # req = json.loads(request.body)
    # #print(req)
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
    #print(request.body)
    req=json.loads(request.body)
    id=req['id']

    #file = json.loads(request.FILES)
    #name = req['name']
    IDCard = req['idcard']
    phonenumber = req['phonenumber']
    bank=req['bank']
    banknumber = req['banknumber']

   # images = request.FILES
   # icon = images['icon']


    foreman = Foreman.objects.get(id=id)
    #foreman.name = name
    foreman.IDCard = IDCard
    foreman.phonenumber = phonenumber
    foreman.Bank = bank
    foreman.BankNumber = banknumber

    #foreman.
    foreman.save()
    mydict = {'result':SUCCESS,'msg':"提交成功！"}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def foreman_add_group(request): #包工头添加小组
    """
    #POST
    :param request: 包工头id、小组信息
    :return: 成功/失败
    """
    #print(request.body)
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

def forman_show_group(request): #包工头展示小组

    """
    GET
    :param request: 包工头id
    :return: 小组列表
    """
    forid = request.GET.get('id')
    foreman = Foreman.objects.get(id=forid)
    groups = Farmers.objects.filter(leader=foreman) #leader为该包工头的
    group_ser = FarmersSerializer(groups,many=True) #序列化

    # 名称组合
    group_list = []
    for group in groups:
        name = group.type + str(group.classNumber)

        one_group = {"id": group.id, "name": name, "memberNumber": group.memberNumber,"status":group.authState}
        group_list.append(one_group)

    mydict = {'result': SUCCESS, 'msg': '获取成功','data':group_list, }
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def member_add_pic(request): #添加组员审核照片
    """

    :param request:
    :return:
    """


def group_add_member(request): #添加组员
    """
    POST
    :param request: 组的id，组员list（身份证、姓名）
    :return:是否成功
    """
    #print(request)
    #print(request.POST)
    #req = json.loads(request.body)
    #req = request.body


    # #print(req)
    # id = req['id']  # 组号
    # name = req['name']
    # phonenumber = req['phonenumber']
    # idcard = req['idcard']

    id=request.POST.get('id')
    #print(id)
    name = request.POST.get('name')
    #print(name)
    phonenumber = request.POST.get('phonenumber')
    idcard = request.POST.get('idcard')
    farmer =Farmers.objects.get(id=id)




    images = request.FILES
    #print(images)
    auth = images['auth']
    #auth = images['auth']

    #, authInfo = auth
    FarmersMember.objects.create(name=name, phoneNumber=phonenumber, IDCard=idcard, group=farmer,authInfo = auth)
    farmer.memberNumber = farmer.memberNumber+1
    #farmer.authInfo = auth
    farmer.authState = "审核中"
    farmer.save()
    mydict = {'result': SUCCESS, 'msg': '添加成功'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def group_show_member(request):#展示该组成员
    """
    GET
    :param request: 组的id
    :return: 成员列表
    """
    id = request.GET.get('id') #组号
    farmer = Farmers.objects.get(id=id)
    members = FarmersMember.objects.filter(group=farmer)
    members_ser =FarmersMemberSerializer(members, many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'data': members_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def register_manager(request):  # 新增管理员
    """
    POST
    :param request: 管理员用户名、密码
    :return: 成功/失败 —— 当前管理员列表？
    """
    if request.method == "POST":
        #print(request.body)
        req = json.loads(request.body)
        #print(req)
        username = req['username']
        password = req['password']
        if Administrator.objects.filter(name=username):  # 已存在
                messages.error(request, "用户名已存在")
                msg = "用户名已存在"
                mydict = {'result': 'false','msg': msg}
                # return render(request,'login.html',{'msg':'用户名已存在'})
                #print("用户名已存在")
                # return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")

        else:
                userPassword = make_password(password, None, 'pbkdf2_sha256')
                # userName = username
                data_dict = {'name': username, 'password': userPassword}

                Administrator.objects.create(name=username,password=userPassword)

                # serializer = AdministratorSerializer(data=data_dict)
                # serializer.is_valid(raise_exception=True)
                # serializer.save()  # 数据库新增信息
                # messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'result': 'true','msg': msg}
                #print("注册成功")
                # return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                # return render(request,'login.html',{'msg':'注册成功'}


def all_manager(request):  # 获取所有管理员
    """
    GET
    :param request:
    :return: 管理员用户列表（id、用户名）
    """
    adminList = Administrator.objects.all()
    #admin_ser = AdministratorSerializer(adminList, many=True)
    index=0
    AllAdmin = []
    for admin in adminList:
        thisAdmin = {'index':index,'id':admin.id,'name':admin.name}
        index = index+1
        AllAdmin.append(thisAdmin)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'data': AllAdmin}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def delete_manager(request):  # 删除管理员
    """
    POST
    :param request: 要删除的管理员id列表
    :return: 更新后的管理员列表
    """
    req = json.loads(request.body)
    manager_list = req['del_list']
    for manid in manager_list:
        manager = Administrator.objects.get(id=manid)
        if manager:
            manager.delete()
        else:
            all_manager = Administrator.objects.all()
            manager_ser = AdministratorSerializer(all_manager, many=True)
            mydict = {'result': ERROR, 'msg': '用户不存在！', 'data': manager_ser.data}
            return HttpResponse(json.dumps(mydict), content_type="application/json")
    all_manager = Administrator.objects.all()
    manager_ser = AdministratorSerializer(all_manager, many=True)
    mydict = {'result': SUCCESS, 'msg': '删除成功', 'data': manager_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_auth_enterprise(request):#  获取企业列表-管理员用
    """
    GET
    :param request: 管理员登录状态？
    :return: 企业列表+各审核状态
    """

    # 获取所有企业列表和审核状态
    # （前端首先显示待审核企业）
    enterList = Enterprise.objects.all()
    enter_ser = EnterpriseSerializer(enterList, many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'data': enter_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_enter_auth_info(request): #  获取审核某个企业-管理员用 （提供下载功能） ——获取企业详情
    """
    GET
    :param request: 企业id
    :return: 企业信息
    """

    enterid = request.GET.get('id')
    enter = Enterprise.objects.get(id=enterid)
    enter_ser = EnterpriseSerializer(enter)
    mydict = {'result': SUCCESS, 'msg': '获取成功','data':enter_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def post_enter_auth_result(request):  # 提交企业审核结果-管理员用
    """
    POST
    :param request: 列表：每项为：企业id、审核结果、审核意见
    :return: 成功/失败
    """

    # 置该企业审核字段

    req = json.loads(request.body)
    id = req['id']
    authState = req['authState']
    authAdvice = req['authAdvice']
    enter = Enterprise.objects.get(id=id)
    enter.authState=authState
    enter.authAdvice=authAdvice
    enter.save()

    mydict = {'result': SUCCESS, 'msg': '提交成功'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_all_groups(request):  # 获取农民工小组列表
    """
    GET
    :param request:
    :return:小组列表(小组id，工头姓名、小组名称如木工01组、审核状态)
    """
    groupList = Farmers.objects.all()
    group_ser = FarmersSerializer(groupList,many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'data': group_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_one_group_info(request):  # 获取某单个小组信息
    """
    GET
    :param request: 小组id
    :return: 工头姓名、工头资料、小组名称、小组成员信息、审核状态
    """
    groupid = request.GET.get('id') #小组id
    group = Farmers.objects.get(id=groupid)
    group_ser = FarmersSerializer(group)
    members = FarmersMember.objects.filter(group=group)
    members_ser = FarmersMemberSerializer(members,many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功', 'group_data': group_ser.data,'members':members_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def post_group_auth_info(request):  # 提交某个小组审核结果
    """
    POST
    :param request: 小组id、审核结果、审核意见
    :return: 成功/失败
    """
    req = json.loads(request.body)
    id = req['id']
    auth_result = req['auth_result']

    group = Farmers.objects.get(id=id)
    group.authState = auth_result
    group.save()
    mydict = {'result': SUCCESS, 'msg': '提交成功'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")
