from django.urls import path, re_path
from app04 import  views

urlpatterns = [
    re_path(r'^index/', views.index),
]
