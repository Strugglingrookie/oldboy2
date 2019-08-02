# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 9:03
# @Author  : Xiao

from wsgiref.simple_server import make_server

def open_file(filename):
    with open(filename,'rb') as f:
        data= f.read()
    return data

#定义一个函数，供创建服务使用，当有请求来时，调用这个函数
# environ    根据http协议解析的请求参数 包括请求首行 请求头 请求体
# start_response  根据http协议组装返回数据  包括请求首行 请求头
def application(environ, start_response):
    print(environ)
    print(environ.get('PATH_INFO'))  # 请求路径
    start_response('200 OK',[('Content-Type','text/html')])
    path = environ.get('PATH_INFO')
    data = open_file('login.html') if path == '/login' else open_file('index.html')
    return [data]
# 创建服务，当没指定服务ip时，默认是127.0.0.1
my_server = make_server('',8081,application)
print('starting...')
# 启动服务，开始监听请求
my_server.serve_forever()