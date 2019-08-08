from django.urls import path,re_path,include
from book_app01 import views

urlpatterns = [
    path('book/', views.book),
    path('book/add', views.add_book),
    re_path(r'book/(\d+)/update', views.update_book),
    re_path(r'book/(\d+)/delete', views.delete_book),
]
