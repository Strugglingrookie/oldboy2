# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 10:10
# @Author  : Xiao


# 非阻塞的recvform系统调用调用之后，进程并没有被阻塞，内核马上返回给进程，如果数据还没准备好，
# 此时会返回一个error。进程在返回之后，可以干点别的事情，然后再发起recvform系统调用。重复上面的过程，
# 循环往复的进行recvform系统调用。这个过程通常被称之为轮询。轮询检查内核数据，直到数据准备好，再拷贝数据到进程，
# 进行数据处理。需要注意，拷贝数据整个过程，进程仍然是属于阻塞的状态。
import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8089))
server.listen(1000)
server.setblocking(False)
print("starting...")

rlis = []
wlis = []
while True:
    try:
        print("trying to accept conn...")
        conn, addr = server.accept()
        rlis.append(conn)
        if addr:
            print("get conn %s" % str(addr))
    except BlockingIOError:

        #收消息
        del_rlis = []
        # print(rlis)
        for conn in rlis:
            try:
                print("trying to recv datas...")
                res = conn.recv(1024)
                if not res:
                    del_rlis.append(conn)
                    continue
                res = res.upper()
                wlis.append([conn, res])
            except BlockingIOError:
                continue
            except Exception as e:
                conn.close()
                del_rlis.append(conn)
        for conn in del_rlis:
            rlis.remove(conn)

        # 发消息
        del_wlis = []
        for datas in wlis:
            print("tr ying to send datas...")
            conn = datas[0]
            data = datas[1]
            try:
                conn.send(data)
                del_wlis.append(datas)
            except BlockingIOError:
                continue
            except Exception as e:
                conn.close()
                del_wlis.append(datas)
        for datas in del_wlis:
            wlis.remove(datas)

server.close()
