# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket
import os
import struct
import json
import re


class Myclient():
    ip = "127.0.0.1"
    port = 8083
    ip_port = (ip, port)
    download_path = r"/Users/yangyiyi/Documents/oldboy/module3/mySocket/socket_class/file_client/download"

    def __init__(self):
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.connect(self.ip_port)  # 主动初始化TCP服务器连接

    def get_file(self,server_socket, file_name):
        file_abspath = os.path.join(self.download_path, file_name)
        header_len_bytes = server_socket.recv(4)  # 接收4个字节的数据头信息
        header_len = struct.unpack("i", header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
        header_str = server_socket.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
        header = json.loads(header_str, encoding="utf-8")
        file_size = header["file_size"]  # 根据数据头信息得到本次要接收的数据大小
        recv_size = 0

        with open(file_abspath, "wb") as f:
            while recv_size < file_size:  # 当接收到的数据小于本次数据长度时就一直接收
                line = server_socket.recv(1024)
                f.write(line)  # 将每次接收到的数据拼接
                recv_size += len(line)  # 实时记录当前接收到的数据长度

    def put_file(self, server_socke, file_name):
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
            header = {"file_size": file_size, "file_name": file_name, "md5": "123456"}
            header_bytes = bytes(json.dumps(header), encoding='utf-8')
            header_len_bytes = struct.pack("i", len(header_bytes))
            server_socke.send(header_len_bytes)
            server_socke.send(header_bytes)
            with open(file_name, "rb") as f:
                for line in f:
                    server_socke.send(line)
        else:
            print("上传文件不存在！")

    def run(self):
        while True:
            msg = input(">>>>:").strip()
            if re.fullmatch(r"(get|put){1}\s{1}\S+", msg, re.I):
                msg_lis = msg.split()
                file_method = msg_lis[0].lower()
                file_name = msg_lis[1]
                msg_bytes = msg.encode("utf-8")
                header = {"file_method": file_method, "msg_size": len(msg_bytes)}
                header_bytes = json.dumps(header).encode("utf-8")
                header_size = struct.pack("i", len(header_bytes))
                self.server_socket.send(header_size)
                self.server_socket.send(header_bytes)
                self.server_socket.send(msg_bytes)  # 发送的数据必须是bytes类型
                print(file_name)
                methods[file_method](self.server_socket, file_name)
            else:
                print("输入格式不正确，请重新输入！")

    def __del__(self):
        self.server_socket.close()


if __name__ == "__main__":
    client = Myclient()
    client.run()
