from django.shortcuts import render, HttpResponse
from django.urls import reverse
from app01.tools import Mysql


# Create your views here.

def index(request):
    print(request.method)
    print(request.path)
    print(request.get_full_path())
    print(request.GET)
    print(request.POST)
    print(request.body)
    print(request.FILES)
    print(request.encoding)
    print(request.META)
    print(request.COOKIES)
    print(request.session)
    return render(request, 'index.html')


def login(request):
    log_url = reverse('app01:log')  # 另一种反向解析
    # time_url = reverse('tim')
    # articles_url = reverse('achive', args=(2019,))  # 当路径是一个正则表达式的时候，需要传参，有几个参数就传几个，否则会报错
    print(log_url)
    # print(time_url)
    # print(articles_url)
    method = request.method
    print(method)
    if method.lower() == 'post':
        req_data = request.POST
        print(req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        mysql_check = Mysql('localhost', 3306, 'root', '123456', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        print('res', res)
        if res and isinstance(res, list):
            return render(request, 'index.html')
        else:
            return HttpResponse('username or password is wrong!')
    else:
        print(request.GET)
        # 反向解析在这一步做的，render会根据urls控制器传的name进行解析{% url 'log' %} ---> /app01/login/
        return render(request, 'login.html')

