# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 8:37
# @Author  : Xiao

import socket


'''
地址簇：
socket.AF_INET:典型的TCP/IP四层模型的通信过程,发送方、接收方依赖IP:Port来标识，即将本地的socket绑定到对应的IP端口上;
发送数据时，指定对方的IP端口，经过Internet，可以根据此IP端口最终找到接收方；接收数据时，可以从数据包中获取到发送方的IP端口。
socket.AF_UNIX：典型的本地IPC，类似于管道，依赖路径名标识发送方和接收方。即发送数据时，指定接收方绑定的路径名，
操作系统根据该路径名可以直接找到对应的接收方，并将原始数据直接拷贝到接收方的内核缓冲区中，并上报给接收方进程进行处理。
同样的接收方可以从收到的数据包中获取到发送方的路径名，并通过此路径名向其发送数据.（可实现进程间的通讯）
类型：
socket.SOCK_STREAM：流式socket , for TCP
socket.SOCK_DGRAM： 数据报式socket , for UDP
socket.SOCK_RAW：   原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；
SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
'''
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
        with open('index.html', 'rb') as f:
            data = f.read()
        # 发送数据给客户端，必须要发送这个，浏览器才可以解析
        conn.send(b"HTTP/1.1 200 OK\r\nstatus: 200\r\nContent-Type:text/html\r\n\r\n%s"%data)
        conn.close()  # 关闭连接套接字
    except Exception as e:
        print(e)
