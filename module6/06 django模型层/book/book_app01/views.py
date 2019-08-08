from django.shortcuts import render,redirect
from book_app01.models import Book

# Create your views here.


def book(request):
    method = request.method
    req = request.POST if request.POST else request.GET
    try:
        title = req.get('title') if req.get('title') else ''
    except:
        title = ''
    book_list = Book.objects.filter(title__contains=title)
    '''
        # 1 查询人民出版社出版过的价格大于200的书籍
        res = Book.objects.filter(publish="人民出版社",price__gt=200)
        # 2 查询2017年8月出版的所有以py开头的书籍名称
        res = Book.objects.filter(pub_date__contains="2017-08",title__startswith='py').values('title')
        # 3 查询价格为50,100或者150的所有书籍名称及其出版社名
        res = Book.objects.filter(price__in=[50,100,150]).values('title','publish')
        # 4 查询价格在100到200之间的所有书籍名称及其价格
        res = Book.objects.filter(price__range=[100,200]).values('title','price')
        # 5 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
        res = Book.objects.filter(publish="人民出版社").values('price').distinct().order_by('-price')
        print('res----------->',res)
    '''
    return  render(request, 'book.html',locals())


def add_book(request):
    method = request.method
    if method == 'POST':
        req = request.POST
        title = req['title'].strip()
        price = req['price'].strip()
        date = req['date'].strip()
        publish = req['publish'].strip()
        if title and price and date and publish:
            selct_res = Book.objects.filter(title=title)
            if not selct_res:
                Book.objects.create(title=title,price=price,pub_date=date,publish=publish)
                return redirect('/app01/book')
            opt_res = '书籍【%s】已存在,请修改后提交！'%title
        else:
            opt_res = '输入不能为空,请修改后提交！'
    return render(request, 'addbook.html', locals())


def update_book(request, num):
    select_res = Book.objects.filter(id=num)
    if select_res:
        method = request.method
        book_obj = select_res[0]
        if method == 'POST':
            req = request.POST
            title = req['title'].strip()
            price = req['price'].strip()
            date = req['date'].strip()
            publish = req['publish'].strip()
            if title and price and date and publish:
                selct_res = Book.objects.exclude(id=num).filter(title=title)
                if not selct_res:
                    Book.objects.filter(id=num).update(title=title, price=price, pub_date=date, publish=publish)
                    return redirect('/app01/book')
                opt_res = '书籍【%s】已存在,请修改后提交！' % selct_res[0].title
            else:
                opt_res = '输入不能为空,请修改后提交！'
        return render(request, 'updatebook.html', locals())
    return redirect('/app01/book')

def delete_book(request, num=None):
    select_res = Book.objects.filter(id=num)
    if select_res:
        Book.objects.filter(id=num).delete()
    return redirect('/app01/book')

