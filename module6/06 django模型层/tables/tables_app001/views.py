from django.shortcuts import render, HttpResponse
from tables_app001.models import *

# Create your views here.


def add(request):

    ###################    单表插入记录   ####################
    Publish.objects.create(name='人民出版社', city='北京', email='qwe@qq.com')
    Publish.objects.create(name='湖南出版社', city='湖南', email='hn@qq.com')
    Publish.objects.create(name='深圳出版社', city='深圳', email='sz@qq.com')
    AuthorDetail.objects.create(age=18, addr='湖南', phone='13537730001')
    AuthorDetail.objects.create(age=28,  addr='湖南', phone='13537730002')
    AuthorDetail.objects.create(age=38,  addr='深圳', phone='13537730003')

    ##################    一对一插入记录   ####################
    detail_obj1 = AuthorDetail.objects.filter(id=1).first()
    detail_obj2 = AuthorDetail.objects.filter(id=2).first()
    detail_obj3 = AuthorDetail.objects.filter(id=3).first()
    Author.objects.create(name='杨一', authorDetail_id=detail_obj1.id)
    Author.objects.create(name='杨二', authorDetail=detail_obj2)
    Author.objects.create(name='杨三', authorDetail=detail_obj3)

    ##################    一对一插入记录   ####################
    publish_obj = Publish.objects.filter(id=1).first()
    book_obj1 = Books.objects.create(title='盘龙', price=16, pub_date='2018-12-12', publish=publish_obj)
    book_obj2 = Books.objects.create(title='星辰变', price=20, pub_date='2017-12-12', publish=publish_obj)


    ##################    多对多插入记录 add 方法  ####################
    book_obj1 = Books.objects.filter(id=1).first()
    book_obj2 = Books.objects.filter(id=2).first()

    author_obj1 = Author.objects.filter(name='杨一').first()
    author_obj2 = Author.objects.filter(name='杨二').first()
    author_obj3 = Author.objects.filter(name='杨三').first()

    book_obj1.authors.add(author_obj1, author_obj2, author_obj3)
    # book_obj2.authors.add(1)
    book_obj2.authors.add(*[1,4])


    ##################    解除多对多的关系   ####################
    # book_obj1.authors.remove(1)
    # book_obj1.authors.remove(*[4,])
    # book_obj1.authors.remove(author_obj3)


    return HttpResponse('OJBK!')


def query_son(request):
    """
    跨表查询:
       1 基于对象查询
       2 基于双下划线查询
       3 聚合和分组查询
       4 F 与 Q查询
    """
    # -------------------------基于对象的跨表查询(子查询)-----------------------
    # 一对多查询的正向查询 : 查询盘龙这本书的出版社的名字
    res = Books.objects.filter(title='盘龙').first().publish.name
    # 一对多查询的反向查询 : 查询人民出版社出版过的书籍名称
    res = Publish.objects.filter(name='人民出版社').first().books_set.all().values('title')
    # 多对多查询的正向查询 : 查询星辰变这本书的所有作者的名字
    res = Books.objects.filter(title='星辰变').first().authors.all().values('name')
    # 多对多查询的反向查询 : 查询杨一出版过的所有书籍名称
    res = Author.objects.filter(name='杨一').first().books_set.all().values('title')
    # 一对一查询的正向查询 : 查询杨二的手机号
    res = Author.objects.filter(name='杨二').first().authorDetail.phone
    # 一对一查询的反向查询 : 查询手机号为0001尾号的作者的名字
    res = AuthorDetail.objects.filter(phone__endswith='0001').first().author.name


    # -------------------------基于双下划线的跨表查询(join查询)-----------------------
    '''
        正向查询按字段,反向查询按表名小写用来告诉ORM引擎join哪张表
    '''
    # 一对多查询的正向查询 : 查询盘龙这本书的出版社的名字
    res = Books.objects.filter(title='盘龙').values('publish__name')
    # ----->  <QuerySet [{'publish__name': '人民出版社'}]>

    # 一对多查询的反向查询 : 查询人民出版社出版过的书籍名称
    res = Publish.objects.values('name').filter(books__title='盘龙')
    res = Publish.objects.filter(books__title='盘龙').values('name')  # 都可以
    # -----> <QuerySet [{'name': '人民出版社'}]>

    # 多对多查询的正向查询 : 查询星辰变这本书的所有作者的名字
    res = Books.objects.filter(title='星辰变').values('authors__name')
    # -----> <QuerySet [{'authors__name': '杨一'}, {'authors__name': '杨二'}]>

    # 多对多查询的反向查询 : 查询杨一出版过的所有书籍名称
    res = Author.objects.filter(books__title='星辰变').values('name')
    res = Author.objects.values('name').filter(books__title='星辰变')  # 都可以
    # -----> <QuerySet [{'name': '杨一'}, {'name': '杨二'}]>

    # 一对一查询的正向查询 : 查询杨二的手机号
    res = Author.objects.filter(name='杨二').values('authorDetail__phone')
    # -----> <QuerySet [{'authorDetail__phone': 13537730002}]>

    # 一对一查询的反向查询 : 查询手机号为0001尾号的作者的名字
    res = AuthorDetail.objects.filter(phone__endswith='0001').values('author__name')
    # ----->  <QuerySet [{'author__name': '杨一'}]>

    # 练习: 查询人民出版社出版过的所有书籍的名字以及作者的姓名
    res = Books.objects.filter(publish__name='人民出版社').values('title', 'authors__name')

    # 练习: 手机号以0001结尾的作者出版过的所有书籍名称以及出版社名称
    res = Author.objects.filter(authorDetail__phone__endswith='0001').values('books__title', 'books__publish__name')
    # < QuerySet[{'books__title': '星辰变', 'books__publish__name': '人民出版社'}, {'books__title': '盘龙','books__publish__name': '人民出版社'}] >


    # --------------  聚合 aggregate:返回值是一个字典,不再是queryset  --------------
    # 查询所有书籍的平均价格
    from django.db.models import Avg, Max, Min, Count, Sum
    res = Books.objects.all().aggregate(Avg('price'))
    # --------> {'price__avg': Decimal('18.000000')}
    res = Books.objects.all().aggregate(avgPrice=Avg('price')) # 取别名
    # --------> {'avgPrice': Decimal('18.000000')}

    # 查询价格最高的书籍
    res = Books.objects.all().aggregate(Max('price'))
    # -------->  {'price__max': Decimal('20.00')}


    # ---------------  分组查询 annotate ,返回值依然是queryset  ---------------

    # ------------------------->单表分组查询:
    # Employee.objects.create(name='steven', age=18, sal=1000, dep='销售部')
    # Employee.objects.create(name='mike', age=28, sal=2000, dep='销售部')
    # Employee.objects.create(name='ben', age=38, sal=1000, dep='销售部')
    # Employee.objects.create(name='jack', age=48, sal=8000, dep='IT部')
    # Employee.objects.create(name='Mary', age=18, sal=3000, dep='IT部')
    # 单表分组查询的ORM语法: 单表模型.objects.values("group by的字段").annotate(聚合函数("统计字段"))

    # 查询每一个部门的名称以及员工的平均薪水
    res = Employee.objects.values('dep').annotate(Avg('sal'))
    # <QuerySet [{'dep': '销售部', 'sal__avg': Decimal('1333.33333')}, {'dep': 'IT部', 'sal__avg': Decimal('5500.00000')}]>

    # 查询每一个部门的名称以及员工数
    res = Employee.objects.values('dep').annotate(Count('id'))
    #  <QuerySet [{'dep': '销售部', 'id__count': 3}, {'dep': 'IT部', 'id__count': 2}]>

    # ------------------------->多表分组查询:
    # Books.objects.create(title='吞噬星空', price=30, pub_date='2017-12-12', publish_id=2)
    # Books.objects.create(title='蛮荒记', price=40, pub_date='2017-12-12', publish_id=2)

    ## 示例1 查询每一个出版社的名称以及出版的书籍个数
    res = Books.objects.values('publish__name').annotate(c=Count('id'))
    res = Books.objects.values('publish__id').annotate(c=Count('id')).values('publish__name', 'c')
    res = Publish.objects.values('id').annotate(c=Count('books__id')).values('name', 'c')
    # <QuerySet [{'publish__name': '人民出版社', 'c': 2}, {'publish__name': '湖南出版社', 'c': 2}]>

    ## 示例2 查询每一个作者的名字以及出版过的书籍的最高价格
    res = Author.objects.values('pk').annotate(Max('books__price'))
    res = Author.objects.values('pk').annotate(max=Max('books__price')).values('name', 'max')
    # <QuerySet [{'name': '杨一', 'max': Decimal('20.00')}, {'name': '杨二', 'max': Decimal('20.00')}, {'name': '杨三', 'max': Decimal('16.00')}]>

    # 总结 跨表的分组查询的模型:
    # 每一个后表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段))
    # 示例3 查询每一个书籍的名称以及对应的作者个数
    res = Books.objects.values('pk').annotate(c=Count('authors__id')).values('title','c')
    # < QuerySet[{'title': '盘龙', 'c': 3}, {'title': '星辰变', 'c': 2}, {'title': '吞噬星空', 'c': 0}, {'title': '蛮荒记', 'c': 0}] >

    #################### 跨表分组查询的另一种玩法  ####################
    # 示例1 查询每一个出版社的名称以及出版的书籍个数
    res = Publish.objects.values('pk').annotate(c=Count('books__id')).values('name','c')
    res = Publish.objects.all().annotate(c=Count('books__id')).values('name','c')
    res = Publish.objects.annotate(c=Count('books__id')).values('name','c')
    # < QuerySet[{'name': '人民出版社', 'c': 2}, {'name': '湖南出版社', 'c': 2}, {'name': '深圳出版社', 'c': 0}] >

    ##################### 练习   ####################
    # 统计每一本以'盘'开头的书籍的作者个数：
    res = Books.objects.filter(title__startswith='盘').annotate(c=Count('authors__id')).values('title','c')
    # <QuerySet [{'title': '盘龙', 'c': 3}]>

    # 统计不止一个作者的图书
    res = Books.objects.annotate(c=Count('authors__id')).filter(c__gt=1).values('title','c')
    # < QuerySet[{'title': '盘龙', 'c': 3}, {'title': '星辰变', 'c': 2}] >

    # 根据一本图书作者数量的多少对查询集QuerySet进行排序
    res = Books.objects.annotate(c=Count('authors__id')).values('title', 'c').order_by('c')
    # < QuerySet[{'title': '吞噬星空', 'c': 0}, {'title': '蛮荒记', 'c': 0}, {'title': '星辰变', 'c': 2}, {'title': '盘龙', 'c': 3}] >

    # 查询各个作者出的书的总价格:
    res = Author.objects.annotate(total=Sum('books__price')).values('name','total')
    # <QuerySet [{'name': '杨一', 'total': Decimal('36.00')}, {'name': '杨二', 'total': Decimal('36.00')}, {'name': '杨三', 'total': Decimal('16.00')}]>

    # 总结 跨表的分组查询的模型:
    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    # 每一个后的表模型.objects.annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")


    # ###############  F 查询条件里包含字段  ###############
    # 查询评论数大于阅读数的书记
    from django.db.models import F
    res = Books.objects.filter(read_num__gt=F('comment_num'))
    # < QuerySet[ < Books: 盘龙 >, < Books: 星辰变 >] >

    # 所有书的价格上调 10%
    res = Books.objects.update(price=F('price')*1.1)


    # ###############  Q 查询条件关系  与或非 ###############
    from django.db.models import Q
    # 与 &
    res = Books.objects.filter(price__lt=3, read_num__gt=100)
    res = Books.objects.filter(Q(price__lt=3)&Q(read_num__lt=100))

    # 或 |
    res = Books.objects.filter(Q(price__lt=3)|Q(read_num__lt=100))

    # 非 ~
    res = Books.objects.filter(~Q(price__lt=3))


    print(res)
    return HttpResponse('OJBK!')


