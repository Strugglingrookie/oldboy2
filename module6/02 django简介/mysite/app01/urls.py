# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 21:02
# @Author  : Xiao

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
    path('login/', views.login, name='log'),  #反向解析 name='log'
    path('timer/', views.timer,name='tim'),
    path('regist/', views.regist),
    path('regist/', views.regist),
    re_path(r'^articles/([0-9]{4})/$', views.special_case_2019,name='achive'),
]
