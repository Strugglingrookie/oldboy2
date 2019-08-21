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
        res = {"user": None, "msg": None}
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            phone = form.cleaned_data['tel']
            file_obj = request.FILES.get('avatar')
            '''
            if not file_obj:
                # 注意创建用户的时候要用create_user方法  用create的话不会对密码进行加密
                UserInfo.objects.create_user(username=username,email=email,password=pwd,phone_num=phone)
            else:
                # django会将文件对象下载到项目的根目录avatars(model指定的路径)文件夹中
                # （如果没有avatars文件夹，Django会自动创建）,user_obj的avatar存的是文件的相对路径。
                
                # 如果settings中 配置了 MEDIA_ROOT=os.path.join(BASE_DIR,"media")
                # django会将文件对象下载到配置目录下的avatars中，没有则创建。
                
                UserInfo.objects.create_user(username=username,email=email,password=pwd,phone_num=phone,avatar=file_obj)
           '''
            # 上面的写法不规范，优化后如下
            extra = {}
            if file_obj:
                extra = {"avatar":file_obj}
            UserInfo.objects.create_user(username=username, email=email, password=pwd, phone_num=phone,**extra)

            res["user"] = form.cleaned_data.get("name")
        else:
            res["msg"] = form.errors
        return JsonResponse(res)
    else:
        form = UserForms()
        return render(request, 'regist.html', locals())


def valid_img(request):
    data = valid_code_data.get_valid_img(request)
    return HttpResponse(data)