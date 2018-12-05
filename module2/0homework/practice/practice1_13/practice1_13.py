# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/30


# 1.logging模块有几个日志级别？
#debug info warning error critical

# 2.请配置logging模块，使其在屏幕和文件里同时打印以下格式的日志
#   2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts
# import logging
# from logging import handlers
# logger = logging.getLogger("my_practice")
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# fh = logging.FileHandler("practice_test.log")
# # fh = handlers.RotatingFileHandler("practice_test.log",maxBytes=10,backupCount=3)
# # fh = handlers.TimedRotatingFileHandler("practice_test.log",when="S",interval=5,backupCount=3)
# fh.setLevel(logging.DEBUG)
# logger.addHandler(ch)
# logger.addHandler(fh)
# ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelno)s - %(lineno)s - %(message)s')
# ch.setFormatter(ch_formatter)
# fh.setFormatter(fh_formatter)
#
# class IgnoreSmall(logging.Filter):
#     def filter(self, record):
#         return "small" not in record.msg
# ch.addFilter(IgnoreSmall())
#
# logger.debug("what a big debug!!!")
# logger.info("what a big info!!!")
# logger.warning("what a big warning!!!")
# logger.error("what a small error!!!")
# logger.critical("what a big critical!!!")

# 3.json、pickle、shelve三个区别是什么？
# json:在python里只支持int str list tuple dict,体积小(占用内存小)，所有语言通用
# pickle:支持所有python数据类型，体积大，只能python用
# shelve:上面两种统一个文件只能支持一种python数据类型，shelve可以支持一个文件多个k,v，可以是任意python数据类型。但是也只能python用。

# 4.json的作用是什么？
# 使各种语言的数据类型转换成字符串存到硬盘或者通过网络传输给其他语言，使语言间无障碍通信。

# 5.subprocess执行命令方法有几种？
import subprocess
# res = subprocess.run(["df",'-h'],stdout=subprocess.PIPE,stderr=subprocess.PIPE) #执行命令，并返回运行结果
# res = subprocess.run("df -h|grep disk1s4",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True) #执行复杂shell命令，并返回运行结果
#call方法和run方法类似，一般用run方法
#在后台执行复杂shell命令，不影响python的主程序运行，并返回运行结果，返回的结果是一个对象，需要获取stdout,然后用read方法读取
# res = subprocess.Popen("df -h|grep disk1s4",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# res = subprocess.Popen("sleep 10",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# print(res.pid)
# res.kill()
# res.terminate()
# print(res.stdout.read())

# 6.为什么要设计好目录结构？
# 项目层次清晰，便于阅读/维护

# 7.打印出命令行的第一个参数。例如：
#   python argument.py luffy
#   打印出 luffy
# import sys
# args = sys.argv
# if len(args)>1:
#     print(args[1])

# 8.代码如下：
# '''
# Linux当前目录/usr/local/nginx/html/
# 文件名：index.html
# '''
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(index.html)))
# print(BASE_DIR)
# 打印的内容是什么？
# os.path.dirname和os.path.abspath含义是什么？
# 打印 /usr/local/nginx/
# os.path.dirname 得到的是当前文件或文件夹所在的目录   os.path.abspath得到的文件的绝对目录

# 9.通过configparser模块完成以下功能
# 文件名my.cnf
# [DEFAULT]
# [client]
# port = 3306
# socket = /data/mysql_3306/mysql.sock
# [mysqld]
# explicit_defaults_for_timestamp = true
# port = 3306
# socket = /data/mysql_3306/mysql.sock
# back_log = 80
# basedir = /usr/local/mysql
# tmpdir = /tmp
# datadir = /data/mysql_3306
# default-time-zone = '+8:00'
# 修改时区 default-time-zone = '+8:00' 为 校准的全球时间 +00:00
# 删除 explicit_defaults_for_timestamp = true
# 为DEFAULT增加一条 character-set-server = utf8
# import configparser
# config = configparser.ConfigParser()
# config.read("my.cnf")
# config["mysqld"]["default-time-zone"] = "+00:00"
# config.remove_option("mysqld","explicit_defaults_for_timestamp")
# config["DEFAULT"]["character-set-server"] = "utf8"
# config.write(open("my.cnf","w"))

# 10.写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母.
# import string,random
# def get_confirm(n):
#     lis = []
#     while n>0:
#         res = []
#         res.append(str(random.randint(0,9)))
#         res.append(random.choice(string.ascii_lowercase))
#         res.append(random.choice(string.ascii_uppercase))
#         res.extend(random.sample((string.ascii_letters+string.digits),3))
#         random.shuffle(res)
#         new = "".join(res)
#         if new not in lis:
#             lis.append(new)
#             n -= 1
#     return lis
# print(get_confirm(5))

# 11.利用正则表达式提取到 luffycity.com ，内容如下
val = '''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>luffycity.com</title>
</head>
<body>
</body>
</html>'''
# import re
# res = re.findall("[a-z]{9}\.com",val)
# print(res)

# 12.写一个用户登录验证程序，文件如下
# 1234.json
# {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# 用户名为json文件名，密码为 password。
# 判断是否过期，与expire_date进行对比。
# 登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
# import json,os,time
# f = open("1234.json","r+")
# user_dic = json.load(f)
# username = os.path.splitext("1234.json")[0]
# pwd = user_dic["password"]
# invalid_time = user_dic["expire_date"]
# invalid_time_stamp = time.mktime(time.strptime(invalid_time,"%Y-%m-%d"))
# n = 0
# while n < 3:
#     user = input("your name:")
#     password = input("your password:")
#     if time.time() > invalid_time_stamp :
#         exit("账号已过期！")
#     if user_dic['status'] == 1:
#         exit("账号已锁定！")
#     if user == username and pwd == password:
#         print("欢迎登系统！")
#         break
#     n += 1
#     if n == 3:
#         print("登陆次数用尽，账户已锁定！")
#         user_dic['status'] = 1
#         f.seek(0)
#         f.truncate()
#         json.dump(user_dic,f)
# f.close()

# 13.把第12题三次验证的密码进行hashlib加密处理。即：json文件保存为md5的值，然后用md5的值进行验证。
# import hashlib,json,os,time
# def get_md5(val):
#     m = hashlib.md5()
#     m.update(b"abc")
#     return m.hexdigest()
# f = open("1234.json","r+")
# user_dic = json.load(f)
# username = os.path.splitext("1234.json")[0]
# pwd = user_dic["password"]
# invalid_time = user_dic["expire_date"]
# invalid_time_stamp = time.mktime(time.strptime(invalid_time,"%Y-%m-%d"))
# n = 0
# while n < 3:
#     user = input("your name:")
#     password = get_md5(input("your password:"))
#     if time.time() > invalid_time_stamp :
#         exit("账号已过期！")
#     if user_dic['status'] == 1:
#         exit("账号已锁定！")
#     if user == username and pwd == password:
#         print("欢迎登系统！")
#         break
#     n += 1
#     if n == 3:
#         print("登陆次数用尽，账户已锁定！")
#         user_dic['status'] = 1
#         f.seek(0)
#         f.truncate()
#         json.dump(user_dic,f)
# f.close()