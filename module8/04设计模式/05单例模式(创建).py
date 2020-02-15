# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 22:35
# @File   : 05单例模式(创建).py


'''
内容：保证一个类只有一个实例，并提供一个访问它的全局访问点。
角色：
单例（Singleton）
优点：
对唯一实例的受控访问
单例相当于全局变量，但防止了命名空间被污染
'''


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父方法object来生成一个实例
            cls._instance = super().__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)

print(a.a)  # 20
print(b.a)  # 20
print(id(a), id(b))
# 2444210899432 2444210899432
