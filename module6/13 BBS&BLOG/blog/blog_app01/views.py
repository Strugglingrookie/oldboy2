from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from blog import settings
from blog_app01.utils import valid_code_data
from blog_app01.myforms import UserForms
from blog_app01.models import UserInfo




def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        res = {"user":None, "msg":""}
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        valid_code = request.POST.get('valid_code')
        valid_code = valid_code.upper() if valid_code else valid_code
        if valid_code.upper() == valid_code:
            user = auth.authenticate(username=name, password=pwd)
            if user:
                auth.login(request, user)
                res['user'] = user.username
            else:
                res['msg'] = "用户名或密码有误！"
        else:
            res['msg'] = "验证码有误！"
        return JsonResponse(res)
    return render(request, 'login.html')


def regist(request):
    if request.method == 'POST':  # 或者 if request.is_ajax():
        form = UserForms(request.POST)
        res = response = {"user": None, "msg": None}
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            phone = form.cleaned_data['tel']
            # 注意创建用户的时候要用create_user方法  用create的话不会对密码进行加密
            res = UserInfo.objects.create_user(username=username,email=email,password=pwd,phone_num=phone)
            response["user"] = form.cleaned_data.get("username")
        else:
            res["msg"] = form.errors
        return JsonResponse(res)
    else:
        form = UserForms()
        return render(request, 'regist.html', locals())


def valid_img(request):
    data = valid_code_data.get_valid_img(request)
    return HttpResponse(data)