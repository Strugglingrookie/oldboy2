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
# class Animal:
#     def __init__(self,name,age,life,attack_value):
#         self.name = name
#         self.age = age
#         self.life = life
#         self.attack_value = attack_value
#
# class People(Animal):
#     def attack(self,dog):
#         dog.life -= self.attack_value
#         print("人打了狗，狗丢失生命值 %s " %self.attack_value)
#
#
# class Dog(Animal):
#     def attack(self, person):
#         person.life -= self.attack_value
#         print("狗咬了人，人丢失生命值 %s " % self.attack_value)
#
# p = People("xg",18,100,10)
# d = Dog("xiaobai",1,50,5)
# p.attack(d)
# print(p.life,d.life)
# p.attack(d)
# print(p.life,d.life)
# d.attack(p)
# print(p.life,d.life)

# 18.编写程序, 在元类中控制把自定义类的数据属性都变成大写.
# class Mymeta(type):
#     def __new__(cls,class_name,class_bases,class_dict):
#         for i,v in class_dict.items():
#             if not i.endswith("__") and isinstance(v,str):
#                 class_dict[i] = v.upper()
#         print(class_dict)
#         return type.__new__(cls,class_name ,class_bases, class_dict)
#
# class People(object,metaclass=Mymeta):
#     country = "china"
#
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):  # 对象加上括弧直接就调用这个方法
#         print("my name is %s"%self.name)
#         print("my am from %s"%self.country)
#
# print(People.__dict__)
# p1 = People("xg")
# print(p1.__dict__)

# 19.编写程序, 在元类中控制自定义的类无需init方法.

# 20.编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
# class Student:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Student.count += 1
# s1 = Student("xg")
# s2 = Student("xh")
# s3 = Student("xk")
# print(Student.count)

# 21.编写程序, A继承了B, 俩个类都实现了handle方法, 在A中的 handle 方法中调用 B 的 handle 方法
# class B:
#     def handle(self):
#         print("handle of B")
#
# class A(B):
#     def handle(self):
#         print("handle of A")
#         super().handle()
#
# a = A()
# a.handle()

# 22.编写程序, 如下有三点要求：
# 自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# e.g
# {
#     "egon": {"password": "123", 'status': False, 'timeout': 0},
#     "alex": {"password": "456", 'status': False, 'timeout': 0}
# }
# 定义用户类，定义方法db，例如执行obj.db可以拿到用户数据结构
# 在该类中实现登录、退出方法, 登录成功将状态(status)修改为True, 退出将状态修改为False(退出要判断是否处于登录状态).密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于10秒即不允许登录)
# import json,time
# class user:
#     def __init__(self):
#         self.users = self.db
#
#     @property
#     def db(self):
#         f = open("users.json","r")
#         res = json.load(f)
#         f.close()
#         return res
#
#     def login(self):
#         count = 3
#         while count > 0:
#             user = input("Your name :\n").strip()
#             pwd = input("Password :\n").strip()
#             if self.users.get(user) and pwd == self.users.get(user)["password"]:
#                 if self.users.get(user)["timeout"]+10 > time.time():
#                     print("您的账户已被锁定，请稍后再试！")
#                 else:
#                     print("欢迎%s登陆系统".center(50, "*") % user)
#                     self.users.get(user)["status"] = "True"
#                     break
#             else:
#                 if count == 1:
#                     print("错误次数达到3次，已被锁定".center(50, "*"))
#                     if self.users.get(user):
#                         self.users.get(user)["timeout"] = time.time()
#                         f = open("users.json", "w")
#                         json.dump(self.users,f)
#                         f.close()
#                 else:
#                     print("用户名或密码有误，请重新输入".center(50, "*"))
#                 count -= 1
#
#     def logout(self):
#         if self.users.get(user) and self.users.get(user)["status"] == "True":
#             self.users.get(user)["status"] = "False"
#             exit("退出程序！")
#         exit("退出登录！")
#
#     def run(self):
#         self.login()
#         self.logout()
#
# u = user()
# u.run()