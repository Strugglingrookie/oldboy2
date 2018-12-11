# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:42
# @Author  : Xiao


from src.group import Myclass
from src.school import Myschool
from src.teacher import Myteacher



def run():
    c = Myclass()
    t = Myteacher()
    s = Myschool()
    while True:
        choice = input("1.班级 2.教师 3.学校 your choice:\n")
        if choice == "1":
            c.myclass_operation()
        if choice == "2":
            t.teacher_operation()
        if choice == "3":
            s.myschool_operation()
        else:
            print(choice)
            exit("退出程序！")