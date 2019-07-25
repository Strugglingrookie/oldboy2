"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('favicon.ico/', views.favicon),
    # path('login/', views.login),
    # path('timer/', views.timer),
    # path('regist/', views.regist),

    # 路由配置：路径--------->视图函数
    re_path(r'^articles/2019/$',views.special_case_2019),
    re_path(r'^articles/([0-9]{4})/$',views.year_archive),  # 正则分组匹配后会将分组匹配值作为传参调用视图函数
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),  # 这里有三个传参 request,year,month
    # 有名分组，就是关键字传参 固定写法  ?P<name>  等于是 year=2019,month=2,day=5
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$',views.day_archive),

    # 路由分发  app01开头的路径，指定到app01.urls文件，由它去分发
    re_path(r'^app01/',include('app01.urls')),

]
