from django.shortcuts import render
from django.forms import widgets
from django import forms

# Create your views here.


# 简单的forms校验
def simple_forms(request):
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
    return render(request, 'simple_forms.html')


# forms校验 前端渲染  为了避免前端和后端字段不一致，可以直接由后端渲染前端页面
def multi_forms(request):
    wdg1 = widgets.TextInput(attrs={'class':'form-control'})  # 可以给input标签加任何属性
    wdg2 = widgets.PasswordInput(attrs={'class':'form-control'})
    class UserForms(forms.Form):  # 创建forms校验对象
        name = forms.CharField(min_length=4, max_length=8,widget=wdg1, label='姓名') # min_length 校验规则
        pwd = forms.CharField(min_length=4,widget=wdg2, label='密码')
        r_pwd = forms.CharField(min_length=4,widget=wdg2, label='确认密码')
        email = forms.EmailField(widget=wdg1, label='邮箱')
        tel = forms.CharField(min_length=11, max_length=11,widget=wdg1, label='手机号')
    myform = UserForms()  #  实例传给前端进行渲染
    if request.method == 'POST':
        # 将这个传给前端，可以渲染错误提示信息  myform.tel.errors.0 拿到相应字段的错误信息进行渲染
        # 而且将用户输入的信息重传给用户  避免待提交的数据刷新
        myform = UserForms(request.POST)
        print(myform)
        print(myform.is_valid())  # 规则是否校验通过 全部通过为True
        if myform.is_valid():
            # cleaned_data  校验通过的所有字段，比如输入100个字段，但是这里只校验4个字段，得到的就是过滤后的4个字段
            print(myform.cleaned_data)
        else:
            print(myform.cleaned_data)  # 通过的部分字段，哪个字段校验通过就往这里加
            print(myform.errors)  # ErrorDict : {"校验错误的字段":["错误信息",]} 不通过的往这里加，是一个字典
            print(myform.errors.get('email'))  # ErrorList ["错误信息",]  是一个列表
            print(myform.errors.get('email')[0]) # 取第一个错误信息，一般都是取第一个错误信息返回给前端
            return render(request, 'multi_forms.html', locals())
    return render(request, 'multi_forms.html',locals())


# 局部钩子与全局钩子
def gouzi(request):
    # 通models，可以将forms放在一个文件，然后导入
    from forms_app01.myforms import UserForms
    myform = UserForms()
    if request.method == 'POST':
        myform = UserForms(request.POST)
        if myform.is_valid():
            print(myform.cleaned_data)
        else:
            clean_error = myform.errors.get("__all__")
        return render(request, 'gouzi.html', locals())
    return render(request, 'gouzi.html',locals())
