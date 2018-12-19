# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 隐藏属性
'''
# 申明类时，数据属性或者函数属性，在属性名称前加上两个下划线，就实现了属性隐藏，但在python里不存在绝对的隐藏，它只是在申明的时候定义了它的调用方式。
class A:
    __country = "china"

    def __def(self):
        print(self.__country)


a = A()
print(a.__country)  # 报错，这是隐藏属性
print(a._A__country)  # 对的，python里不会绝对隐藏，只是在类命名的时候定义了新的访问方式，需要在隐藏变量名前加 "_类名" 就可以访问
print(A.__dict__)  # 可以看到在类A的属性字典里有一个kv是'_A__country': 'china'，隐藏的函数属性也一样的道理

# 当然python只是没有绝对隐藏，但是如果加上了隐藏属性，一般不会像上面那样去访问，那这个有什么用呢？
# 1.防止属性被改写   2.防止类内部在调用属性的时候调用到别的类的属性
class A:
    def func1(self):
        print("i am func1 from A")

    def __func2(self):
        print("i am func2 from A")

    def func3(self):
        print("i am func3 from A")
        self.func1()  # b调用时，这里实际是 b.func1(),那么他先会在B类里找func1，所以这里会打印("i am func1 from B")
        self.__func2()  # b调用时，这里实际是 b._A__func1(),那么找到的就是A类里的__func2，所以这里会打印("i am func2 from A")


class B(A):
    def func1(self):
        print("i am func1 from B")

    def __func2(self):  # 这里并不是改写父类A的__func2,因为这里已经变成了，_B__func2
        print("i am func2 from A")


b = B()
b.func3()
'''
'''
#一：封装数据属性：明确的区分内外，控制外部对隐藏的属性的操作行为
# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print('Name:<%s> Age:<%s>' %(self.__name,self.__age))
#
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             print('名字必须是字符串类型')
#             return
#         if not isinstance(age,int):
#             print('年龄必须是数字类型')
#             return
#         self.__name=name
#         self.__age=age
#
# p=People('egon',18)
#
# # p.tell_info()
#
# # p.set_info('EGON',38)
# # p.tell_info()
#
# # p.set_info(123,38)
# p.set_info('egon','38')
# p.tell_info()


#二、 封装方法：隔离复杂度
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a = ATM()
a.withdraw()
'''
# property 将函数属性变成数据属性，但只是像数据属性，并不是真的数据属性，在重新赋值的时候会报错。


class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


p=People('xg',60,168)
# print(p.bmi)
# p.bmi=3333 #报错AttributeError: can't set attribute

# 但是有一些方法可以修改和删除这些属性。


class A:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):  # 修改被property装饰的函数属性，直接 a.name = new_name 即可
        self.__name = name

    @name.deleter
    def name(self):  # 删除 a.name ,直接 del a.name 即可
        print("不可以删除")


a = A("xg")
print(a.name)
a.name = "XG"
print(a.name)
del a.name
print(a.name)

