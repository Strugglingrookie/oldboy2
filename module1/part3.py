# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:31
# @Author  : Xiao

# 基础要求：
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 2、允许用户根据商品编号购买商品
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4、可随时退出，退出时，打印已购买商品和余额
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
# 扩展需求：
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 2、允许查询之前的消费记录
# 踩分点:
# 基础要求完成每条15分；
# 扩展需求完成每条10分；
# 代码结构足够好，可以酌情加分。

#文件用字典格式存储用户信息数据 {"xiaogang":{"password":"123456","salary":123,"goods":{"电脑": 1999,"鼠标" : 10}},...}

products = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

# 打开文件读取用户信息,如果不存在用户则定义一个空字典
with open('user_info.txt','a+',encoding='utf-8') as f:
    f.seek(0)
    tmp = f.read()
    user_info = eval(tmp) if tmp else {}

# 用户登录和薪资信息输入校验
while True:
    user = input("Your name :\n").strip()
    pwd = input("Password :\n").strip()
    if not user or not pwd:
        print("输入不能为空请重新输入！")
        continue
    elif user in user_info and pwd != user_info[user]["password"] :
        print("用户名或密码错误，请重新输入！")
        continue
    elif user in user_info and pwd == user_info[user]["password"] :
        break
    else:
        while True:
            salary = input("Input your salary:\n").strip()
            if not salary.isdigit() or float(salary) <= 0:
                print("输入薪资有误请重新输入！")
                continue
            else:
                salary = float(salary)
                break
    break

# 如果用户不存在,在user_info里初始化用户信息
if user not in user_info:
    user_info[user] = {}
    user_info[user]["password"] = pwd
    if not user_info[user].get("goods"):
        user_info[user]["goods"] = {}

# 如果用户存在,输出用户已购买商品
else:
    salary = user_info[user]["salary"]
    if not user_info[user]["goods"]:
        print("您的余额为：\033[1;33;42m %s \033[0m ，尚未购买商品".center(100, "-") % (salary))
    else:
        print("您的余额为：\033[1;33;42m %s \033[0m ，已购买商品有".center(100, "-") % (salary))
        for i in user_info[user]["goods"]:
            print(i, user_info[user]["goods"][i])

#购物主逻辑
while True:
    print("商店已上架商品有".center(100, "-"))
    for index, value in enumerate(products):
        print("%s %s %s" % (index, value['name'], value["price"]))
    choice = input("请输入商品编号进行购买，购物完成请输入q退出,输入l查看已购买商品信息\n")
    if choice.isdigit() and int(choice) < len(products):
        if products[int(choice)]["name"] in user_info[user]["goods"]:
            print("您已购买过该商品:\033[1;31;43m %s \033[0m " % (products[int(choice)]["name"]))
        elif products[int(choice)]["name"] not in user_info[user]["goods"] and salary >= products[int(choice)][
            "price"]:
            salary -= products[int(choice)]["price"]
            user_info[user]["salary"] = salary
            user_info[user]["goods"][products[int(choice)]["name"]] = products[int(choice)]["price"]
            print("您已成功购买商品：\033[1;33;42m %s \033[0m ，您的余额还有：\033[1;33;42m %s \033[0m " % (products[int(choice)]["name"], salary))
        else:
            print("您的余额：\033[1;31;43m %s \033[0m 已不足购买此商品，请另做选择！" % salary)
            continue
    elif choice.upper() == "Q":
        if not user_info[user]["goods"]:
            print("您的余额为：\033[1;33;42m %s \033[0m ，尚未购买商品".center(100, "-") % (salary))
        else:
            print("您的余额为：\033[1;33;42m %s \033[0m ，已购买商品有".center(100, "-") % (salary))
            for i in user_info[user]["goods"]:
                print(i, user_info[user]["goods"][i])
        with open('user_info.txt', 'w', encoding='utf-8') as f:
            f.write(str(user_info))
        exit()
    elif choice.upper() == "L":
        if not user_info[user]["goods"]:
            print("您的余额为：\033[1;33;42m %s \033[0m ，尚未购买商品".center(100, "-") % (salary))
        else:
            print("您的余额为：\033[1;33;42m %s \033[0m ，已购买商品有".center(100, "-") % (salary))
            for i in user_info[user]["goods"]:
                print(i, user_info[user]["goods"][i])
    else:
        print("：\033[1;31;43m 输入有误，请重新选择! \033[0m ")