# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket,subprocess,struct,json


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