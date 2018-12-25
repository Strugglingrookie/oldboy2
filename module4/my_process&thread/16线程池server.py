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

# queue实现的线程池：

import socket, queue
from threading import Thread, currentThread


server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8089))
server.listen(1000)
# pool = ThreadPoolExecutor(2)
q = queue.Queue(1000)


def rec_data():
    while True:
        conn = q.get()
        while True:
            try:
                res = conn.recv(1024)
                if not res:break
                res = res.upper()
                conn.send(res)
                print("server cunrrent thread: %s" % currentThread().getName())
            except Exception as e:
                print(e)
                conn.close()
                q.task_done()
                break


def start():
    print("starting...")
    for i in range(2):
        t = Thread(target=rec_data)
        t.daemon = True
        t.start()
    while True:
        conn, addr = server.accept()
        q.put(conn)
        # pool.submit(rec_data, conn, addr)


if __name__ == "__main__":
    start()