# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/16


# udp协议不需要建立链接，直接发送和接收，接收方的地址放在发送函数的第二个位置参数上
# 缺点  不可靠，没有确保数据一定送达，它只做了一件事，发送数据，对方有没有收到，都不在发送。
# 优点  1.因为不需要建链接和确认数据收到，所以发送速度更快  2.不存在粘包现象
# 应用  QQ的消息发送就是用的udp，一般用于数据查询


import socket


ip = "127.0.0.1"
port = 8083
ip_port = (ip, port)
soctet_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
soctet_server.bind(ip_port)
print("starting....")
msg, addr = soctet_server.recvfrom(1024)
soctet_server.sendto(msg.upper(), addr)
print(msg.decode("utf-8"))

