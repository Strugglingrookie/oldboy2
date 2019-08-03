from django.shortcuts import render,redirect,HttpResponse
from views_app01.tools import Mysql

# Create your views here.


def index(request):
    return render(request,'index.html',{'word':'嗯哼'})


# HttpRequest对象
def login(request):
    # request属性  django将请求报文中的请求行、首部信息、内容主体封装成 HttpRequest 类中的属性
    # body  是post请求参数，一个字符串，代表请求报文的主体。在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML,Json等
    print('request.body:\n',request.body)

    # method 请求方式 get post 等
    method = request.method
    print('method:\n',method)

    # path  一个字符串，表示请求的路径组件（不含域名）
    print('path:\n',request.path)

    # encoding   一个字符串，表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）
    # 这个属性是可写的，你可以修改它来修改访问表单数据使用的编码
    print('encoding:\n', request.encoding)

    # META  一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器
    print('META:\n', request.META)
    '''CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE —— 请求的正文的MIME 类型。
    HTTP_ACCEPT —— 响应可接收的Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST —— 客服端发送的HTTP Host 头部。
    HTTP_REFERER —— Referring 页面。
    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR —— 客户端的IP 地址。
    REMOTE_HOST —— 客户端的主机名。
    REMOTE_USER —— 服务器认证后的用户。
    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME —— 服务器的主机名。
    SERVER_PORT —— 服务器的端口（是一个字符串）。
 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。'''

    # FILES 一个类似于字典的对象，包含所有的上传文件信息
    # FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据
    # FILES 只有在请求为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况才会包含数据。否则，FILES 将为一个空的类似于字典的对象。
    print('FILES:\n', request.FILES)

    # COOKIES  一个标准的Python 字典，包含所有的cookie。键和值都为字符串。
    print('COOKIES:\n', request.COOKIES)

    # session 一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
    print('session:\n', request.session)

    # user 一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户
    # 如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们
    print('user:\n', request.user)


    # request方法
    # get_full_path  返回 path，如果可以将加上查询字符串,即get请求后面的查询参数，如：/app01/login/?a=1&b=2。
    print('get_full_path:\n',request.get_full_path())

    # is_ajax
    print('is_ajax:\n',request.is_ajax())
    '''如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。
　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存'''

    if method.lower() == 'post':
        # 如果使用 POST 上传文件的话，文件信息将包含在 FILES 属性中。
        # 注意：键值对的值是多个的时候,比如checkbox类型的input标签，select标签，需要用：request.POST.getlist("hobby")
        req_data = request.POST  # 一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。
        print('request.POST:\n',req_data)
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        if res and isinstance(res,list):
            return render(request, 'index.html')
        else:
            return HttpResponse('username or password is wrong!')
    else:
        print('request.GET:\n',request.GET)  # 一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象
        return render(request, 'login.html')


# HttpResponse 对象
#响应对象主要有三种形式：HttpResponse()    render()    redirect()
def regist(request):
    method = request.method
    if method.lower() == 'post':
        req_data = request.POST
        user = req_data.get('user')
        pwd = req_data.get('pwd')
        if user and pwd:
            mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
            sql = "select * from user_info WHERE  name=%s"
            res = mysql_check.exec_sql(sql, user)
            if res and isinstance(res,list):
                return HttpResponse('username is already exits!')
            insert_sql = 'insert into user_info (name,password) VALUES (%s,%s) '
            mysql_check.exec_sql(insert_sql, user,pwd)

            # redirect() 重定向
            # return redirect("/app01/index")  # 传递要重定向的一个硬编码的URL
            return redirect("http://127.0.0.1:8080/app01/index/")  # 也可以是一个完整的URL
            '''
            1）301和302的区别。
            　　301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取
              （用户看到的效果就是他输入的地址A瞬间变成了另一个地址B）——这是它们的共同点。
            　　他们的不同在于。301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；
            　　302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 302好于301
            2）重定向原因：
                （1）网站调整（如改变网页目录结构）；
                （2）网页被移到一个新地址；
                （3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
                    这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；
                    再者某些注册了多个域名的网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。'''

        # HttpResponse()括号内直接跟一个具体的字符串作为响应体。
        return HttpResponse('username or password can not be empty !')

    # render(request, template_name[, context]）
    # 结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的 HttpResponse 对象。
    # render方法就是将一个模板页面中的模板语法进行渲染，最终渲染成一个html页面作为响应体
    '''request： 用于生成响应的请求对象。
    template_name：要使用的模板的完整名称，可选的参数
    context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。'''
    return render(request,'register.html',{'word':'hello world!'})