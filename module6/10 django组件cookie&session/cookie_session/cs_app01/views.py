from django.shortcuts import render, HttpResponse, redirect
from cs_app01.myforms import Myform
from cs_app01.models import UserInfo
import datetime


def cookie(request):
    if request.method == 'POST':
        print(request.POST)
        form = Myform(request.POST)
        if form.is_valid():
            res = redirect('/app01/index')  # 设置响应对象，redirect和render的实质都是HttpResponse的类
            res.set_cookie('user', form.cleaned_data.get('name'))  # set_cookie是HttpResponsea的方法  设置cookie
            res.set_cookie('last_login_time', datetime.datetime.now())
            res.set_cookie('path_cookie', 'login_path',path='/app01/login')  # path 指定路径下有效
            res.set_cookie('max_age', '60',max_age=60)  # 只有max_age,  则按秒计算过期时间, 浏览器会存在本地缓存路径, 并自动删除过期cookie
            res.set_cookie('expires_time', '16:53:40',expires=20)  # expires 指定到生效的时间
            # 只有expires, 则按照时间字符串计算过期时间, 浏览器会存在本地缓存路径, 自动删除过期cookie
            # expires格式可以为:  1.时间格式的字符串 : " Wdy, DD-Mth-YY HH:MM:SS GMT "  2.秒数  3.datetime.datetime 对象
            # 若 max_age和 expires 同时存在, 则默认使用 max_age  如果设置的cookie时间小于计算机时间, 浏览器则不提取cookie
        else:
            clean_error = form.errors.get("__all__")
            res = render(request, 'login.html', locals())
    else:
        # 数据初始化
        '''
        userlis=[]
        for i in range(1, 10):
            userlis.append(UserInfo(name='yangxga%s'%i, pwd='123456'))
        UserInfo.objects.bulk_create(userlis)
        '''
        form = Myform()
        res = render(request, 'login.html', locals())
    return res


def session(request):
    if request.method == 'POST':
        print(request.POST)
        form = Myform(request.POST)
        if form.is_valid():
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 设置session  如果数据库没有这个sessionid，数据库会插入一条记录，如果有，则更新数据库记录
            request.session['user'] = form.cleaned_data.get('name')
            request.session['last_login_time'] = now
            request.session['delete_test'] = 'delete_test'
            res = redirect('/app01/index')
            '''
            设置session的过程
            if request.COOKIE.get("sessionid"):
                更新
                 在django—session表中创建一条记录:
                   session-key                                     session-data
                   i2yqstppfexaxy6z74e2b1sggw5j7gm2                  更新数据
            else:
                1 生成随机字符串   i2yqstppfexaxy6z74e2b1sggw5j7gm2
                2 response.set_cookie("sessionid",i2yqstppfexaxy6z74e2b1sggw5j7gm2)
                3 在django—session表中创建一条记录:
                   session-key                                     session-data
                   i2yqstppfexaxy6z74e2b1sggw5j7gm2       {"user":yangxga1,"last_login_time":"2019-08-15 21:24:55"}
            '''
        else:
            clean_error = form.errors.get("__all__")
            res = render(request, 'login.html', locals())
    else:
        # 数据初始化
        '''
        userlis=[]
        for i in range(1, 10):
            userlis.append(UserInfo(name='yangxga%s'%i, pwd='123456'))
        UserInfo.objects.bulk_create(userlis)
        '''
        form = Myform()
        res = render(request, 'login.html', locals())
    return res


def index(request):
    '''
    # cookies
    print(request.COOKIES)
    user = request.COOKIES.get('user')  # 获取cookies
    last_login_time = request.COOKIES.get('last_login_time')
    res = render(request, 'index.html', locals())
    # res.delete_cookie('user')  # 删除cookies
    print(request.COOKIES)
    '''
    #sessions
    # print(request.session['user'])
    # user = request.session['user']  # 获取cookies
    # last_login_time = request.session['last_login_time']
    user = request.session.get('user') # 这种方法也行，建议这种，没取到不会报错
    last_login_time = request.session.get('last_login_time')
    '''
    查找的过程
        1  request.COOKIE.get("session")  #  i2yqstppfexaxy6z74e2b1sggw5j7gm2
        2  django-session表中过滤纪录:
           obj=django—session.objects .filter(session-key=ltv8zy1kh5lxj1if1fcs2pqwodumr45t).first()
        3 obj.session-data.get("user")
        '''
    # del request.session['delete_test']  # 删除session
    # print(request.session.get('delete_test'))
    res = render(request, 'index.html', locals())
    return res


def logout(request):
    request.session.flush()  # 清空当前sessionid下的session值
    '''
    清空的过程
    1 randon_str=request.COOKIE.get("sessionid")
    2 django-session.objects.filter(session-key=randon_str).delete()
    3 response.delete_cookie("sessionid",randon_str)

    '''
    return redirect('/app01/session')


'''
class HttpResponseBase:
    def set_cookie(self, key, 键
        value='',          值
        max_age=None,      超长时间cookie需要延续的时间（以秒为单位）如果参数是\ None`` ，这个cookie会延续到浏览器关闭为止。
        expires=None,      超长时间expires默认None ,cookie失效的实际日期/时间。 
        path='/',           Cookie生效的路径，浏览器只会把cookie回传给带有该路径的页面，这样可以避免将
                            cookie传给站点中的其他的应用。 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
        domain=None,         Cookie生效的域名你可用这个参数来构造一个跨站cookie。如， 
                            domain=".example.com"所构造的cookie对下面这些站点都是可读的：
                             www.example.com 、 www2.example.com 和an.other.sub.domain.example.com 。
                            如果该参数设置为 None ，cookie只能由设置它的站点读取。
        secure=False,        如果设置为 True ，浏览器将通过HTTPS来回传cookie。
        httponly=False       只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
            ): pass
            
# settings
SESSION_COOKIE_NAME= "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH= "/"                               # Session的cookie保存的路径（默认）
SESSION_COOKIE_AGE = 10                             # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False                     # 是否每次请求都保存Session，默认修改之后才保存（默认）
      
'''
