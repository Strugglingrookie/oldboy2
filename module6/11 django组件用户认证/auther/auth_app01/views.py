from django.shortcuts import render, redirect, HttpResponse
from auth_app01.myforms import Form
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')


def regist(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            user = None

            # 注意创建用户的时候要用create_user方法  用create的话不会对密码进行加密
            res = User.objects.create_user(username=username,email=email,password=pwd)

            # 注册完成之后 调用 authenticate() 进行认证得到一个  User  对象
            if res:
                user = authenticate(username=username, password=pwd)

            # login函数接受一个HttpRequest对象，以及一个认证了的User对象
            # login函数使用django的session框架给某个已认证的用户附加上sessionid等信息
            # 链接跳转到index后 会带上sessionid信息，且 request.user 定义成了一个全局变量任何地方都可以用，包括模板
            if user:
                login(request, user)

            return redirect('/app01/index/')
        else:
            print(form.cleaned_data)
            print(form.errors)
        return render(request, 'regist.html', locals())
    else:
        form = Form()
        return render(request, 'regist.html', locals())


def mylogin(request):
    return render(request, 'login.html')


def logout(request):
    return redirect( '/index/')