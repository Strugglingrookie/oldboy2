# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 20:01
# @Author  : Xiao

from django.urls import path,re_path
from app02 import views

urlpatterns = [
    re_path('test',views.test,name="index")
]