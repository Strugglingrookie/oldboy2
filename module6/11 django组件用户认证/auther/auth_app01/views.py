from django.shortcuts import render, redirect, HttpResponse
from auth_app01.myforms import Form, LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from auther import settings


def index(request):
    if not request.user.is_authenticated:
        print(request.user)
    else:
        print('no user')
    return render(request, 'index.html')


def regist(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            user = None

            # 注意创建用户的时候要用create_user方法  用create的话不会对密码进行加密
            res = User.objects.create_user(username=username, email=email, password=pwd)

            # 注册完成之后 调用 authenticate() 进行认证得到一个  User  对象
            if res:
                user = authenticate(username=username, password=pwd)

            # login函数接受一个HttpRequest对象，以及一个认证了的User对象
            # login函数使用django的session框架给某个已认证的用户附加上sessionid等信息
            # 链接跳转到index后 会带上sessionid信息，且 request.user 定义成了一个全局变量任何地方都可以用，包括模板
            if user:
                login(request, user)

            return redirect('/app01/index/')
        else:
            print(form.cleaned_data)
            print(form.errors)
        return render(request, 'regist.html', locals())
    else:
        form = Form()
        return render(request, 'regist.html', locals())


def mylogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('name')
            pwd = form.cleaned_data.get('pwd')
            user = auth.authenticate(username=username, password=pwd)
            if user:
                login(request, user)
                # next_url 用户请求可能是其他请求重定向过来的，登录完成后，根据next值返回到相应的url
                next_url = request.GET.get('next', '/app01/index')
                return redirect(next_url)
            else:
                error = '用户名或密码错误！'
                return render(request, 'login.html', locals())
    else:
        form = LoginForm()
        return render(request, 'login.html', locals())


def mylogout(request):
    # 接受一个HttpRequest对象，无返回值。调用时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错。
    logout(request)
    return redirect('/app01/index/')


# 上面通过auth已经实现了简单的登录注册以及首页之间的跳转 但是实际场景存在这样的情况：
# 1  用户登陆后才能访问某些页面，
# 2  如果用户没有登录就访问该页面的话直接跳到登录页面
# 3  用户在跳转的登陆界面中完成登陆后，自动访问跳转到之前访问的地址

# 方式一
def secret(request):
    if request.user.is_authenticated:
        my_secret = 'secret'
        return render(request, 'secret.html', locals())
    else:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))


# 方式二  login_required 装饰器
# 若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' (这个值可以在settings文件中通过LOGIN_URL进行修改)。
# 并传递  当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。
@login_required
def mimi(request):
    my_secret = 'mimi'
    return render(request, 'secret.html', locals())


# 修改密码
@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                return redirect("/app01/login/")
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'password.html', content)
