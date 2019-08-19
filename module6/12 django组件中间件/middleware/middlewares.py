from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from middleware import settings
import time


'''
中间件顾名思义，是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。
因为改变的是全局，所以需要谨慎实用，用不好会影响到性能。
如果你想修改请求，例如被传送到view中的HttpRequest对象。 或者你想修改view返回的HttpResponse对象，这些都可以通过中间件来实现。
可能你还想在view执行之前做一些操作，这种情况就可以用 middleware来实现。
'''


class MdOne(MiddlewareMixin):

    # 当用户发起请求的时候会依次经过所有的的中间件，这个时候的请求时process_request,最后到达views的函数中，views函数处理后，
    # 在依次穿过中间件，这个时候是process_response,最后返回给请求者。
    def process_request(self, request):
        ip_black_lis = ['127.0.0.1']
        print("----------------------> 请求到达MdOne.process_request")
        ip = request.META.get('REMOTE_ADDR')
        # 请求到达中间件process_request，如果process_request函数有return，那么将不再继续按正常的流程走到视图函数
        # 而是直接返回数据给客户端()，如之前是  A->B->C->视图函数  假如B中发生return，直接返回数据 B->A->客户端
        # if ip in ip_black_lis:
        #     return HttpResponse('ip在黑名单内，请求中断！')

    # 当最后一个中间的process_request到达路由关系映射之后，返回到中间件1的process_view，然后依次往下，到达views函数。
    # 最后通过process_response依次返回到达用户。
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("----------------------> 请求到达MdOne.process_view")
        # process_view如果有返回值，会越过其他的process_view以及视图函数，但是所有的process_response都还会执行。
        # return HttpResponse('ojbk!')

        # 还可以直接调用视图函数
        # response = callback(request, *callback_args, **callback_kwargs)
        # return response

    # 当视图函数报错时，执行这个函数，注意这里已经到达了视图函数，开始网上冒泡，所以这里先答应 MdTwo的process_exception
    # HttpResponse('内部有误！') 返回给客户端，如果在 MdTwo 中有返回，则跳过 MdOne 的 MdTwo的process_exception 直接到 MdTwo的process_response
    def process_exception(self, request, exception):
        print("----------------------> 当视图函数出错MdOne.process_exception")
        # return HttpResponse('内部有误！')

    def process_response(self, request, response):
        print("----------------------> 返回达到MdOne.process_response")
        return response


class MdTwo(MiddlewareMixin):

    def process_request(self, request):
        print("----------------------> 请求到达MdTwo.process_request")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("----------------------> 请求到达MdTwo.process_view")

    def process_exception(self, request, exception):
        print("----------------------> 当视图函数出错MdTwo.process_exception")
        return HttpResponse('内部有误！')

    def process_response(self, request, response):
        print("----------------------> 返回达到MdTwo.process_response")
        return response


ip_pool = {}
# Django中间件限制用户每分钟访问次数不超过10次,一般用于反爬
class IpLimitMiddleWare(MiddlewareMixin):

    def time_filter(self, val):
        return time.time() - val < 60

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip_pool.get(ip):
            ip_pool[ip] = list(filter(self.time_filter, ip_pool[ip]))
            ip_pool[ip].append(time.time())
        else:
            ip_pool[ip] = [time.time()]
        print(ip_pool)
        if len(ip_pool[ip]) > 10:
            return HttpResponse("频繁访问，请稍后再试！")


# URL访问过滤
# 如果用户访问的是login视图（放过）
# 如果访问其他视图，需要检测是不是有session认证，已经有了放行，没有返回login，这样就省得在多个视图函数上写装饰器了！
class AuthLimit(MiddlewareMixin):

    def process_request(self, request):
        path = request.path
        print(path)
        if path != settings.LOGIN_URL and not request.user.is_authenticated:
            new_path = settings.LOGIN_URL + '?next=' + path
            return redirect(new_path)