from django.shortcuts import render, redirect
from book_app01.models import *


# Create your views here.


def book(request):
    method = request.method
    req = request.POST if request.POST else request.GET
    try:
        title = req.get('title') if req.get('title') else ''
    except exception as e:
        title = ''
    book_list = Book.objects.filter(title__contains=title)

    return render(request, 'book.html', locals())


def add_book(request):
    method = request.method
    res = Publish.objects.all().exists()
    res_author = Author.objects.all().exists()
    if not res:
        Publish.objects.create(name='人民出版社', city='北京', email='123@qq.com')
        Publish.objects.create(name='南京出版社', city='南京', email='456@qq.com')
        Publish.objects.create(name='东京出版社', city='东京', email='789@qq.com')
    if not res_author:
        d1 = AuthorDetail.objects.create(age=18, addr='北京', phone=13537730001)
        d2 = AuthorDetail.objects.create(age=28, addr='北京', phone=13667730001)
        d3 = AuthorDetail.objects.create(age=38, addr='深圳', phone=13967730001)
        d2 = AuthorDetail.objects.filter(id=2).first()
        d3 = AuthorDetail.objects.filter(id=3).first()
        Author.objects.create(name='杨一', authorDetail_id=1)
        Author.objects.create(name='杨二', authorDetail_id=d2.id)
        Author.objects.create(name='杨三', authorDetail=d3)
    if method == 'POST':
        req = request.POST
        print('req---->', req)
        title = req.get('title').strip()
        price = req.get('price').strip()
        date = req.get('date').strip()
        publish_id = req.get('publish_id').strip()
        # get只能取到authors_id_list列表的最后一个值，getlist取整个authors_id_list列表
        authors_id_lis = req.getlist('authors_id_list')
        print('authors_id_lis------->', authors_id_lis)
        if title and price and date and publish_id and authors_id_lis:
            select_res = Book.objects.filter(title=title).exists()
            if not select_res:
                publish_obj = Publish.objects.filter(id=publish_id).first()
                # res = Book.objects.create(title=title, price=price, pub_date=date, publish=publish_obj)
                res = Book.objects.create(title=title, price=price, pub_date=date, publish_id=publish_id)
                res.authors.add(*authors_id_lis)
                return redirect('/app01/book')
            opt_res = '书籍【%s】已存在,请修改后提交！' % title
        else:
            opt_res = '输入不能为空,请修改后提交！'
    publish_obj = Publish.objects.all()
    author_obj = Author.objects.all()
    return render(request, 'addbook.html', locals())


def update_book(request, num):
    book_obj = Book.objects.filter(id=num).first()
    publish_obj = Publish.objects.all()
    author_obj = Author.objects.all()
    if book_obj:
        method = request.method
        if method == 'POST':
            req = request.POST
            print('req---->', req)
            title = req.get('title').strip()
            price = req.get('price').strip()
            date = req.get('date').strip()
            publish_id = req.get('publish_id').strip()
            # get只能取到authors_id_list列表的最后一个值，getlist取整个authors_id_list列表
            authors_id_lis = req.getlist('authors_id_list')
            print('authors_id_lis------->', authors_id_lis)
            if title and price and date and publish_id and authors_id_lis:
                select_res = Book.objects.exclude(id=num).filter(title=title)
                if not select_res:
                    Book.objects.filter(id=num).update(title=title, price=price, pub_date=date, publish_id=publish_id)
                    # book_obj.authors.clear()
                    # book_obj.authors.add(*authors_id_lis)
                    book_obj.authors.set(authors_id_lis)  # 该方法等同于上面两个步骤
                    return redirect('/app01/book')
                opt_res = '书籍【%s】已存在,请修改后提交！' % select_res[0].title
            else:
                opt_res = '输入不能为空,请修改后提交！'
        return render(request, 'updatebook.html', locals())
    return redirect('/app01/book')


def delete_book(request, num=None):
    book_obj = Book.objects.filter(id=num).first()
    if book_obj:
        book_obj.authors.clear()
        book_obj.delete()
    return redirect('/app01/book')
