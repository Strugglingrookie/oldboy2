from views_app01 import views
from django.urls import path, re_path

urlpatterns = [
    path('index/', views.index),
    re_path('^login/', views.login, name='log'),
    re_path('^regist/', views.regist, name='reg'),
]
