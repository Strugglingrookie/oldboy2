# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/26 10:32
# @File   : settings.py


import os
from lib.log_write import Mylog
from lib.operate_db import MySql

EMAIL_INFO = {
    "user": "waznyyy@163.com",
    "host": "smtp.163.com",
    "password": "xg0304",
    # win系统发送邮件，附件中文乱码，设置encoding=gbk可解决
    "encoding": "gbk"
}

TO = ["295266301@qq.com"]

CS = ["3418666179@qq.com", "waznyyy@163.com"]

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(BASE_PATH, "cases")  # 查找用例的目录

DATA_PATH = os.path.join(BASE_PATH, 'data')  # 用例数据的目录
USER_INFO = os.path.join(DATA_PATH, "userinfo.txt")

REPORT_PATH = os.path.join(BASE_PATH, "report")

LOG_PATH = os.path.join(BASE_PATH, "logs", "utp.log")
LOG_LEVEL = 'info'
log = Mylog(LOG_PATH, LOG_LEVEL).get_logger()

HOSTS = {
    "test": "http://localhost:8080",
    "dev": "http://localhost:8080",
    "pre": "http://localhost:8080",
}

HOST = HOSTS.get('test')

DB_INFO = {
    "host": "localhost",
    "user": "root",
    "pwd": "123456",
    "dbname": "utp",
    "port": 3308,
    "charset": "utf8"
}
mysql = MySql(**DB_INFO)
