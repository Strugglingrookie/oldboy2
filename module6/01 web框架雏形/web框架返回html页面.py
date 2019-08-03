# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 8:37
# @Author  : Xiao

import socket

ip_port= ("127.0.0.1",8081)
max_connect = 1  # 最对只接收5个连接，超过时直接拒绝

# 实例化socket套接字对象，指定地址簇为socket.AF_INET；类型为socket.SOCK_STREAM　流式socket , for TCP
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 端口复用，当程序重启时端口还是被占用的，加上这个可忽略端口冲突报错
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(ip_port)  # 绑定本机ip+port
server_socket.listen(max_connect)  # 开始TCP监听，5代表在允许有一个连接排队，更多的新连接连进来时就会被拒绝
print("starting....")
while True: # 循环生成连接对象，当前连接断开马上进入下一次等待，知道有连接
    try:  # 当客户端暴力断开连接时，windows下会报错，所以用try防止报错导致程序奔溃
        conn,client_addr = server_socket.accept()  # #阻塞直到有连接为止，有了一个新连接进来后，就会为这个请求生成一个连接对象
        rec = conn.recv(1024)  # 最多接收1024个字节的数据
        if not rec:break  # 当客户端暴力断开连接时，linux下会进入死循环接收数据为空，所以当接收数据为空的时候跳出循环
        # 注意一定要以rb形式打开，因为http网络传输的时候只能传输bytes字节，如果不是rb，需要encode转一下才可以
        with open('index1.html', 'rb') as f:
            data = f.read()
        # 发送数据给客户端，必须要发送这个，浏览器才可以解析
        conn.send(b"HTTP/1.1 200 OK\r\nstatus: 200\r\nContent-Type:text/html\r\n\r\n%s"%data)
        conn.close()  # 关闭连接套接字
    except Exception as e:
        print(e)
