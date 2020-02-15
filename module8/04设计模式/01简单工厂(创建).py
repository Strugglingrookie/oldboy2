# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 21:41
# @File   : 01简单工厂(创建).py


'''
创建型模式（即创建对象的模式）：
工厂方法模式、抽象工厂模式、创建者模式、单例模式

工厂方法模式：
不直接向客户端暴露对象创建的实现细节，
而是通过一个工厂类来负责创建产品类的实例。

角色：
工厂角色（Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）

优点：
隐藏了对象创建的实现细节
客户端不需要修改代码
缺点：
违反了单一职责原则，将创建逻辑几种到一个工厂类里
当添加新产品时，需要修改工厂类代码，违反了开闭原则
'''

from abc import ABCMeta, abstractmethod


# 抽象产品角色
class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass

# 具体产品角色
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huaei = use_huabei

    def pay(self, money):
        if self.use_huaei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额支付%d元." % money)


# 具体产品角色
class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


# 工厂角色
class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError("No such payment named %s" % method)



# client
pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)