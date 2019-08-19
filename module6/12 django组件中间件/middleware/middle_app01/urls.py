from django.urls import path
from middle_app01 import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('secret/', views.secret),
]
