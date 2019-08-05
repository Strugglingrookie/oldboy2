from django.urls import path, re_path
from model_app01 import views

urlpatterns = [
    re_path(r'^index/', views.index),
    re_path(r'^login/', views.login, name='log'),
    re_path(r'^regist/', views.regist, name='reg'),
]
