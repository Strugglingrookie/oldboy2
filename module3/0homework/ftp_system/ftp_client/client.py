# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket
import os
import struct
import json


class Myclient():
    online = 0
    ip = "127.0.0.1"
    port = 8083
    ip_port = (ip, port)
    download_path = r"E:\Study\oldboy\module3\0homework\ftp_system\ftp_client\download"

    def __init__(self):
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.connect(self.ip_port)  # 主动初始化TCP服务器连接

    def send_msg(self, msg_bytes):
        """发送本次请求的指令，服务端根据指令返回数据"""
        header = {"msg_size": len(msg_bytes)}
        header_bytes = json.dumps(header).encode("utf-8")
        header_size = struct.pack("i", len(header_bytes))
        self.server_socket.send(header_size)
        self.server_socket.send(header_bytes)
        self.server_socket.send(msg_bytes)

    def send_code(self, code_dic):
        """发送上传文件的结果状态，服务端根据这些状态做下一步操作"""
        res_code_bytes = bytes(json.dumps(code_dic), encoding='utf-8')
        res_code_len_bytes = struct.pack("i", len(res_code_bytes))
        self.server_socket.send(res_code_len_bytes)
        self.server_socket.send(res_code_bytes)

    @property
    def get_code(self):
        """拿到服务端关于本次指令的操作结果"""
        code_len_bytes = self.server_socket.recv(4)
        code_len = struct.unpack("i", code_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
        code_str = self.server_socket.recv(code_len).decode("utf-8")  # 根据上面的长度接收数据头信息
        code_dic = json.loads(code_str, encoding="utf-8")
        code = code_dic["code"]
        msg = code_dic["msg"]
        return code, msg

    def login(self):
        count = 0
        while count < 3:
            user = input("your name:").strip()
            password = input("your password:").strip()
            if user and password:
                msg = "login %s,%s" % (user, password)
                msg_bytes = msg.encode("utf-8")
                self.send_msg(msg_bytes)
                res_code, res_msg = self.get_code
                print(res_msg)
                if res_code == "0":
                    login_code, login_msg = self.get_code
                    print(login_msg)
                    if login_code == "0":
                        Myclient.online = 1
                        break
                count += 1
            else:
                print("账号或密码不能为空！")
        else:
            exit("too many login!")

    def _sz(self, file_name):
        file_abspath = os.path.join(self.download_path, file_name)
        if not os.path.exists(file_abspath):
            data_code = {"code": "0", "msg": file_name}
            self.send_code(data_code)
            res_code, res_msg = self.get_code
            print(res_msg)
            if res_code == "0":
                header_len_bytes = self.server_socket.recv(4)  # 接收4个字节的数据头信息
                header_len = struct.unpack("i", header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
                header_str = self.server_socket.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
                header = json.loads(header_str, encoding="utf-8")
                file_size = header["file_size"]  # 根据数据头信息得到本次要接收的数据大小
                recv_size = 0
                tmp_size = 0
                per_size = file_size/50
                num = 1
                with open(file_abspath, "wb") as f:
                    while recv_size < file_size:  # 当接收到的数据小于本次数据长度时就一直接收
                        if tmp_size > per_size:
                            rate = str((recv_size / file_size)*100)[:5] + "%"
                            print("%s %s" % ("#"*num, rate))
                            tmp_size = 0
                            num += 1
                        line = self.server_socket.recv(1024)
                        f.write(line)  # 将每次接收到的数据拼接
                        recv_size += len(line)  # 实时记录当前接收到的数据长度
                        tmp_size += len(line)
                print("%s %s" % ("#" * (num+1), "100.00%"))
                print("download file %s success!" % file_name)
        else:
            res_code = {"code": "1", "msg": file_name}
            self.send_code(res_code)
            print("%s is already exists" % file_name)

    def _rz(self, file_path):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            res_code = {"code": "0", "msg": file_name}
            self.send_code(res_code)
            res_code, res_msg = self.get_code
            print(res_msg)
            if res_code == "0":
                file_size = os.path.getsize(file_path)
                header = {"file_size": file_size, "file_name": file_name, "md5": "123456"}
                header_bytes = bytes(json.dumps(header), encoding='utf-8')
                header_len_bytes = struct.pack("i", len(header_bytes))
                self.server_socket.send(header_len_bytes)
                self.server_socket.send(header_bytes)
                res_code, res_msg = self.get_code
                print(res_msg)
                upload_size = 0
                tmp_size = 0
                per_size = file_size / 50
                num = 1
                if res_code == "0":
                    with open(file_path, "rb") as f:
                        for line in f:
                            if tmp_size > per_size:
                                rate = str((upload_size / file_size) * 100)[:5] + "%"
                                print("%s %s" % ("#" * num, rate))
                                tmp_size = 0
                                num += 1
                            self.server_socket.send(line)
                            upload_size += len(line)
                            tmp_size += len(line)
                    print("%s %s" % ("#" * (num + 1), "100.00%"))
                    print("upload file %s success!" % file_name)
        else:
            res_code = {"code": "1", "msg": "no such file: %s " % file_path}
            self.send_code(res_code)
            print("上传文件不存在！")

    def _ls(self, dirname):
        """查看当前文件夹下的文件或目录！"""
        res_code, res_msg = self.get_code
        print(res_msg)
        if res_code == "0":
            header_len_bytes = self.server_socket.recv(4)
            header_len = struct.unpack("i", header_len_bytes)[0]
            header_str = self.server_socket.recv(header_len).decode("utf-8")
            header = json.loads(header_str, encoding="utf-8")
            file_size = header["file_size"]
            recv_size = 0
            res = b''
            while recv_size < file_size:
                res += self.server_socket.recv(1024)
                recv_size = len(res)
            res = res.decode("GBK")
            print(res)

    def _cd(self, dirname):
        res_code, res_msg = self.get_code
        print(res_msg)

    def run(self):
        """反复向服务器发送请求，当请求的返回操作码为0成功时，调用相应属性，失败时不做任何处理直接循环"""
        self.login()
        print("attention please : input: ls . to see file or dir in the current dir！")
        while True:
            msg = input(">>>>:").strip()
            msg_lis = msg.split(" ", 1)
            if len(msg_lis) == 2 and hasattr(self, "_%s" % msg_lis[0].lower()):
                method = msg_lis[0].lower()
                args = msg_lis[1]
                msg_bytes = msg.encode("utf-8")
                self.send_msg(msg_bytes)
                res_code, res_msg = self.get_code
                print(res_msg)
                if res_code == "2":
                    self.login()
                if res_code == "0":
                    func = getattr(self, "_%s" % method.lower())
                    func(args)
            else:
                print("输入格式不正确，请重新输入！")

    def __del__(self):
        self.server_socket.close()


if __name__ == "__main__":
    try :
        client = Myclient()
        client.run()
    except Exception as e:
        print(e)
