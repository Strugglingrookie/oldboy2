# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/02


import os,sys

from conf.settings import USER_BANK_FILE
from core.log_write import user_logger,bank_logger
from core.login import json_func,check_online

users_atm = json_func(USER_BANK_FILE)

def check_amount(amount):
    if not amount.isdigit() or not(float(amount) > 0):
        return False
    return float(amount)

def check_user(user):
    if user in users_atm:
        return True

def check_user_amount(user,amount):
    if users_atm[user]["usable"] < amount:
        return False
    return True

def check_user_status(func):
    def wrapper(*args,**kwargs):
        user = args[0]
        if users_atm[user]["status"] == 1:
            return func(*args,**kwargs)
        user_logger.info("%s 账户已被冻结，不可进行此次操作，请联系管理员解冻！" % user)
        bank_logger.info("已冻结账户 %s 尝试进行ATM操作，请管理员留意！" % user)
    return wrapper

@check_online
@check_user_status
def transfer_amount(user,in_user,amount):
    if not check_user(in_user):
        print("入账账户 %s 不存在！"%(user,in_user))
        user_logger.warning("%s转账时，入账账户%s不存在！"%(user,in_user))
        return False
    amount = check_amount(amount)
    if not amount:
        print("输入的金额非正数")
        user_logger.warning("%s转账时，输入的金额非正数"%user)
        return False
    fee = 0.05*amount
    if not check_user_amount(user,(amount+fee)):
        print("账户余额为 %s元，不足转账！"%(users_atm[user]["usable"]))
        user_logger.warning("%s转账时，账户余额 %s 已不足！"%(user,users_atm[user]["usable"]))
        return False
    users_atm[user]["usable"] -= (amount+fee)
    users_atm[in_user]["usable"] += amount
    users_atm["admin"]["usable"] += fee
    print("成功转账给 %s 金额 %s 元！收取手续费用 %s 元!" % (in_user,amount,fee))
    user_logger.info("%s 成功转账给 %s 金额 %s 元！手续费用 %s !"% (user,in_user,amount,fee))
    bank_logger.info("%s 成功转账给 %s 金额 %s 元！手续费用 %s !"% (user,in_user,amount,fee))
    bank_logger.info("admin 账户收入手续费金额 %s 元！"%fee)

@check_online
@check_user_status
def look_info(user):
    user_logger.debug("%s 查询余额！"% user)
    print("您的信用卡额度为 %s 元，当前可用余额为：%s 元"%(users_atm[user]["limit"],users_atm[user]["usable"]))

@check_online
@check_user_status
def withdraw_amount(user,amount):
    amount = check_amount(amount)
    if not amount:
        print("输入的提现金额非正数")
        user_logger.warning("%s提现时，输入的提现金额非正数" %user)
        return False
    fee = 0.05 * amount
    if not check_user_amount(user, (amount + fee)):
        print("账户余额 %s元 不足提现！" % (users_atm[user]["usable"]))
        user_logger.warning("%s提现时，账户余额 %s 已不足！" % (user, users_atm[user]["usable"]))
        return False
    users_atm[user]["usable"] -= (amount + fee)
    users_atm["admin"]["usable"] += fee
    print("成功提现金额 %s 元！收取手续费用 %s 元" % (amount,fee))
    user_logger.info("%s 成功提现金额 %s 元！手续费用 %s 元" % (user, amount,fee))
    bank_logger.info("%s 成功提现金额 %s 元！手续费用 %s 元" % (user, amount,fee))
    bank_logger.info("admin 账户收入手续费金额 %s 元！" % fee)

@check_online
@check_user_status
def repay_amount(user,amount):
    amount = check_amount(amount)
    used_amount = users_atm[user]["limit"] - users_atm[user]["usable"]
    if not amount:
        print("输入的还款金额非正数")
        user_logger.warning("%s还款时，输入的还款金额非正数" %user)
        return False
    if amount > used_amount:
        print("输入的还款金额大于已用金额，只需还款 %s 元！" %(used_amount))
        user_logger.info("%s还款时，输入的还款金额大于已用金额，只需还款 %s 元！" %(user,used_amount))
        return False
    users_atm[user]["usable"] += amount
    users_atm["admin"]["usable"] += amount
    print("成功还款金额 %s 元！" % (amount))
    user_logger.info("%s 成功还款金额 %s 元！" % (user, amount))
    bank_logger.info("%s 成功还款金额 %s 元！" % (user, amount))
    bank_logger.info("admin 账户收入 %s 的还款金额 %s 元！" % (user, amount))

@check_online
@check_user_status
def consume_amount(user,amount):
    usable_amount = users_atm[user]["usable"]
    if not amount:
        print("扣款金额非正数" % user)
        user_logger.warning("%s扣款时，传递的扣款金额非正数" % user)
        return False
    if amount > usable_amount:
        print("扣款金额 %s 大于可用金额%s 元！扣款失败！" % ( amount, usable_amount))
        user_logger.warning("%s扣款时，扣款金额 %s 大于可用金额%s 元！扣款失败！" % (user, amount, usable_amount))
        return False
    users_atm[user]["usable"] -= amount
    print("成功扣款您的金额 %s 元！" % (amount))
    user_logger.info("%s 成功扣款金额 %s 元！" % (user, amount))
    bank_logger.info("%s 成功扣款金额 %s 元！" % (user, amount))
    return True
