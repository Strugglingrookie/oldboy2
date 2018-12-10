# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 16:31
# @Author  : Xiao


# 15.请编写一段符合多态特性的代码.
'''
import abc
class A(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def call(self):
        pass

class B(A):
    def __init__(self,name):
        self.name = name

    def call(self):
        print("%s 是这样叫的 喂喂喂" % self.name)


class C(A):
    def __init__(self,name):
        self.name = name

    def call(self):
        print("%s 是这样叫的 汪汪汪" % self.name)

b = B("xg")
c = C("xiaobai")
b.call()
c.call()
'''

# 16.很多同学都是学会了面向对象的语法，却依然写不出面向对象的程序，原因是什么呢？原因就是因为你还没掌握一门面向对象设计利器，即领域建模，请解释下什么是领域建模，以及如何通过其设计面向对象的程序？
# http://www.cnblogs.com/alex3714/articles/5188179.html 此blog最后面有详解
# 需求所涉及的领域的一个建模,更通俗的讲法是业务模型。
# 找名词 加属性 连关系

# 17.请写一个小游戏，人狗大站，2 个角色，人和狗，游戏开始后，生成2个人，3 条狗，互相混战，人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。注意，请按题14领域建模的方式来设计类。
# people name sex age life attack_value
# dog name life attack_value
# 人打了狗 攻击力10，狗掉血 10
# 狗咬了人 攻击力5，人掉血 5
# 关系  人大狗   狗咬人
class People:
    def __init__(self,name,age,life,attack_value):
        self.name = name

# 18.编写程序, 在元类中控制把自定义类的数据属性都变成大写.

# 19.编写程序, 在元类中控制自定义的类无需init方法.

# 20.编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.

# 21.编写程序, A继承了B, 俩个类都实现了handle方法, 在A中的 handle 方法中调用 B 的 handle 方法

# 22.编写程序, 如下有三点要求：
# 自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# e.g
# {
#     "egon": {"password": "123", 'status': False, 'timeout': 0},
#     "alex": {"password": "456", 'status': False, 'timeout': 0},
# }
# 定义用户类，定义方法db，例如
# 执行obj.db可以拿到用户数据结构
# 在该类中实现登录、退出方法, 登录成功将状态(status)
# 修改为True, 退出将状态修改为False(退出要判断是否处于登录状态).密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于10秒即不允许登录)

# 23.用面向对象的形式编写一个老师角色, 并实现以下功能, 获取老师列表, 创建老师、删除老师、创建成功之后通过
# pickle
# 序列化保存到文件里，并在下一次重启程序时能
# 读取到创建的老师, 例如程序目录结构如下.
# .
# | -- bin /
# | | -- main.py
# 程序运行主体程序(可进行菜单选择等)
# | -- config /
# | | -- settings.py
# 程序配置(例如: 配置存储创建老师的路径相关等)
# | -- db
# 数据存储(持久化, 使得每次再重启程序时, 相关数据对应保留)
# | | -- teachers / 存储所有老师的文件
# | | -- ......
# | -- src / 程序主体模块存放
# | | -- __init__.py
# | | -- teacher.py
# 例如: 实现老师相关功能的文件
# | | -- group.py
# 例如: 实现班级相关的功能的文件
# | -- manage.py
# 程序启动文件
# | -- README.md
# 程序说明文件

# 24.根据23题, 再编写一个班级类, 实现以下功能, 创建班级, 删除班级, 获取班级列表、创建成功之后通过
# pickle
# 序列化保存到文件里，并在下一次重启程序时能
# 读取到创建的班级.

# 25.根据23 题, 编写课程类, 实现以下功能, 创建课程(创建要求如上), 删除课程, 获取课程列表

# 26.根据23题, 编写学校类, 实现以下功能, 创建学校, 删除学校, 获取学校列表

# 27.通过23题, 它们雷同的功能, 是否可以通过继承的方式进行一些优化
# 伪代码
# class Behavior(object):
#     def fetch(self, keyword):
#         通过
#         keyword
#         参数
#         查询出对应的数据列表
# class School(Behavior):
#     pass
#
#
# class Teacher(Behavior):
#     pass
#
#
# s = School()
# t = Teacher()
#
# s.fetch("school")
# t.fetch("teacher")