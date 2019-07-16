# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 20:05
# @Author  : Xiao

from wsgiref.simple_server import make_server
from urls import url_datas

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html'),('Charset','utf8')])
    print("PATH", environ.get("PATH_INFO"))
    # 当前请求路径
    path = environ.get("PATH_INFO")
    func = None
    for item in url_datas:
        if path == item[0]:
            func = item[1]
            break
    if func:
        return [func(environ)]
    return [b'404!']

server = make_server('',8080,application)

# 开始监听HTTP请求:
print('starting....')
server.serve_forever()

'''
web框架 yuan功能总结
main.py: 启动文件,封装了socket
1 urls.py: 路径与视图函数映射关系  ---- url控制器
2 views.py 视图函数,固定有一个形式参数:environ -----视图函数,
3 templates文件夹: html文件   -----模板
4 models: 在项目启动前,在数据库中创建表结构    ----- 与数据库相关
'''

