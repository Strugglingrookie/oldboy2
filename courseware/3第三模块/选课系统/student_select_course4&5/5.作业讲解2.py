# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:59
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.作业讲解.py
# @Software: PyCharm

import os
import sys
import pickle

student_info = 'student_info'
course_info = 'course_info'
userinfo = 'userinfo'
class Base:
    def __str__(self):
        return self.name
class Course(Base):
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher
    def __repr__(self):
        return ' '.join([self.name, self.price, self.period, self.teacher])

class Person:
    @staticmethod
    def get_from_pickle(path):
        with open(path,'rb') as f:
            while True:
                try :
                    stu_obj = pickle.load(f)
                    yield stu_obj
                except EOFError:
                    break

    def show_courses(self):
        for count,course in enumerate(self.get_from_pickle(course_info),1):
            print(count,repr(course))

    def dump_obj(self,path,obj):
        with open(path,'ab') as f:
            pickle.dump(obj,f)

class Student(Person,Base):
    operate_lst = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def __repr__(self):
        # course_name = [course.name for course in self.courses]
        course_name = [str(course) for course in self.courses]
        return '%s %s'%(self.name,'所选课程%s' % '|'.join(course_name))

    def select_course(self):
        self.show_courses()
        num = int(input('num >>>'))
        for count,course in enumerate(self.get_from_pickle(course_info),1):
            if count == num:
                self.courses.append(course)
                print('您选择了%s课程' % (course))
                break
        else:print('没有您要找的课程')

    def check_selected_course(self):
        for course in self.courses:
            print(course.name,course.teacher)

    def exit(self):
        with open(student_info+'_bak', 'wb') as f2:
            for stu in self.get_from_pickle(student_info):
                if stu.name == self.name:  # 如果从原文件找到了学生对象和我当前的对象是一个名字，就认为是一个人
                    pickle.dump(self, f2)  # 应该把现在新的学生对象写到文件中
                else:
                    pickle.dump(stu, f2)  # 反之，应该原封不动的把学生对象写回f2
        os.remove(student_info)
        os.rename(student_info+'_bak',student_info)
        exit()

    @classmethod
    def init(cls,name):
        for stu in cls.get_from_pickle(student_info):
            if stu.name == name:
                return stu
        else:print('没有这个学生')

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
        self.dump_obj(course_info, course_obj)
        print('%s课程创建成功'%course_obj.name)

    def create_student(self):
        # 用户名和密码记录到userinfo文件，将学生对象存储在student_info文件
        stu_name =input('student name : ')
        stu_pwd =input('student password : ')
        stu_auth = '%s|%s|Student\n'%(stu_name,stu_pwd)
        stu_obj = Student(stu_name)
        with open(userinfo,'a',encoding='utf-8') as f:
            f.write(stu_auth)
        self.dump_obj(student_info, stu_obj)
        print('%s学生创建成功'%stu_obj.name)

    def show_students(self):
        for count,stu in enumerate(self.get_from_pickle(student_info),1):
            print(count,stu)

    def show_student_course(self):
        for stu in self.get_from_pickle(student_info):
            print(repr(stu))

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        return cls(name)   # 管理员的对象

def login():
    name = input('username : ')
    pawd = input('password : ')
    with open(userinfo,encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify = line.strip().split('|')
            if usr == name and pawd == pwd:
                return {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}

ret = login()
if ret['result']:
    print('\033[1;32;40m登录成功\033[0m')
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