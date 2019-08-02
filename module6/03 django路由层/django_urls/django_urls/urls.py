"""django_urls URL Configuration

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

urlpatterns = [
    # 路由分发  app01开头的路径，指定到app01.urls文件，由它去分发
    # re_path(r'^app01/',include('app01.urls')),
    re_path(r'^app01/',include(('app01.urls','app01'))),  #('app01.urls','app01')中 app01是名称空间
    re_path(r'^app02/',include(('app02.urls','app02'))),  # 避免不同应用中通用的反向解析路径覆盖 HTML模板在用的时候指定名称空间即可
]
