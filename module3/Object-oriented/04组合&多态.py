# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 组合 ：对象1的属性是对象2，对象1就拥有了对象2的数据和函数属性，这就是组合
'''
# A类型和B类型没有共性，不可以继承，但是A有B的特性，比如A是人，B是家，A和B没有继承关系，但是人有家，A有B的关系，那么就可以把B的属性都给A用
class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("hi my name is %s"%self.name)


class home:
    def __init__(self,adress,area,height):
        self.adress = adress
        self.area = area
        self.heaight = height

    def home_info(self):
        print("地址：%s，面积：%s"%(self.adress,self.area))


xg = people("晓钢",18)
hourse = home("地球",1000,10)
xg.hourse = hourse
xg.hourse.home_info()  #地址：地球，面积：1000
'''

# 抽象类：抽取一些类的共性作为一个类，比如水果类，人类。抽象类能被继承，但是不能被实例化。
# 当函数属性用装饰器abc.abstractmethod装饰的时候，子类必须按照抽象类的定义实现这个固定的函数属性，否则报错。
'''
import abc #需要用到abc这个模块来定义抽象类


class animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod  #abc.abstractmethod 装饰后，该类的所有子类必须含有该方法才不会报错
    def run(self):
        print("people is running!")

    def sleep(self):
        pass

class people(animal):
    def run(self):  #必须定义run方法才可以,否则报错
        pass
'''

#多态：同一类事物的多种形态
'''
import abc


class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod  
    def talk(self): # animal的所有子类都必须实现talk方法，否则报错
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

class Cat(Animal): #动物的形态之三:猫
    def talk(self):
        print('say miamiao')

#多态性：指的是可以在不考虑对象的类型的情况下而直接使用对象方法  从而扩展性高
peo1=People()
dog1=Dog()
pig1=Pig()
cat1=Cat()

# peo1.talk()
# dog1.talk()
# pig1.talk()

def func(animal):
    animal.talk()
    
func(peo1)
func(pig1)
func(dog1)
func(cat1)
'''

# 鸭子类型  不同类定义的函数或者数据属性名字相同，不同对象在调用这些属性时，看上去都是一样的属性，实现功能也一样，但内部代码逻辑并不一样。


class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Text:
    def read(self):
        print('text read')

    def write(self):
        print('text write')

# f=open(...)
# f.read()
# f.write()

disk=Disk()
text=Text()

disk.read()
disk.write()

text.read()
text.write()
#
# #序列类型：列表list，元祖tuple，字符串str
#
l=list([1,2,3])
t=tuple(('a','b'))
s=str('hello')
#
# # print(l.__len__())
# # print(t.__len__())
# # print(s.__len__())
#
# # def len(obj):
# #     return obj.__len__()

print(len(l))
print(len(t))
print(len(s))
