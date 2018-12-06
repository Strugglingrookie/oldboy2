# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:59
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.作业讲解.py
# @Software: PyCharm

# 场景 角色 类 —> 属性和方法
# 站在每个角色的角度上去思考程序执行的流程
import sys
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Student:
    operate_lst = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_courses(self):
        print('查看可选课程')

    def select_course(self):
        print('选择课程')

    def check_selected_course(self):
        print('查看已选课程')

    def exit(self):
        exit()

class Manager:
    operate_lst = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_courses'),
                   ('查看所有学生','show_students'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]
    def __init__(self,name):
        self.name = name

    def create_course(self):
        print('创建课程')

    def create_student(self):
        print('创建学生')

    def show_courses(self):
        print('查看所有课程')

    def show_students(self):
        print('查看所有学生')

    def show_student_course(self):
        print('查看所有学生的选课情况')

    def exit(self):
        exit()

# 学生 ： 登录就可以选课了
    # 有学生账号了
    # 有课程了

# 管理员 ：登录就可以完成以下功能
    # 学生的账号是管理员创建的
    # 课程也应该是管理员创建的

# 应该先站在管理员的角度上来开发
# 登录
# 登录必须能够自动识别身份
# 用户名|密码|身份
def login():
    name = input('username : ')
    pawd = input('password : ')
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify = line.strip().split('|')
            if usr == name and pawd == pwd:
                return {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}

ret = login()
if ret['result']:
    print('登录成功')
    if hasattr(sys.modules[__name__],ret['id']):
        cls = getattr(sys.modules[__name__],ret['id'])
        obj = cls(ret['name'])
        for id,item in enumerate(cls.operate_lst,1):
            print(id,item[0])
        func_str = cls.operate_lst[int(input('>>>')) - 1][1]
        print(func_str)
        if hasattr(obj,func_str):
            getattr(obj,func_str)()
else:
    print('登录失败')

    # if ret['id'] == 'Manager':
    #     obj = Manager(ret['name'])
    #     for id,item in enumerate(Manager.operate_lst,1):
    #         print(id,item[0])
    #     func_str = Manager.operate_lst[int(input('>>>')) - 1][1]
    #     if hasattr(obj,func_str):
    #         getattr(obj,func_str)()
    # elif ret['id'] == 'Student':
    #     obj = Student(ret['name'])
    #     for id,item in enumerate(Student.operate_lst,1):
    #         print(id,item[0])
    #     func_str = Student.operate_lst[int(input('>>>')) - 1][1]
    #     if hasattr(obj,func_str):
    #         getattr(obj,func_str)()