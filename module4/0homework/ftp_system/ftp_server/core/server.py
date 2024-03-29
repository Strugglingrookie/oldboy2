# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:11
# @Author  : Xiao


import socket
import os
import sys
import struct
import json
import hashlib
import configparser
import subprocess
import queue
from threading import Thread
from conf.settings import *


class Myserver(object):
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(MAX_CONNECT)
    q = queue.Queue(MAX_QUEUE)  # 初始化队列大小，最对只能有多少个等待链接

    def __init__(self, conn):
        """实例化时自动启动文件服务"""
        self.conn = conn  # 接收到的客户连接信息
        self.client_addr = None  # 接收到的客户连接地址信息
        self.header_len_bytes = None  # 发送数据的报文头信息
        self.users = self.get_users()  # 拿到用户信息，登录的时候用来判断
        self.online = 0  # 用户的登录状态，每次接收到客户端的命令都要判断用户是否已经登录，未登录需要先登录
        self.home = None  # 用户的家目录，用户登录的时候会更新家目录
        self.cur = None  # 用户的当前目录，用户登录的时候当前目录就是家目录，随着用户cd命令执行更新
        self.quota = 0  # 用户的家目录的大小限制，用户上传时会先判断目录大小是否够接收文件
        print("starting....")

    @staticmethod
    def get_md5(var):
        """"加密，盐值为123456"""
        salt = "123456"
        new_var = salt + var
        m = hashlib.md5()
        m.update(new_var.encode())
        return m.hexdigest()

    @staticmethod
    def get_users():
        '''拿到用户基础信息'''
        """"初始化用户信息"""
        users = configparser.ConfigParser()
        users.read(DATA_PATH)
        return users

    @property
    def get_code(self):
        """拿到客户端上传文件的操作结果"""
        code_len_bytes = self.conn.recv(4)
        code_len = struct.unpack("i", code_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
        code_str = self.conn.recv(code_len).decode("utf-8")  # 根据上面的长度接收数据头信息
        code_dic = json.loads(code_str, encoding="utf-8")
        code = code_dic["code"]
        msg = code_dic["msg"]
        return code, msg

    @property
    def get_msg(self):
        """拿到客户端发来的请求"""
        header_len = struct.unpack("i", self.header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
        header_str = self.conn.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
        header = json.loads(header_str, encoding="utf-8")
        msg_size = header["msg_size"]  # 根据数据头信息得到本次要接收的数据大小
        msg = self.conn.recv(msg_size).decode("utf-8")
        return msg

    def send_code(self,code_dic):
        """发送本次请求的结果状态，客户端根据这些状态做下一步操作"""
        res_code_bytes = bytes(json.dumps(code_dic), encoding='utf-8')
        res_code_len_bytes = struct.pack("i", len(res_code_bytes))
        self.conn.send(res_code_len_bytes)
        self.conn.send(res_code_bytes)

    def _login(self, user_info):
        """登陆逻辑，登录成功后初始化用户的家目录、当前目录、登录状态等信息"""
        info_lis = user_info.split(",")
        if len(info_lis) == 2:
            user, pwd = info_lis
            pwd = self.get_md5(pwd)
            if user in self.users and pwd == self.users[user].get("password"):
                code_dic = {"code": "0", "msg": "login success!"}
                self.send_code(code_dic)
                self.home = os.path.join(HOME_PATH, self.users[user].get("home_dir"))
                self.cur = self.home
                self.quota = float(self.users[user].get("quota"))*(1024**3)
                self.online = 1
                return True
        code_dic = {"code": "1", "msg": "error username or password!"}
        self.send_code(code_dic)

    def _sz(self, file_name):
        """发送文件给客户端
           1.首先拿到客户端的确认信息，是否上传
           2.确定后，判断文件是否存在，并告诉客户端接下来是传文件还是通知文件不存在
           3.文件存在则开始发送文件
        """
        res_code, res_msg = self.get_code
        if res_code == "0":
            file_path = os.path.join(self.cur, file_name)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                code_dic = {"code": "0", "msg": "start to download %s " % file_name}
                self.send_code(code_dic)
                file_size = os.path.getsize(file_path)
                header = {"file_size": file_size, "file_name": file_name, "md5": "123456"}
                header_bytes = bytes(json.dumps(header), encoding='utf-8')
                header_len_bytes = struct.pack("i", len(header_bytes))
                self.conn.send(header_len_bytes)
                self.conn.send(header_bytes)
                with open(file_path, "rb") as f:
                    for line in f:
                        self.conn.send(line)
            else:
                code_dic = {"code": "1", "msg": "%s is a directory or file doesn't exist!" % file_name}
                self.send_code(code_dic)

    def _rz(self, file_name):
        """保存来自文件
           1.首先确认客户端是否要传文件
           2.确定后，判断文件是否存在，并告诉客户端接下来是接收文件还是通知文件已存在
           3.用户当前目录文件不存在则开始接收文件
        """
        res_code, res_msg = self.get_code
        if res_code == "0":
            file_name = os.path.basename(file_name)
            file_abspath = os.path.join(self.cur, file_name)
            if not os.path.exists(file_abspath):
                res_code = {"code": "0", "msg": "start to upload file %s..." % file_name}
                self.send_code(res_code)
                header_len_bytes = self.conn.recv(4)  # 接收4个字节的数据头信息
                header_len = struct.unpack("i", header_len_bytes)[0]  # struct.unpack解压数据，得到数据头信息长度
                header_str = self.conn.recv(header_len).decode("utf-8")  # 根据上面的长度接收数据头信息
                header = json.loads(header_str, encoding="utf-8")
                file_size = header["file_size"]  # 根据数据头信息得到本次要接收的数据大小
                empty_size =float(self.quota) - os.path.getsize(self.home)
                if empty_size < file_size:
                    res_code = {"code": "1", "msg": "only %s space left,no space to accept file %s" % (empty_size,file_name)}
                    self.send_code(res_code)
                else:
                    res_code = {"code": "0", "msg": "uploading file %s..." % file_name}
                    self.send_code(res_code)
                    recv_size = 0
                    with open(file_abspath, "wb") as f:
                        while recv_size < file_size:  # 当接收到的数据小于本次数据长度时就一直接收
                            line = self.conn.recv(1024)
                            f.write(line)  # 将每次接收到的数据拼接
                            recv_size += len(line)  # 实时记录当前接收到的数据长度
            else:
                res_code = {"code": "1", "msg": "%s is already exists..." % file_name}
                self.send_code(res_code)

    def _ls(self, dirname):
        """
        1.接收客户端需要查看的是哪个目录
        2.判断目录是否存在，存在继续往下走，不存在则直接告诉客户端失败，目录不存在
        3.执行命令，如果服务器端是linux系统，则用ls，如果是windows则用dir
        4.如果命令执行结果为空，返回客户端当前目录下没有文件
        5.如果不为空，则开始发送目录下的文件夹或文件信息
        """
        new_dirname = os.path.join(self.cur, dirname) if dirname != "." else self.cur
        print(new_dirname)
        cmd = "dir" if sys.platform.lower().startswith("win") else "ls"
        if os.path.exists(new_dirname) and not os.path.isfile(new_dirname):
            res = subprocess.Popen("%s %s" % (cmd, new_dirname), shell=True, stdout=subprocess.PIPE)
            out = res.stdout.read()
            if out:
                print(out.decode("GBK"))
                res_code = {"code": "0", "msg": "%s dir has follow files or dirs..." % dirname}
                self.send_code(res_code)
                header = {"file_size": len(out)}
                header_bytes = bytes(json.dumps(header), encoding='utf-8')
                header_len_bytes = struct.pack("i", len(header_bytes))
                self.conn.send(header_len_bytes)
                self.conn.send(header_bytes)
                self.conn.send(out)
            else:
                res_code = {"code": "3", "msg": "%s current dir is empty..." % dirname}
                self.send_code(res_code)
        else:
            res_code = {"code": "1", "msg": "%s no such directory" % dirname}
            self.send_code(res_code)

    def _cd(self, dirname):
        """
        1.接收到客户端的需要进入的目录信息，跟当前目录进行拼接
        2.如果目录存在，则修改当前目录的变量值，如果不存在则告诉客户端，目录不存在
        """
        new_dirname = os.path.join(self.cur, dirname)
        if os.path.exists(new_dirname) and not os.path.isfile(new_dirname):
            res_code = {"code": "0", "msg": "切换成功，当前目录为 %s " % dirname}
            self.send_code(res_code)
            self.cur = new_dirname
        else:
            res_code = {"code": "1", "msg": "切换失败， %s 目录不存在" % dirname}
            self.send_code(res_code)

    def comunication(self):
        """
        通信主程序，每个实例都是通过这个方法和客户端通信的。
        1.先判断用户的是否登陆，如果没有登陆而且请求不是login，则返回客户端让其登陆，如果已登陆则往下走
        2.判断用户请求的方法是否正确，不正确则返回客户端，请求方法有误，如果方法存在则往下走
        3.调用具体的方法
        """
        while True:
            try:
                self.header_len_bytes = self.conn.recv(4)  # 接收4个字节的数据头信息
                if not self.header_len_bytes:
                    break
                msg = self.get_msg
                print(msg)
                method, args = msg.split(" ", 1)
                if not self.online and method != "login":
                    res_code = {"code": "2", "msg": "please login first!"}
                    self.send_code(res_code)
                elif hasattr(self, "_%s" % method.lower()) and args:
                    res_code = {"code": "0", "msg": "wait moment,it's working now"}
                    self.send_code(res_code)
                    func = getattr(self, "_%s" % method.lower())
                    func(args)
                else:
                    res_code = {"code": "1", "msg": "error request %s !" % msg}
                    self.send_code(res_code)
            except Exception as e:
                print(e)
                self.q.task_done()
                self.conn.close()
                break

    @classmethod
    def start(cls):
        """
        循环拿队列q里的链接，拿到一个实例化一个，然后启动comunication方法，开始和客户端交互
        """
        while True:
            conn = cls.q.get()
            client = Myserver(conn)
            client.comunication()

    @classmethod
    def create_thread(cls):
        '''
        开启多线程，线程数为settings设置的最大并发数
        '''
        for i in range(MAX_RUN):
            t = Thread(target=cls.start)
            t.daemon = True
            t.start()

    @classmethod
    def run(self):
        """
       启动，循环等链接，每来一个链接就赛到队列里
       """
        self.create_thread()
        while True:
            print("waiting for connection...")
            conn, client_addr = self.server_socket.accept()
            self.q.put(conn)


if __name__ == "__main__":
    Myserver.run()
