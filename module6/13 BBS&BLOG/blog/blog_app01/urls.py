from django.urls import path
from blog_app01 import views


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('regist/', views.regist),
    path('valid_img/', views.valid_img),
]