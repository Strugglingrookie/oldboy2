from django.urls import path
from forms_app01 import views

urlpatterns = [
    path('simple_forms/', views.simple_forms),
    path('multi_forms/', views.multi_forms),
    path('gouzi/', views.gouzi),
]
