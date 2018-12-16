# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/16


import socket


ip = "127.0.0.1"
port = 8083
ip_port = (ip, port)
socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket_client.sendto(b"hello", ip_port)
msg, addr = socket_client.recvfrom(1024)
print(msg.decode("utf-8"), addr)
