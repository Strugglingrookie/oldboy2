# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/26 10:32
# @File   : settings.py


import os
import faker
from lib.log_write import Mylog

EMAIL_INFO = {
    "user": "waznyyy@163.com",
    "host": "smtp.163.com",
    "password": "xg0304",
    # win系统发送邮件，附件中文乱码，设置encoding=gbk可解决
    "encoding": "gbk"
}

QQ_EMAIl = {
    "user": "3418666179@qq.com",
    "host": "smtp.qq.com",
    "password": "123",
    # win系统发送邮件，附件中文乱码，设置encoding=gbk可解决
    "encoding": "gbk"
}

TO = ["295266301@qq.com"]

CS = ["3418666179@qq.com", "waznyyy@163.com"]

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(BASE_PATH, "test_case")

REPORT_PATH = os.path.join(BASE_PATH, "report")

WEB_PICTURE_PATH = os.path.join(REPORT_PATH,'picture')

APP_PATH = os.path.join(BASE_PATH, 'conf', 'appController.yml')

APP_REPORT = os.path.join(BASE_PATH, 'report', '{}')

APP_PICTUREPATH = os.path.join(BASE_PATH, 'report','app_picture', '{}')

# 生成报告时的地址
APP_ERROR = '../report/app_picture/{}/'

LOG_DIR = os.path.join(BASE_PATH, "log")
LOG_PATH = os.path.join(LOG_DIR, "server.log")
LOG_LEVEL = 'debug'
logger = Mylog(LOG_PATH, LOG_LEVEL).get_logger()

# 用于参数化
f = faker.Faker(locale="zh-CN")

PARAMS_MAP = {
    "<card>": f.ssn,
    "<phone>": f.phone_number,
    "<email>": f.email,
    "<name>": f.name,
    "<password>": f.password,
    "<bankcard>": f.credit_card_number,
    "<money>": f.random_int,
    "<address>": f.address
}


