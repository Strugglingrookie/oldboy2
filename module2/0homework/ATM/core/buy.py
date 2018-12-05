# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2


import re
from conf.settings import PRODUCTS_FILE,USER_FILE
from core.log_write import user_logger
from core.login import users,check_online,json_func
from core.atm import look_info,repay_amount,transfer_amount,withdraw_amount,consume_amount,USER_BANK_FILE,users_atm

products = json_func(PRODUCTS_FILE)

@check_online
def show_cart(user):
    user_logger.info("%s 查看购物车！"%user)
    if users[user]["products"]:
        print("您的购物车有如下商品".center(100, "-"))
        for i in users[user]["products"]:
            print(i, users[user]["products"][i])
    else:
        print("您尚未购买商品！")

def show_products(user):
    user_logger.info("%s 查看商品列表！"%user)
    print("商店已上架商品有".center(100, "-"))
    for index, value in enumerate(products):
        print("%s %s %s" % (index, value['name'], value["price"]))

@check_online
def buy_product(user):
    show_cart(user)
    while True:
        show_products(user)
        choice = input("请输入商品编号进行购买，购物完成请输入q退出购物,输入l查看已购买商品信息\n")
        if re.fullmatch("\d+",choice) and int(choice) < len(products):
            product_name = products[int(choice)]["name"]
            product_price = products[int(choice)]["price"]
            if product_name in users[user]["products"]:
                print("您已购买过该商品:\033[1;31;43m %s \033[0m " % product_name)
            elif consume_amount(user,product_price):
                users[user]["products"][product_name] = product_price
                print("成功购买商品：\033[1;33;42m %s \033[0m  " % product_name)
                user_logger.info("%s 用户成功购买商品： %s "%(user,product_name))
            else:
                print("您的余额不足以购买 %s"%product_name)
                user_logger.info("%s 用户因为余额不足,购买商品：%s 失败"%(user,product_name))
        elif choice.upper() == "Q":
            show_cart(user)
            json_func(USER_FILE, users)
            break
        elif choice.upper() == "L":
            show_cart(user)
        else:
            print("：\033[1;31;43m 输入有误，请重新选择! \033[0m ")

def user_run(user):
    while True:
        print("您可以选择以下对应编号进行操作".center(100, "-"))
        choice = input("1.查看账户信息\n2.转账\n3.提现\n4.还款\n5.购买商品\nq.退出程序\n>>:").strip()
        if choice == "1":
            look_info(user)
        elif choice == "2":
            in_user = input("请输入入账账户号：").strip()
            amount = input("请输入转账金额：").strip()
            transfer_amount(user,in_user,amount)
        elif choice == "3":
            amount = input("请输入提现金额：").strip()
            withdraw_amount(user,amount)
        elif choice == "4":
            amount = input("请输入还款金额：").strip()
            repay_amount(user,amount)
        elif choice == "5":
            buy_product(user)
        elif choice.lower() == "q":
            json_func(USER_BANK_FILE,users_atm)
            json_func(USER_FILE,users)
            exit("退出程序！")
        else:
            print("选择有误，请严格按照提示进行选择！")


if __name__ == "__main__":
    user_run("xg")


