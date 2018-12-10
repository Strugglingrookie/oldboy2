# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/6


# 练习1：编写一个学生类，产生一堆学生对象， (5分钟)
# 要求：
# 有一个计数器（属性），统计总共实例了多少个对象
# class student:
#     school = "haerbin"
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         student.count  += 1
#
# stu1 = student("stu1")
# stu2 = student("stu2")
# print(stu1.count)
# stu3 = student("stu3")
# print(student.count)

# 练习2：模仿王者荣耀定义两个英雄类， (10分钟)
# 要求：
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。

# class hero:
#
#     def __init__(self,name,attack_value,life_value):
#         self.name = name
#         self.attack_value = attack_value
#         self.life_value = life_value
#
#     def attack(self,other):
#         if self.life_value < 0:
#             print("您已经死亡，不可再发起攻击！")
#         elif other.life_value < 0:
#             print("%s 已经死亡，不可再发起攻击！"%other.name)
#         else:
#             other.life_value -= self.attack_value
#             print("您攻击了 %s，损失生命值 %s"%(other.name,self.attack_value))
#
# a = hero("a",10,30)
# b = hero("b",10,30)
# a.attack(b)
# a.attack(b)
# a.attack(b)
# a.attack(b)
# a.attack(b)
# b.attack(a)

# 练习一：在元类中控制把自定义类的数据属性都变成大写
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
#
# p1()

#  练习二：在元类中控制自定义的类无需init方法
# 1.元类帮其完成创建对象，以及初始化操作；
# 2.要求实例化时传参必须为关键字形式，否则抛出异常TypeError: must use keyword argument
# 3.key作为用户自定义类产生对象的属性，且所有属性变成大写
# class Mymetaclass(type):
#     # def __new__(cls,name,bases,attrs):
#     #     update_attrs={}
#     #     for k,v in attrs.items():
#     #         if not callable(v) and not k.startswith('__'):
#     #             update_attrs[k.upper()]=v
#     #         else:
#     #             update_attrs[k]=v
#     #     return type.__new__(cls,name,bases,update_attrs)
#
#     def __call__(self, *args, **kwargs):
#         if args:
#             raise TypeError('must use keyword argument for key function')
#         obj = object.__new__(self) #创建对象，self为类Foo
#
#         for k,v in kwargs.items():
#             obj.__dict__[k.upper()]=v
#         return obj
#
# class Chinese(metaclass=Mymetaclass):
#     country='China'
#     tag='Legend of the Dragon' #龙的传人
#     def walk(self):
#         print('%s is walking' %self.name)
#
#
# p=Chinese(name='egon',age=18,sex='male')
# print(p.__dict__)

