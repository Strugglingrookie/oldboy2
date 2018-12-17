# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 13:50
# @Author  : Xiao


# 1.面向对象三大特性，各有什么用处，说说你的理解。
# 封装  封装数据在于提高数据的安全性，封装方法在于隔离复杂度。整体作用类似于函数的作用，调函数只关心结果，而不关心内部结构。
# 封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使用者只知道一个接口(函数)，参数不变。
# 继承  实现代码的重用
# 多态  增加了程序的灵活性，提高了程序的扩展性。

# 2.类的属性和对象的属性有什么区别?
# 类的属性在定义类的时候就生成了，就算不生成对象也可以用：
# 且类的数据属性只会存一份，不论实例化多少对象，指向的类数据属性都是同一个内存地址，函数属性有多少个对象则多少个内存地址
# 对象的属性，实在实例化的时候，类会初始化对象的数据属性，函数属性是类定义的。对象的数据属性只给对象自己调用。

# 3.面向过程编程与面向对象编程的区别与应用场景?
# 面向过程  将大问题细化成一个个小问题，再一个个小问题逐一解决，直到最后解决问题。
# 优点：复杂问题流程化，进而简单化 缺点：灵活性、扩展性很差
# 应用：应用在一些需求比较稳定的项目，还有日常的一些脚本、工具，着眼于快速解决一些小问题的，用面向过程。
# 定义：万物皆对象，对象就是特征于技能的集合（比如孙悟空，毛脸雷公嘴是特征，七十二变是技能）
# 优点：可扩展性强
# 缺点：编程复杂度高，极容易出现过度设计的问题，而且在一些扩展性要求低的场景使用面向对象会徒增编程难度
# 应用：实用于客户需求频繁变化，如互联网/游戏/企业应用

# 4.类和对象在内存中是如何保存的。
# 一切皆对象，和变量是一样的，都是有一变量名，指向一个内存地址。

# 5.什么是绑定到对象的方法、绑定到类的方法、解除绑定的函数、如何定义，如何调用，给谁用？有什么特性
# 绑定到对象的方法：指类中不被任何装饰器装饰的函数，给对象用的方法，对象调用会将调用者作为第一个参数传递给方法。
# 绑定到类的方法：指类中被 classmethod 修饰的函数，给类用的方法，类调用会将调用者作为第一个参数传递给方法。
# 解除绑定的函数：指类中被 staticmethod 修饰的函数，类和对象都可以调用，不会自动传值

# 6.使用实例进行 获取、设置、删除 数据, 分别会触发类的什么私有方法
#
#  class A(object):
#      pass
#
#  a = A()
#
#  a["key"] = "val"
#  a = a["key"]
#  del a["key"]
# __getitem__    __setitem__     __delitem__

# 7.python中经典类和新式类的区别
# 经典类  没有继承object  新式类 继承了object  python2中才有经典类，python3里全部默认继承object
# 区别 经典类，属性查找是深度优先  新式类：是广度优先

# 8.如下示例, 请用面向对象的形式优化以下代码
#    def exc1(host,port,db,charset,sql):
#        conn=connect(host,port,db,charset)
#        conn.execute(sql)
#        return xxx
#    def exc2(host,port,db,charset,proc_name)
#        conn=connect(host,port,db,charset)
#        conn.call_proc(sql)
#        return xxx
#    # 每次调用都需要重复传入一堆参数
#    exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
#    exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
# class operate_mysql:
#     def __init__(self,host,port,db,charset):
#         self.host = host
#         self.port = port
#         self.db = db
#         self.db = charset
#         self.conn = connect(self.host,self.port,self.db,self.charset)
#
#     def exc1(self,sql):
#         res = self.conn.execute(sql)
#         return res
#
#     def exc2(self, sql):
#         res = self.conn.call_proc(sql)
#         return res
#
# mysql = operate_mysql('127.0.0.1',3306,'db1','utf8')
# mysql.exc1('select * from tb1;')
# mysql.exc2('存储过程的名字;')

# 9.示例1, 现有如下代码， 会输出什么：
#
# class People(object):
#   __name = "luffy"
#   __age = 18
#
# p1 = People()
# print(p1.__name, p1.__age)
# 报错，隐藏属性不可以这样访问，需要改成print(p1._People__name, p1._People__age)才可以访问

# 10示例2, 现有如下代码， 会输出什么：
# class People(object):
#
#    def __init__(self):
#        print("__init__")
#
#    def __new__(cls, *args, **kwargs):
#        print("__new__")
#        return object.__new__(cls, *args, **kwargs)
#
# p = People()
# print(p)
# 首先打印 __init__ ，然后打印 __new__  ，返回一个对象

# 11.请简单解释Python中 staticmethod（静态方法）和 classmethod（类方法）, 并分别补充代码执行下列方法。
# staticmethod（静态方法） 不会自动传值   classmethod（类方法）类或对象调用时，会自动将类作为第一个参数传递
# class A(object):
#
#    def foo(self, x):
#        print("executing foo(%s, %s)" % (self,x))
#
#    @classmethod
#    def class_foo(cls, x):
#        print("executing class_foo(%s, %s)" % (cls,x))
#
#    @staticmethod
#    def static_foo(x):
#        print("executing static_foo(%s)" % (x))
#
# a = A()
# A.foo(A,"qwe")
# a.foo("rty")
# A.class_foo(123)
# a.class_foo(456)
# A.static_foo("abc")
# a.static_foo("efg")

# 12.请执行以下代码，解释错误原因，并修正错误。
# class Dog(object):
#
#    def __init__(self,name):
#        self.name = name
#
#    @property
#    def eat(self):
#        print(" %s is eating" %self.name)
#
# d = Dog("ChenRonghua")
# d.eat()
# property装饰的方法是私有属性方法，它是将一个函数属性变成数据属性(不同的是这种属性不可修改变量值)，调用改成d.eat即可。

# 13.下面这段代码的输出结果将是什么？请解释。
# class Parent(object):
#    x = 1
#
# class Child1(Parent):
#    pass
#
# class Child2(Parent):
#    pass
#
# print(Parent.x, Child1.x, Child2.x)  # 输出 1    1    1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x) # 输出 1    2    1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x) # 输出 3    2    3
# # 1 1 1 继承自父类的类属性x，所以都一样，指向同一块内存地址
# # 1 2 1 更改Child1，Child1的x指向了新的内存地址
# # 3 2 3 更改Parent，Parent的x指向了新的内存地址

# 14.多重继承的执行顺序，请解答以下输出结果是什么？并解释。
class A(object):
   def __init__(self):
       print('A')
       super(A, self).__init__()

class B(object):
   def __init__(self):
       print('B')
       super(B, self).__init__()

class C(A):
   def __init__(self):
       print('C')
       super(C, self).__init__()

class D(A):
   def __init__(self):
       print('D')
       super(D, self).__init__()

class E(B, C):
   def __init__(self):
       print('E')
       super(E, self).__init__()

class F(C, B, D):
   def __init__(self):
       print('F')
       super(F, self).__init__()

class G(D, B):
   def __init__(self):
       print('G')
       super(G, self).__init__()

if __name__ == '__main__':
   g = G()  # G D A B
   f = F()  # F C B D A