from django.shortcuts import render, HttpResponse
from ajax_app01.models import *
from django.db.models import Q
import json

# Create your views here.


def regist(request):
    method = request.method
    if method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        select_res = UserInfo.objects.filter(Q(name=name)|Q(user_detail__nickname=nickname)).exists()
        res = {"code":None,"msg":None}
        if select_res:
            res["code"]="100000"
            res["msg"]="用户已存在!"
        else:
            detail = UserDetail.objects.create(nickname=nickname, phone=phone)
            UserInfo.objects.create(name=name, password=pwd, user_detail=detail)
            res["code"] = "000000"
            res["msg"] = "注册成功!"
        return HttpResponse(json.dumps(res))
    else:
        return render(request, 'regist.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        select_res = UserInfo.objects.filter(name=name,password=pwd).exists()
        res = {"user":None,"msg":None}
        if select_res:
            res["user"] = name
        else:
            res["msg"] = "用户名或密码错误！"
        return HttpResponse(json.dumps(res))
    return render(request, 'login.html')


def check(request):
    method = request.method
    if method == 'POST':
        dic = {'name':'用户名','nickname':'用户昵称','phone':'手机号'}
        print(request.body)  # 原始的请求体数据  不管啥类型的请求数据都取的到
        print(request.POST)  # POST请求数据  if contentType==urlencoded ,request.POST才有数据
        req_data = json.loads(request.body.decode('utf8'))
        type = req_data['type']
        value = req_data['value']
        if type == 'name':
            res = UserInfo.objects.filter(name=value).exists()
        elif type == 'nickname':
            res = UserInfo.objects.filter(user_detail__nickname=value).exists()
        else:
            res = UserInfo.objects.filter(user_detail__phone=value).exists()
        if res:
            return HttpResponse('{"code":"100000","msg":"%s已存在！"}'%dic[type])
        else:
            return HttpResponse('{"code":"000000","msg":"校验成功！"}')
    else:
        return render(request, 'index.html')


def file(request):
    import os
    from ajax.settings import STATICFILES_DIRS
    if request.method == 'POST':
        if request.is_ajax():
            print('--------------------------ajax--------------------------')
            print(request.body)  # 原始的请求体数据
            print(request.GET)  # GET请求数据
            print(request.POST)  # POST请求数据  if contentType==urlencoded ,request.POST才有数据
            print(request.FILES)  # 上传的文件数据
            file_obj = request.FILES.get('imgfile')
            with open(os.path.join(STATICFILES_DIRS[0],file_obj.name), 'wb') as f:
                for line in file_obj:
                    f.write(line)
        else:
            print('--------------------------form--------------------------')
            print(request.body)  # 原始的请求体数据
            print(request.GET)  # GET请求数据
            print(request.POST)  # POST请求数据  if contentType==urlencoded ,request.POST才有数据
            print(request.FILES)  # 上传的文件数据
            file_obj = request.FILES.get('imgfile')
            with open(os.path.join(STATICFILES_DIRS[0],file_obj.name), 'wb') as f:
                for line in file_obj:
                    f.write(line)
        return HttpResponse('OJBK!')
    return render(request, 'file.html')