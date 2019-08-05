from django.shortcuts import render,redirect,HttpResponse
from model_app01.tools import Mysql
from model_app01.models import Book

# Create your views here.


def output(lis):
    for i in lis:
        print(i.id, i.title, i.price)

def index(request):
    '''
    # ==================================  添加记录  ==================================
    # 添加表记录 方式一  先实例化，然后调用 save方法
    insert_opration = Book(title='python',state=1,pub_date='2012-01-01',price=23,publish='深圳出版社')
    insert_opration.save()
    # 添加表记录 方式二  Book.objects.create()  create返回值就是当前生成的对象纪录
    res = Book.objects.create(title="go",state=0,price=10,publish="北京出版社",pub_date="2014-12-12")
    print(res.title, res.state, res.price, res.publish, res.pub_date)
    # 插入一百条记录
    # for i in range(100):
    #     i = str(i)
    #     Book.objects.create(title="%s山药当归枸杞GO"%i, state=True, price=i, publish="北京%s号出版社"%i, pub_date="2019-01-12")


    # ==================================  查询记录  ==================================
    #(1) all()方法:   返回值一个queryset对象  查询所有结果
    sql_res =  Book.objects.all()
    print(sql_res) # [obj1,obj2,.....]
    for obj in sql_res:
        print(obj.title,obj.price)
    print(sql_res[5].price)

    # (2)first(),last() : 调用者:queryset对象  返回值:model对象
    book = Book.objects.all().first()
    book = Book.objects.all()[0]  # 等价于这个
    print(book,book.title)

    # (3) filter(**kwargs)  返回值:queryset对象  它包含了与所给筛选条件相匹配的对象
    sql_res = Book.objects.filter(price=80)
    output(sql_res)
    sql_res = Book.objects.filter(price__gt=77,price__lt=90,state=1)
    output(sql_res)

    # (4) get(**kwargs)  有且只有一个查询结果时才有意义  返回值:model对象
    #  返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
    book_obj=Book.objects.get(title="go")
    book_obj=Book.objects.get(price=100)
    print(book_obj.price)  # 当没有返回值的时候会报错

    # (5) exclude(**kwargs) != 返回值:queryset对象
    sql_res=Book.objects.exclude(title="go")
    output(sql_res)

    # (6) order_by(*field)   调用者: queryset对象   返回值:  queryset对象  对查询结果排序
    sql_res = Book.objects.all().order_by('price')
    sql_res = Book.objects.all().order_by('-id')  # - 代表倒序
    output(sql_res)

    # (7) count()   调用者: queryset对象   返回值: int  返回数据库中匹配查询(QuerySet)的对象数量
    res = Book.objects.all().count()
    res2 = Book.objects.filter(price__gt=88).count()
    print(res,res2)

    # (8) exists()  如果QuerySet包含数据，就返回True，否则返回False
    res = Book.objects.all().exists()
    res2 = Book.objects.filter(price__gt=10086).exists()
    print(res, res2)

    # (9) values(*field) 方法  调用者: queryset对象  返回值:queryset对象  需要的数据列
    # 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列  model的实例化对象，而是一个可迭代的字典序列
    sql_res = Book.objects.all().values('id','title','price')
    sql_res = Book.objects.filter(price=77).values('id','title','price')
    print(sql_res)  # QuerySet [{'title': '77山药当归枸杞GO', 'price': Decimal('77.00'), 'id': 80}]
    print(sql_res[0]['title'])  # 77山药当归枸杞GO

    # (10) values_list 方法  调用者: queryset对象  返回值:queryset对象
    # 它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
    sql_res = Book.objects.all().values_list('id', 'title', 'price')
    sql_res = Book.objects.filter(price=77).values_list('id', 'title', 'price')
    print(sql_res)  # [(80, '77山药当归枸杞GO', Decimal('77.00'))]
    print(sql_res[0][1])  # 77山药当归枸杞GO

    # 11 distinct 从返回结果中剔除重复纪录
    sql_res = Book.objects.all().count()
    sql_res2 = Book.objects.values('price').distinct().count()
    print(sql_res,sql_res2)

    # 点语法 可以一直点下去
    # Book.objects.all().filter().order_by().filter().reverse().first()


    # ==================================  模糊查询  ==================================
    #  __gt 大于    __gte 大于等于    __lt 小于    __lte 小于等于    __in 存在于一个list范围内
    # __startswith 以...开头  __istartswith 以...开头 忽略大小写  contains 包含 like '%aaa%'
    # __icontains 包含 忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains
    # __exact 精确等于 like 'aaa'__range 在...范围内   __year 日期字段的年份
    # __month 日期字段的月份   __day 日期字段的日  __isnull=True/False
    sql_res = Book.objects.filter(price__in=[100, 200, 300])
    sql_res = Book.objects.filter(price__gt=100)
    sql_res = Book.objects.filter(price__lt=100)
    sql_res = Book.objects.filter(price__range=[100, 200])
    sql_res = Book.objects.filter(title__contains="python")
    sql_res = Book.objects.filter(title__icontains="python")
    sql_res = Book.objects.filter(title__startswith="py")
    sql_res = Book.objects.filter(pub_date__year=2012)

    # ================================== 删除和修改 ===============================
    # delete: 调用者: queryset对象  model对象  但是如果没有查询到记录，delete时会报错
    sql_res=Book.objects.filter(price=2).delete()
    print(sql_res)
    Book.objects.filter(price=66).first().delete()

    # update :  调用者: queryset对象
    ret = Book.objects.filter(title="java").update(title="php")
'''
    return render(request,'index.html',locals())


def login(request):
    method = request.method
    if method.lower() == 'post':
        req_data = request.POST  # 一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。
        print('request.POST:\n',req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        if res and isinstance(res,list):
            return render(request, 'index.html')
        else:
            return HttpResponse('username or password is wrong!')
    else:
        print('request.GET:\n',request.GET)  # 一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象
        return render(request, 'login.html')


def regist(request):
    method = request.method
    if method.lower() == 'post':
        req_data = request.POST
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
            return redirect("/app01/index")  # redirect() 重定向  传递要重定向的一个硬编码的URL
            # return redirect("http://127.0.0.1:8080/app01/index/")  # 也可以是一个完整的URL
        return HttpResponse('username or password can not be empty !')
    return render(request,'register.html',{'word':'hello world!'})