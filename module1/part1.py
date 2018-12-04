# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:31
# @Author  : Xiao

# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
users = {"alex":123456,'Miller':654321,"Xiaogang":"123654"}
count = 3
while count > 0:
    user = input("Your name :\n").strip()
    pwd = input("Password :\n").strip()
    if user in users and pwd == str(users.get(user)):
        print("欢迎%s登陆系统".center(50,"*")%user)
        break
    else:
        if count == 1:
            print("错误次数达到3次，已被锁定".center(50, "*"))
        else:
            print("用户名或密码有误，请重新输入".center(50, "*"))
        count -= 1

# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
users = {"alex":123456,'Miller':654321,"Xiaogang":"123654"}
count = 3
with open("user.txt", "a+", encoding="utf-8") as f:
    f.seek(0)
    lock_users = f.read().splitlines()
while count > 0:
    user = input("Your name :\n").strip()
    pwd = input("Password :\n").strip()
    if user not in lock_users:
        if user in users and pwd == str(users.get(user)):
            print("欢迎%s登陆系统".center(50,"*")%user)
            break
        else:
            if count == 1:
                print("错误次数达到3次，已被锁定".center(50, "*"))
                with open("user.txt","a+",encoding="utf-8") as f:
                    f.write(user+"\n")
            else:
                print("用户名或密码有误，请重新输入".center(50, "*"))
            count -= 1
    else:
        print("用户被锁定，请联系管理员解锁！".center(50, "*"))
        break