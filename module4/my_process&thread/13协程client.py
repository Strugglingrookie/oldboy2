# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23


import socket
from threading import Thread, currentThread


def send_msg():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8089))
    while True:
        msg = "%s say hello" % currentThread().getName()
        client.send(msg.encode())
        res = client.recv(1024)
        print(res)


if __name__ == "__main__":
    for i in range(100):
        t = Thread(target=send_msg)
        t.start()
