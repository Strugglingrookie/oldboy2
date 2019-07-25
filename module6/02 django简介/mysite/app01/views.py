from django.shortcuts import render,HttpResponse
from app01.tools import Mysql
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    log_url = reverse('log')  # 另一种反向解析
    time_url = reverse('tim')
    articles_url = reverse('achive',args=(2019,))  #当路径是一个正则表达式的时候，需要传参，有几个参数就传几个，否则会报错
    print(log_url)
    print(time_url)
    print(articles_url)
    method = request.method
    print(method)
    if method.lower() == 'post':
        req_data = request.POST
        print(req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        print('res',res)
        if res and isinstance(res,list):
            return render(request, 'index.html')
        else:
            return HttpResponse('username or password is wrong!')
    else:
        print(request.GET)
        # 反向解析在这一步做的，render会根据urls控制器传的name进行解析{% url 'log' %} ---> /app01/login/
        return render(request, 'login.html')

def favicon(request):
    return render(request,'favicon.ico')

def regist(request):
    return render(request,'register.html')

def timer(request):
    import datetime
    ctime = datetime.datetime.now()
    return render(request,'timer.html',{"time":ctime})

def special_case_2019(request):
    return HttpResponse('special_case_2019')

def year_archive(request,year):
    print(year)
    return HttpResponse('special_case_%s'%year)

def month_archive(request,year,month):
    print(year,month)
    return HttpResponse('special_case_%s_%s'%(year,month))

def day_archive(request,day,year,month):
    print(year,month,day)
    return HttpResponse('special_case_%s_%s_%s'%(year,month,day))