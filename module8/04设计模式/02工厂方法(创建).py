# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 22:10
# @File   : 02工厂方法(创建).py


'''
简单工厂模式的两个缺点：
违反了单一职责原则，将创建逻辑几种到一个工厂类里
当添加新产品时，需要修改工厂类代码，违反了开闭原则

为了解决上述缺点，就有了工厂方法模式
内容：定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
角色：
抽象工厂角色（Creator）
具体工厂角色（Concrete Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）

优点：
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
隐藏了对象创建的实现细节
缺点：
每增加一个具体产品类，就必须增加一个相应的具体工厂类
'''

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huaei = use_huabei

    def pay(self, money):
        if self.use_huaei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


class BankPay(Payment):
    def pay(self, money):
        print("银行卡支付%d元." % money)


# 抽象工厂角色（Creator）
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# 具体工厂角色（Concrete Creator）
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


# 具体工厂角色（Concrete Creator）
class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


# 具体工厂角色（Concrete Creator）
class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


# 具体工厂角色（Concrete Creator）
class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# client

pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)
