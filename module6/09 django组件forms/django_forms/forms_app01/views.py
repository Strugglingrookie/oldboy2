from django.shortcuts import render
from django.forms import widgets
from django import forms

# Create your views here.


# 简单的forms校验
def index(request):
    class UserForms(forms.Form):  # 创建forms校验对象
        name = forms.CharField(min_length=4, max_length=8) # min_length 校验规则
        pwd = forms.CharField(min_length=4)
        r_pwd = forms.CharField(min_length=4)
        email = forms.EmailField()
        tel = forms.CharField(min_length=11, max_length=11)
    if request.method == 'POST':
        res = UserForms(request.POST)
        print(res)
        print(res.is_valid())  # 规则是否校验通过 全部通过为True
        if res.is_valid():
            # cleaned_data  校验通过的所有字段，比如输入100个字段，但是这里只校验4个字段，得到的就是过滤后的4个字段
            print(res.cleaned_data)
        else:
            print(res.cleaned_data)  # 通过的部分字段，哪个字段校验通过就往这里加
            print(res.errors)  # ErrorDict : {"校验错误的字段":["错误信息",]} 不通过的往这里加，是一个字典
            print(res.errors.get('email'))  # ErrorList ["错误信息",]  是一个列表
            print(res.errors.get('email')[0]) # 取第一个错误信息，一般都是取第一个错误信息返回给前端
    return render(request, 'index.html')