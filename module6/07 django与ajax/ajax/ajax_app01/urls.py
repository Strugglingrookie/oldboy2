from django.urls import path, re_path
from ajax_app01 import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('regist/', views.regist),
    path('check/', views.check),
    path('file/', views.file),
]
