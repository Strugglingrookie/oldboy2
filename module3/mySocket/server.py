# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket,subprocess,struct,json


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
        while True: # 循环和客户端交互，收、发信息
            rec = conn.recv(1024)  # 最多接收1024个字节的数据
            if not rec:break  # 当客户端暴力断开连接时，linux下会进入死循环接收数据为空，所以当接收数据为空的时候跳出循环

            # 执行客户端发送过来的shell命令，执行命令，并返回执行结果
            res = subprocess.Popen(rec.decode("utf-8"), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            err = res.stderr.read()
            out = res.stdout.read()
            datas = err if err else out

            header = {"file_size":len(datas)} # 数据头信息，记录这次需要发送的文件大小
            header_bytes = bytes(json.dumps(header),encoding='utf-8') # 将数据头信息处理成bytes，便于发送
            header_len_bytes = struct.pack("i",len(header_bytes)) # 规定发送4个字节记录数据头的大小
            # 发送数据(send在待发送数据量大于己端缓存区剩余空间时,数据丢失,不会发完) 注：数据必须是bytes类型
            conn.send(header_len_bytes)  # 发送长度为4个字节经过struct打包的数据头长度信息
            conn.send(header_bytes)     # 发送数据头信息，客户端根据上面接收到的数据头长度，接收指定长度的数据头信息
            conn.send(datas)    #发送正式数据，客户端根据上面接收到数据头信息得到本次发送的数据长度，接收指定长度数据

        conn.close()  # 关闭连接套接字
    except Exception as e:
        print(e)

server_socket.close()  # 关闭套接字