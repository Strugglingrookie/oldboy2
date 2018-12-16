# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket
import os
import struct
import json


class Myserver():
    ip = "127.0.0.1"
    port = 8083
    max_connect = 1  # 最对只接收5个连接，超过时直接拒绝
    ip_port = (ip, port)
    send_path = r"/Users/yangyiyi/Documents/oldboy/module3/mySocket/socket_class/file_server/share"
    recv_path = r"/Users/yangyiyi/Documents/oldboy/module3/mySocket/socket_class/file_server/share"

    def __init__(self):
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.ip_port)
        self.server_socket.listen(self.max_connect)
        print("starting....")

    def send_file(self, conn, file_name):
        file_path = os.path.join(self.send_path, file_name)
        file_size = os.path.getsize(file_path)
        header = {"file_size": file_size, "file_name": file_name, "md5": "123456"}
        header_bytes = bytes(json.dumps(header), encoding='utf-8')
        header_len_bytes = struct.pack("i", len(header_bytes))
        conn.send(header_len_bytes)
        conn.send(header_bytes)
        with open(file_path, "rb") as f:
            for line in f:
                conn.send(line)

    def recv_file(self, conn, file_name):
        file_name = os.path.basename(file_name)
        file_abspath = os.path.join(self.recv_path, file_name)
        header_len_bytes = conn.recv(4)  # 接收4个字节的数据头信息
        header_len = struct.unpack("i", header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
        header_str = conn.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
        header = json.loads(header_str, encoding="utf-8")
        file_size = header["file_size"]  # 根据数据头信息得到本次要接收的数据大小
        recv_size = 0

        with open(file_abspath, "wb") as f:
            while recv_size < file_size:  # 当接收到的数据小于本次数据长度时就一直接收
                line = conn.recv(1024)
                f.write(line)  # 将每次接收到的数据拼接
                recv_size += len(line)  # 实时记录当前接收到的数据长度

    def file_fun(self, conn):
        methods = {"get": self.send_file, "put": self.recv_file}
        while True:
            header_len_bytes = conn.recv(4)  # 接收4个字节的数据头信息
            if not header_len_bytes:
                break
            header_len = struct.unpack("i", header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
            header_str = conn.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
            header = json.loads(header_str, encoding="utf-8")
            msg_size = header["msg_size"]  # 根据数据头信息得到本次要接收的数据大小
            rec = conn.recv(msg_size).decode("utf-8")
            print(rec)
            file_method = rec.split()[0].lower()
            file_name = rec.split()[1]
            methods[file_method](conn, file_name)
        conn.close()

    def run(self):
        while True:
            try:
                conn, client_addr = self.server_socket.accept()
                self.file_fun(conn)
            except Exception as e:
                print(e)

    def __del__(self):
        self.server_socket.close()


if __name__ == "__main__":
    server1 = Myserver()
    server1.run()
