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
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('favicon.ico/', views.favicon),
    path('login/', views.login),
    path('timer/', views.timer),
    path('regist/', views.regist),

    # 路由配置：路径--------->视图函数
    re_path(r'^articles/2019/$',views.special_case_2019),
    re_path(r'^articles/([0-9]{4})/$',views.year_archive),  # 正则分组匹配后会将分组匹配值作为传参调用视图函数
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),  # 这里有三个传参 request,year,month
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$',views.day_archive),  # 这里有四个传参 request,year,month,day
]
