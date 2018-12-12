# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 14:28
# @Author  : Xiao


from src.tools import read_datas
from config.settings import MYTEACHER_FILE
from config.settings import MYSTUDENT_FILE


stus = read_datas(MYSTUDENT_FILE)
teachers = read_datas(MYTEACHER_FILE)
teachers.update(stus)

def login_func():
    while True:
        user_id = input("请输入您的账号: \n").strip()
        pwd = input("请输入您的密码: \n" ).strip()
        if teachers.get(user_id) and pwd == teachers.get(user_id).get("pwd"):
            print("欢迎 %s 登陆系统" % user_id)
            role = teachers.get(user_id).get("role")
            return user_id,role
        else:
            print("账号或密码错误！")

