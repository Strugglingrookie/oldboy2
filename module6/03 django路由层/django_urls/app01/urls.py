from django.urls import path,re_path,register_converter
from app01 import converters,views


#  注册自己写的转换器
register_converter(converters.FullYearDigits, 'my_year')

urlpatterns = [
    re_path('index1/', views.index1),
    path('index2/', views.index2),
    #反向解析 name='log',模板html {% url ''log %}根据反向解析后 得到结果为 login/
    # <form action="{% url 'app01:log' %}" method="post"></form> ---》 <form action="login/" method="post"></form>
    path('login/', views.login, name='log'),
    path('timer/', views.timer, name='tim'),
    path('regist/', views.regist, name='reg'),
    path('test/', views.test, name='test'),

    # 路由配置：路径--------->视图函数
    re_path(r'^articles/2019/$',views.special_case_2019),
    re_path(r'^articles/([0-9]{4})/$',views.year_archive,name='achive'),  # 有圆括弧，正则分组匹配后会将分组匹配值作为传参调用视图函数
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),  # 这里有三个传参 request,year,month

    # 有名分组，就是关键字传参 固定写法  ?P<name>  等于是 year=2019,month=2,day=5
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$',views.day_archive),

    # path 转化，以下的urls存在俩问题：1.传参都是str，但是视图函数其实想得到的是int；2.正则表达式[a-zA-Z0-9]+重复写了三次，后期维护麻烦
    # re_path('^article/(?P<year>[0-9]{4})/$', views.year_archive),
    # re_path('^article/(?P<article_id>[a-zA-Z0-9]+)/detail/$', views.detail_view),
    # re_path('^article/(?P<article_id>[a-zA-Z0-9]+)/edit/$', views.edit_view),
    # re_path('^article/(?P<article_id>[a-zA-Z0-9]+)/delete/$', views.delete_view),

    # 使用尖括号(<>)从url中捕获值，转换字符类型后再传给视图函数 注意不能用正则表达是了，而且得用回path   (?P<article_id>[a-zA-Z0-9]+)
    path('article/<int:year>/', views.year_archive),
    path('article/<int:year>/<int:month>/', views.month_archive),
    path('article/<int:year>/<int:month>/<int:day>', views.day_archive),  # int,匹配正整数，包含0。
    path('article/<str:article_id>/detail/', views.detail_view),  # str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
    path('article/<uuid:article_id>/edit/', views.edit_view),  # slug,匹配字母、数字以及横杠、下划线组成的字符串
    path('article/<slug:article_id>/delete/', views.delete_view),  # uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00
    path('article/<path:article_id>/check/', views.check_view),  # path,匹配任何非空字符串，包含了路径分隔符

    # 自己写的转换器
    path('my_article/<my_year:year>/', views.year_archive),
]
