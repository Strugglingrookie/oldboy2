from django.urls import path, re_path
from cs_app01 import views

urlpatterns = [
    path('index/', views.index),
    path('cookie/', views.cookie),
    path('session/', views.session),
    path('logout/', views.logout),
]
