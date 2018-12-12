# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 14:28
# @Author  : Xiao


from src.teacher import Myteacher
from src.student import Mystudent


teacher = Myteacher()
student = Mystudent()
stus = student.stus
teachers = teacher.teachers
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