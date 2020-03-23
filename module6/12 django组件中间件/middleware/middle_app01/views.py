from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from middle_app01.myforms import LoginForm


# Create your views here.


def index(request):
    print('----------------------> 视图函数给出的真实响应')
    return render(request, 'index.html')

    # 视图函数出错 测试 process_exception
    # return render(request, 'indexasdfadf.html')


def secret(request):
    return render(request, 'secret.html', locals())


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('name')
            pwd = form.cleaned_data.get('pwd')
            user = auth.authenticate(username=username, password=pwd)
            if user:
                auth.login(request, user)
                next_url = request.GET.get('next', '/app01/index')
                return redirect(next_url)
            else:
                error = '用户名或密码错误！'
                return render(request, 'login.html', locals())
        else:
            print(form.cleaned_data)
            print(form.errors)
            return render(request, 'login.html', locals())
    else:
        form = LoginForm()
        return render(request, 'login.html', locals())
