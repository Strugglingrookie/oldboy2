# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:17
# @Author  : Xiao


# 多路复用IO，也叫事件驱动IO
'''
基本原理就是select/epoll这个function会不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程

当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，
当任何一个socket中的数据准备好了，select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。
而blocking IO只调用了一个系统调用\(recvfrom\)。但是，用select的优势在于它可以同时处理多个connection

强调：
1. 如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，可能延迟还更大。select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。
2. 在多路复用模型中，对于每一个socket，一般都设置成为non-blocking，但是，如上图所示，整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO给block。
结论: select的优势在于可以处理多个连接，不适用于单个连接

优点：
相比其他模型，使用select() 的事件驱动模型只用单线程（进程）执行，占用资源少，不消耗太多 CPU，同时能够为多客户端提供服务。
如果试图建立一个简单的事件驱动的服务器程序，这个模型有一定的参考价值。

缺点：
首先select()接口并不是实现“事件驱动”的最好选择。因为当需要探测的句柄值较大时，select()接口本身需要消耗大量时间去轮询各个句柄。
很多操作系统提供了更为高效的接口，如linux提供了epoll，BSD提供了kqueue，Solaris提供了/dev/poll，…。
如果需要实现更高效的服务器程序，类似epoll这样的接口更被推荐。遗憾的是不同的操作系统特供的epoll接口有很大差异，
所以使用类似于epoll的接口实现具有较好跨平台能力的服务器会比较困难。
其次，该模型将事件探测和事件响应夹杂在一起，一旦事件响应的执行体庞大，则对整个模型是灾难性的。
'''

import socket
import select

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8089))
server.listen(1000)
server.setblocking(False)
print("starting...")

rlis = [server,]
wlis = []
wdata = {}
while True:
    rl, wl, xl = select.select(rlis, wlis, [], 0.5)  # 每隔0.5秒批量询问操作系统

    # 收消息
    for sock in rl:
        if sock == server:
            print("trying to accept conn...")
            conn, addr = server.accept()
            rlis.append(conn)
            print("get conn %s" % str(addr))
        else:
            try:
                print("trying to recv datas...")
                res = sock.recv(1024)
                if not res:
                    sock.close()
                    rlis.remove(sock)
                    continue
                res = res.upper()
                wlis.append(sock)
                wdata[sock] = res
            except Exception as e:
                sock.close()
                rlis.remove(sock)

    # 发消息
    for sock in wl:
        print("trying to send datas...")
        res = wdata[sock]
        sock.send(res)
        wlis.remove(sock)
        wdata.pop(sock)

server.close()