from django.urls import path
from forms_app01 import views


urlpatterns = [
    path('index/',views.index)
]