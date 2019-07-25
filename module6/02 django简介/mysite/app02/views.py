from django.shortcuts import render,HttpResponse
from django.urls import reverse

# Create your views here.


def test(request):
    return HttpResponse(reverse('app02:index')) #反向解析的index的名称空间为app02