from django.shortcuts import render,HttpResponse
from app01.tools import Mysql
from django.urls import reverse

# Create your views here.

def index1(request):
    return  render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def login(request):
    log_url = reverse('app01:log')  # 另一种反向解析 reverse
    print(log_url)  #  /app01/login/
    articles_url = reverse('app01:achive',args=(2088,))  #当路径是一个正则表达式的时候，需要传参，有几个分组就传几个，否则会报错
    print(articles_url)
    method = request.method
    if method.lower() == 'post':
        req_data = request.POST
        print(req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        if res and isinstance(res,list):
            return render(request, 'index2.html')
        else:
            return HttpResponse('username or password is wrong!')
    else:
        print(request.GET)
        # 反向解析在这一步做的，render会根据urls控制器传的name进行解析{% url 'log' %} ---> /app01/login/
        return render(request, 'login.html')

def regist(request):
    method = request.method
    if method.lower() == 'post':
        req_data = request.POST
        print(req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        if user and pwd:
            mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
            sql = "select * from user_info WHERE  name=%s"
            res = mysql_check.exec_sql(sql, user)
            if res and isinstance(res,list):
                return HttpResponse('username is already exits!')
            insert_sql = 'insert into user_info (name,password) VALUES (%s,%s) '
            mysql_check.exec_sql(insert_sql, user,pwd)
            return render(request, 'index2.html')
        return HttpResponse('username or password can not be empty !')
    return render(request,'register.html')

def timer(request):
    import datetime
    ctime = datetime.datetime.now()
    return render(request,'timer.html',{"time":ctime})

def special_case_2019(request):
    return HttpResponse('special_case_2019')

def year_archive(request,year):
    print(year)
    print(type(year))
    return HttpResponse('special_case_%s'%year)

def month_archive(request,year,month):
    print(year,month)
    return HttpResponse('special_case_%s_%s'%(year,month))

def day_archive(request,day,year,month):
    print(year,month,day)
    print(type(year),type(month),type(day))
    return HttpResponse('special_case_%s_%s_%s'%(year,month,day))

def test(request):
    return HttpResponse(reverse('app01:test'))  #反向解析的test的名称空间为app01

def detail_view(request,article_id):
    return HttpResponse('detail_view--------%s'%article_id)

def edit_view(request,article_id):
    return HttpResponse('edit_view--------%s'%article_id)

def delete_view(request,article_id):
    return HttpResponse('delete_view--------%s'%article_id)

def check_view(request,article_id):
    return HttpResponse('check_view--------%s'%article_id)