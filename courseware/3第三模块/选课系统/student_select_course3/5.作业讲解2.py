# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:59
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.作业讲解.py
# @Software: PyCharm

# 场景 角色 类 —> 属性和方法
# 站在每个角色的角度上去思考程序执行的流程
import os
import sys
import pickle
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Person:
    def show_courses(self):
        with open('course_info','rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    course_obj = pickle.load(f)
                    print(count,course_obj.name,course_obj.price,course_obj.period,course_obj.teacher)
                except EOFError:
                    break

class Student(Person):
    operate_lst = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def select_course(self):
        self.show_courses()
        num = int(input('num >>>'))   # 1
        count = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    course_obj = pickle.load(f)
                    if count == num:
                        self.courses.append(course_obj)
                        print('您选择了%s课程'%(course_obj.name))
                        break
                    count += 1
                except EOFError:
                    print('没有您选择的课程')
                    break

    def check_selected_course(self):
        for course in self.courses:
            print(course.name,course.teacher)

    def exit(self):
        with open('student_info','rb') as f1,open('student_info_bak','wb') as f2:
            while True:
                try:
                    student_obj = pickle.load(f1)
                    if student_obj.name == self.name:   # 如果从原文件找到了学生对象和我当前的对象是一个名字，就认为是一个人
                        pickle.dump(self,f2)             # 应该把现在新的学生对象写到文件中
                    else:
                        pickle.dump(student_obj, f2)     # 反之，应该原封不动的把学生对象写回f2
                except EOFError:
                    break
        os.remove('student_info')
        os.rename('student_info_bak','student_info')
        exit()

    @staticmethod
    def init(name):
        # 返回一个学生对象就行了
        # 学生对象在哪儿？ 在student_info文件里
        # 找到符合的对象之后 直接将load出来的对象返回
        with open('student_info','rb') as f:
            while True:
                try :
                    stu_obj = pickle.load(f)
                    if stu_obj.name == name:
                        return stu_obj
                except EOFError:
                    print('没有这个学生')
                    break
class Manager(Person):
    operate_lst = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_courses'),
                   ('查看所有学生','show_students'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]
    def __init__(self,name):
        self.name = name

    def create_course(self):
        name = input('course name : ')
        price = input('course price : ')
        period = input('course period : ')
        teacher = input('course teacher : ')
        course_obj = Course(name,price,period,teacher)
        with open('course_info','ab') as f:
            pickle.dump(course_obj,f)
        print('%s课程创建成功'%course_obj.name)

    def create_student(self):
        # 用户名和密码记录到userinfo文件，将学生对象存储在student_info文件
        stu_name =input('student name : ')
        stu_pwd =input('student password : ')
        stu_auth = '%s|%s|Student\n'%(stu_name,stu_pwd)
        stu_obj = Student(stu_name)
        with open('userinfo','a',encoding='utf-8') as f:
            f.write(stu_auth)
        with open('student_info','ab') as f:
            pickle.dump(stu_obj,f)
        print('%s学生创建成功'%stu_obj.name)

    def show_students(self):
        with open('student_info','rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    student_obj = pickle.load(f)
                    print(count,student_obj.name)
                except EOFError:
                    break

    def show_student_course(self):
        with open('student_info','rb') as f:
            while True:
                try:
                    student_obj = pickle.load(f)
                    course_name = [course.name for course in student_obj.courses]
                    print(student_obj.name,'所选课程%s'%'|'.join(course_name))
                except EOFError:
                    break

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        return cls(name)   # 管理员的对象

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
        obj = cls.init(ret['name'])   # 实例化
        while True:
            for id,item in enumerate(cls.operate_lst,1):
                print(id,item[0])
            func_str = cls.operate_lst[int(input('>>>')) - 1][1]
            print(func_str)
            if hasattr(obj,func_str):
                getattr(obj,func_str)()
else:
    print('登录失败')