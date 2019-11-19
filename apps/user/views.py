from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
import json
from user.models import Enterprise
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def login(request):
    return render(request,"login.html")


# 注册(企业1、农民工2)[小程序返回给哪里？]
def register(request):
    if request.method == "POST":
        req = json.loads(request.body)
        username = req['username']
        password = req['password']
        status = req['user_type'] ## web or mini
        if status == "web":#来自web端的数据
            if Enterprise.objects.filter(name=username):
                messages.error(request,"用户名已存在")
                msg = "用户名已存在"
                mydict = {'msg':msg}
                #return render(request,"login.html")
                #return render(request,'login.html',{'msg':'用户名已存在'})
                print("用户名已存在")
                #return render(request,"register",{'data':json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
            else:
                userPassword = make_password(password,None,'pbkdf2_sha256')
                userName = username
                Enterprise.objects.create(name=userName,password=userPassword)
                messages.success(request, "注册成功")
                msg = "注册成功"
                mydict = {'msg':msg}
                print("注册成功")
                #return render(request,"register",{'data': json.dumps(mydict)})
                return HttpResponse(json.dumps(mydict), content_type="application/json")
                #return render(request,'login.html',{'msg':'注册成功'})


def login(request):  # 登录
    result = ""
    if request.method == "POST":
        req = json.loads(request.body)
        username = req['username']
        password = req['password']
        status = req['user_type']
        if status == 'web':
            thisUser = Enterprise.objects.filter(name = username)
            if thisUser.exists():
                for user in thisUser:
                    ret = check_password(password, user.password)
                    if ret :
                        userid = user.id
                        msg = "登录成功"
                        mydict = {'id':userid,'name':username,'msg':msg}
                        return HttpResponse(json.dumps(mydict), content_type="application/json")
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



def entInfoPost(request): #企业信息提交

    mydict = {'msg': ''}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

