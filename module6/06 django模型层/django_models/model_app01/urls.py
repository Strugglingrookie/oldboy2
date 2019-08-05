from django.urls import path, re_path
from model_app01 import views

urlpatterns = [
    re_path(r'^index/', views.index),
    re_path(r'^login/', views.login, name='log'),
    re_path(r'^regist/', views.regist, name='reg'),
    path('book/', views.book),
    path('book_add/', views.book_add, name = 'add'),
    path('book_select/', views.book_select, name = 'select'),
    path('book_update/', views.book_update, name = 'update'),
    path('book_delete/', views.book_delete, name = 'delete'),
]
