# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket,subprocess,struct,json,threading,time


ip_port= ("127.0.0.1",8081)
max_connect = 1
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(ip_port)
server_socket.listen(max_connect)
print("starting....")


def client_conn(conn):
    while True:
        try:
            rec = conn.recv(1024)
            if not rec: break  # 当客户端暴力断开连接时，跳出循环  linux系统

            res = subprocess.Popen(rec.decode("utf-8"), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            err = res.stderr.read()
            out = res.stdout.read()
            datas = err if err else out

            header = {"file_size": len(datas)}
            header_bytes = bytes(json.dumps(header), encoding='utf-8')
            header_len_bytes = struct.pack("i", len(header_bytes))

            conn.send(header_len_bytes)
            conn.send(header_bytes)
            conn.send(datas)
        except Exception as e:
            print(conn,e)
            break   # 当客户端暴力断开连接时，跳出循环  windows系统
    conn.close()

# 多线程，可同时和多个客户端通信,来一个接收一个
while True:
    conn, client_addr = server_socket.accept()
    t = threading.Thread(target=client_conn,args=(conn,))
    t.start()

server_socket.close()