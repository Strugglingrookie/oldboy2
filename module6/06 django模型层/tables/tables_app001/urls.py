# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2019/8/10


from django.urls import path
from tables_app001 import views


urlpatterns = [
    path('add', views.add),
    path('query', views.query),

]