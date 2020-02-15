# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 21:14
# @File   : 00设计原则.py


'''
接口：若干抽象方法的集合。
作用：限制实现接口的类必须按照接口给定的调用方式实现这些方法；
对高层模块隐藏了类的内部实现。

面向对象设计SOLID原则:
开放封闭原则：
一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。
即软件实体应尽量在不修改原有代码的情况下进行扩展。

里氏替换原则：
所有引用父类的地方必须能透明地使用其子类的对象。

依赖倒置原则：
高层模块不应该依赖低层模块，二者都应该依赖其抽象；
抽象不应该依赖细节；细节应该依赖抽象。
换言之，要针对接口编程，而不是针对实现编程。

接口隔离原则：
使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口。

单一职责原则：
不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。 
'''
#
# 设计模式在这里介绍以下几种
#
# 创建型模式（4种）：
# 工厂方法模式、抽象工厂模式、创建者模式、单例模式
#
# 结构型模式（5种）：
# 适配器模式、桥模式、组合模式、外观模式、代理模式
#
# 行为型模式（4种）：
# 责任链模式、观察者模式、策略模式、模板方法模式


from abc import ABCMeta, abstractmethod


# 接口
class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


p = WechatPay()
p.pay(100)


class User:
    def show_name(self):
        pass


class VIPUser(User):
    def show_name(self):
        pass


def show_user(u):
    res = u.show_name()


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")


class Frog(LandAnimal, WaterAnimal):
    pass
