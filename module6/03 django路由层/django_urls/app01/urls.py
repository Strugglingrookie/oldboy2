from django.urls import path,re_path
from app01 import views

urlpatterns = [
    re_path('index1/', views.index1),
    path('index2/', views.index2),
    path('login/', views.login, name='log'),  #反向解析 name='log'
    path('timer/', views.timer, name='tim'),
    path('regist/', views.regist,name='reg'),

    # 路由配置：路径--------->视图函数
    # re_path(r'^articles/2019/$',views.special_case_2019),
    # re_path(r'^articles/([0-9]{4})/$',views.year_archive),  # 有圆括弧，正则分组匹配后会将分组匹配值作为传参调用视图函数
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),  # 这里有三个传参 request,year,month
    #
    # # 有名分组，就是关键字传参 固定写法  ?P<name>  等于是 year=2019,month=2,day=5
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$',views.day_archive),
]
