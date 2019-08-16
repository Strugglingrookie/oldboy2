from django.urls import path, re_path
from auth_app01 import views


urlpatterns = [
    path('index/', views.index),
    path('regist/', views.regist),
    path('login/', views.mylogin),
    path('logout/', views.logout),
]