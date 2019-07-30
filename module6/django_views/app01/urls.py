# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2019/7/28

from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index', views.index, name='index'),
    re_path('login', views.login, name='log'),
]
