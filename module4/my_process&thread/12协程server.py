# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23

# 多线程：
'''
import socket
from threading import Thread, currentThread


server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8089))
server.listen(1000)


def rec_data(conn):
    while True:
        try:
            res = conn.recv(1024)
            if not res:break
            res = res.upper()
            conn.send(res)
        except Exception as e:
            print(e)


def start():
    print("starting...")
    while True:
        conn, addr = server.accept()
        print(addr)
        t = Thread(target=rec_data, args=(conn,))
        t.start()


if __name__ == "__main__":
    start()
'''


# 协程
# 通过gevent实现单线程下的socket并发（from gevent import monkey;monkey.patch_all()
# 一定要放到导入socket模块之前，否则gevent无法识别socket的阻塞）
from gevent import monkey;monkey.patch_all()
import socket, gevent
#如果不想用money.patch_all()打补丁,可以用gevent自带的socket
# from gevent import socket
# s=socket.socket()


def rec_data(conn):
    while True:
        try:
            res = conn.recv(1024)
            if not res:break
            res = res.upper()
            conn.send(res)
        except Exception as e:
            print(e)
        finally:
            conn.close()


def start():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8089))
    server.listen(1000)
    print("starting...")
    while True:
        conn, addr = server.accept()
        print(addr)
        gevent.spawn(rec_data, conn)
    server.close()


if __name__ == "__main__":
    g = gevent.spawn(start)
    g.join()
