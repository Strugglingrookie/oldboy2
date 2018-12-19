# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8

'''
# 绑定方法  绑定给谁就给谁调用，调用时会自动将调用者作为第一个参数传递给函数
# 1.绑定到对象的方法(不被任何装饰器装饰的函数) 2.绑定到类的方法 @classmethod 装饰的函数
# 非绑定方法 没有自动传值的功能 @staticmethod
class A:
    def __init__(self, name):
        self.name = name

    def call(self):  # 绑定到对象的方法，对象调用时默认将调用者作为第一个参数自动传入，类也可调用，但只是作为一个普通函数给类用，不会自动传值。
        print("my name is %s" % self.name)

    @classmethod  # 绑定到类的方法，类调用时默认将调用者作为第一个参数自动传入，对象调用时默认将调用者所属的类作为第一个参数自动传入。
    def func_class(cls):  # 一般写成 cls 与绑定到对象时写的self做区分，两个功能其实是一样的
        print(cls)

    @staticmethod  # 类和对象都可以直接使用，当普通函数那样使用
    def cal(x, y):
        print(x+y)


a1 = A("xg")
# # 调用对象绑定方法
# a1.call()
# A.call(a1)
# # 调用类绑定方法
# A.func_class()
# a1.func_class()
# # 调用非绑定方法
# A.cal(1,2)
# a1.cal(1,2)

# 反射
# 对象的属性操作，实际做的增删改查就是操作对象的 __dict__属性字典 ， 类的属性操作类似
# 判断是否含有属性
print(hasattr(a1, "name"))  # true
# 拿到属性值
print(getattr(a1, "name"))  # 当不存在该属性时，会报错
print(getattr(a1, "asd", None))  # 指定None,当不存在该属性时，不会报错
# 设置属性值
setattr(a1, "sex", "male")
print(getattr(a1, "sex", None))
# 删除属性
delattr(a1, "sex")
print(getattr(a1, "sex", None))

# 反射的应用  类似于功能分发
class Service:
    def run(self):
        while True:
            inp=input('>>: ').strip() #cmd='get a.txt'
            cmds=inp.split() #cmds=['get','a.txt']

            # print(cmds)
            if hasattr(self,cmds[0]):
                func=getattr(self,cmds[0])
                func(cmds)


    def get(self,cmds):
        print('get.......',cmds)


    def put(self,cmds):
        print('put.......',cmds)


obj=Service()
obj.run()
'''

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