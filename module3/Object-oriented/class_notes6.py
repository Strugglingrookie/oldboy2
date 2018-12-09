# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 内置方法：


# # isinstance(obj,cls)检查是否obj是否是类 -cls 的对象
# class Foo(object):
#     pass
# obj = Foo()
# isinstance(obj, Foo)
#
# # issubclass(sub, super)检查sub类是否是 super 类的派生类
# class Foo(object):
#     pass
# class Bar(Foo):
#     pass
# issubclass(Bar, Foo)


# item 将对象变成一个字典形式
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):  # 当用字典形式查对象的属性时，会自动调用该方法
#         print("getitem ....")
#         return self.__dict__.get(item)
#
#     def __setitem__(self, key, value):  # 当用字典形式设置对象的属性时，会自动调用该方法
#         print("setitem ....")
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):  # 当用字典形式删除对象的属性时，会自动调用该方法
#         print("delitem ....")
#         self.__dict__.pop(key)
#
#
# a = A("xg")
# print(a["name"])
# a["sex"] = 'male'
# print(a["sex"])
# del a["sex"]
# print(a["sex"])


# __str__ 在print(对象) 的时候自动触发
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "这是类A"
#
#
# a = A("xg")
# print(a)  # 没有 __str__ 的时候打印的是 <__main__.A object at 0x10e883630> 有了后打印的是__str__里的return的内容


# __del__ 析构函数 对象被销毁的时候，自动触发，比如一些关闭数据库链接
class Open:
    def __init__(self,filename):
        print('open file.......')
        self.filename=filename

    def __del__(self):
        print('回收操作系统资源：self.close()')

f=Open('settings.py')
# del f #f.__del__()
print('----main------') #del f #f.__del__()