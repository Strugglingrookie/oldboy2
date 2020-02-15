# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 23:13
# @File   : 06适配器(结构).py


'''
结构型模式（控制多个类组成一种结构，多个类协同工作）：
适配器模式、桥模式、组合模式、外观模式、代理模式

适配器模式：
内容：将一个类的接口转换成客户希望的另一个接口。
适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

两种实现方式：
类适配器：使用多继承
对象适配器：使用组合

角色：
目标接口（Target）
待适配的类（Adaptee）
适配器（Adapter）

适用场景：
想使用一个已经存在的类，而它的接口不符合你的要求
（对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。
'''

from abc import ABCMeta, abstractmethod


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


class BankPay:
    def cost(self, money):
        print("银联支付%d元." % money)


class ApplePay:
    def cost(self, money):
        print("苹果支付%d元." % money)


# # 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(BankPay())
p.pay(100)

# 组合

# class A:
#     pass
#
# class B:
#     def __init__(self):
#         self.a = A()
