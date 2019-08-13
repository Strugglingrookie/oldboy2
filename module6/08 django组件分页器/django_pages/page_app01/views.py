from django.shortcuts import render,HttpResponse
from page_app01.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

# Create your views here.


def pages(request):
    # 初始化数据
    '''
    booklist = []
    for i in range(1,101):
        booklist.append(Book(title="python_%d"%i,price=i+i+i))
    Book.objects.bulk_create(booklist)  # 批量插入数据    bulk_create(数据库对象实例化列表)
    '''
    book_objs = Book.objects.all()
    my_paginator = Paginator(book_objs, 3)  #  按每页3条进行分页
    print(my_paginator.count)    # 总条数 100
    print(my_paginator.num_pages)  # 总页数  34
    print(my_paginator.page_range) # 页码列表  range(1, 35)

    page1 = my_paginator.page(1)  # 第一页的 page 对象
    # 第一页的所有对象 <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>
    print(page1.object_list)
    for page in page1:  # 打印page对象里的所有书籍对象
        print(page)
    '''
    Book object (1)
    Book object (2)
    Book object (3)
    '''
    page2 = my_paginator.page(2)  # 第二页的 page 对象
    print(page2.has_next())  # 是否有下一页
    print(page2.next_page_number())  # 下一页的页码
    print(page2.has_previous())  # 是否有上一页
    print(page2.previous_page_number()) #上一页的页码

    # 当页码下没有记录时，会报错 EmptyPage  django.core.paginator.EmptyPage: That page contains no results
    # page100 = my_paginator.page(100)
    # 当页码不是数字时，会报错 PageNotAnInteger django.core.paginator.PageNotAnInteger: That page number is not an integer
    # page1_ab = my_paginator.page('ab')
    # 所以在用的时候需要try一下来捕捉这些异常

    # 响应页面的代码  只用到了current_page_num 和 current_page
    paginator = Paginator(book_objs, 6)
    current_page_num = int(request.GET.get('page', 1))
    # 当页码大于总页数时  当前页面取总页数
    current_page_num = current_page_num if current_page_num<=paginator.num_pages else paginator.num_pages

    max_page = 8  # 显示的最大页数
    if paginator.num_pages > max_page:
        middle = max_page / 2
        if current_page_num <= middle:
            page_lis = range(1, max_page+1)
        elif current_page_num+middle > paginator.num_pages:
            page_lis = range(paginator.num_pages - max_page + 1, paginator.num_pages+1)
        else:
            page_lis = range(current_page_num-math.floor(middle), current_page_num+math.ceil(middle))
    else:
        page_lis = paginator.page_range

    try:
        current_page = paginator.page(current_page_num)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())