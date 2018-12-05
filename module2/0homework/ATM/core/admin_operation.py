# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2

import re,datetime
from core.log_write import user_logger,bank_logger
from core.login import users,json_func,check_online,get_md5
from core.atm import users_atm
from conf.settings import USER_FILE,USER_BANK_FILE

@check_online
def add_user(admin):
    while True:
        info = input("请以逗号隔开输入账号(英文或数字),姓名(非空字符),角色(1代表管理员/0代表普通用户),密码(英文或数字),额度\n")
        if re.fullmatch("\w+[,|，]{1}\S+[,|，]{1}[0|1]{1}[,|，]{1}\w+[,|，]{1}[\d]+",info):
            user_lis = re.split("[，|,]",info)
            user = user_lis[0]
            name = user_lis[1]
            role = int(user_lis[2])
            pwd = get_md5(user_lis[3])
            limit = float(user_lis[4])
            if user not in users:
                users[user] = {}
                users[user]["name"] = name
                users[user]["password"] = pwd
                users[user]["role"] = role
                users[user]["products"] = {}
                users[user]["create_time"] = str(datetime.datetime.now().date())
                users_atm[user] = {}
                users_atm[user]["name"] = name
                users_atm[user]["usable"] = limit
                users_atm[user]["limit"] = limit
                users_atm[user]["status"] = 1
                users_atm["admin"]["usable"] -= limit
                print("添加用户 %s 成功"%user)
                user_logger.info("管理员 %s 添加用户 %s 成功"%(admin,user))
                bank_logger.info("管理员 %s 添加用户 %s 成功"%(admin,user))
                break
            else:
                print("%s 用户已存在"%user)
                user_logger.warning("管理员添加用户时，%s 用户已存在"%user)
        else:
            print("输入信息有误,请参照提示按格式输入！")
            user_logger.warning("管理员添加用户时，用户输入用户信息格式有误！")

@check_online
def change_limit(admin):
    while True:
        change = input("请输入用户账号和额度修改值(+表示增加额度，-代表减少额度)\n账号和额度用逗号分割\n>>:")
        if re.fullmatch("\w+[,|，]{1}[+|-]{1}[\d]+", change):
            change_lis = re.split("[，|,]", change)
            user = change_lis[0]
            change_amount = change_lis[1]
            limit = users_atm[user]["limit"]
            usable = users_atm[user]["usable"]
            after_change_limit =eval(str(limit)+change_amount)
            after_change_usable =eval(str(usable)+change_amount)
            if user in users_atm and not after_change_usable < 0:
                users_atm[user]["limit"] = after_change_limit
                users_atm[user]["usable"] = after_change_usable
                print("修改 {user} 额度成功！修改前 {user} 额度：{before}；修改后 {user} 额度：{after}".
                                 format(user=user,before=limit,after=after_change_limit))
                user_logger.info("管理员 {admin} 修改 {user} 额度成功！修改前 {user} 额度：{before}；修改后 {user} 额度：{after}".
                                 format(admin=admin,user=user,before=limit,after=after_change_limit))
                bank_logger.warning("管理员 {admin} 修改 {user} 额度成功！修改前 {user} 额度：{before}；修改后 {user} 额度：{after}".
                                 format(admin=admin,user=user, before=limit, after=after_change_limit))
                break
            else:
                print("被修改的用户不存在或者额度减小过多，请确认修改信息正确性！")
                user_logger.warning("被修改的用户不存在或者额度减小过多，管理员 %s 修改 %s 用户的额度失败！"%(admin,user))
        else:
            print("输入信息有误,请参照提示按格式输入！")
            bank_logger.warning("输入用户和金额格式有误，管理员 %s 修改用户的额度失败！"%admin)

@check_online
def change_status(admin):
    while True:
        change = input("请输入用户账号和修改状态(1代表可用，0代表冻结)\n账号和状态用逗号分割\n>>:")
        if re.fullmatch("\w+[,|，]{1}[1|0]{1}", change):
            change_lis = re.split("[，|,]", change)
            user = change_lis[0]
            change_statu = int(change_lis[1])
            if user in users_atm:
                users_atm[user]["status"] = change_statu
                print("修改 %s 用户状态成功！修改后的状态为 %s"%(user,change_statu))
                user_logger.info("管理员 %s 修改 %s 用户状态成功！修改后的状态为 %s"%(admin,user,change_statu))
                bank_logger.info("管理员 %s 修改 %s 用户状态成功！修改后的状态为 %s"%(admin,user,change_statu))
                break
            else:
                print("被修改的用户不存在，修改 %s 用户的状态失败！"%user)
                user_logger.warning("被修改的用户不存在，管理员 %s 修改 %s 用户的状态失败！"%(admin,user))
        else:
            print("输入用户和状态格式有误,修改 %s 用户的状态失败！")
            user_logger.warning("输入用户和状态格式有误,管理员 %s 修改的状态失败！"%admin)

def admin_run(admin):
    while True:
        print("您可以选择以下对应编号进行操作".center(100, "-"))
        choice = input("1添加用户\n2修改用户额度\n3修改用户状态\nq退出程序\n>>:").strip()
        if choice == "1":
            add_user(admin)
        elif choice == "2":
            change_limit(admin)
        elif choice == "3":
            change_status(admin)
        elif choice.lower() == "q":
            json_func(USER_BANK_FILE, users_atm)
            json_func(USER_FILE, users)
            exit("退出程序！")
        else:
            print("选择有误，请严格按照提示进行选择！")