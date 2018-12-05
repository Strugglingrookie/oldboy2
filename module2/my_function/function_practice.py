# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/25

import chardet
char_set = chardet.detect((open("user_info.txt","rb")).read())
user_list = []
with open("user_info.txt","r+",encoding = char_set["encoding"]) as f:
    for line in f:
        user_list.append(line.strip().split(","))

def login():
    count = 0
    while count < 3:
        user_name = input("your name >>:\t")
        pwd = input("your password >>:\t")
        for index,value in enumerate(user_list):
            if user_name == value[0] and pwd == value[1]:
                print("欢迎%s登陆系统".center(50,"-")%user_name)
                return str(index)
        print("账号或密码错误！")
        count += 1
    print("三次机会已用完，已锁定！")

def print_info(index):
    title = ['name','age','pos','dept']
    print(''.center(25,'-'))
    for i,v in enumerate(list(zip(title,user_list[index][2:]))):
        print('%s\t%s:\t%s'%(i,v[0],v[1]))
    print(''.center(25,'-'))

def modify_info(index):
    print_info(index)
    while True:
        choice = input("请输入您需要修改的序号 >>:\t").strip()
        if choice.isdigit() and int(choice) in list(range(4)):
            while True:
                print("current value:%s"%user_list[index][int(choice)+2])
                value = input("new value >>:\t").strip()
                if value:
                    user_list[index][int(choice)+2] = value
                    print("修改成功！")
                    with open("user_info.txt", "w", encoding="utf-8") as f:
                        for i in user_list:
                            f.write(",".join(i)+"\n")
                    return True
                else:
                    print("不能输入为空！")
        else:
            print("输入有误，请重新选择！")


def modify_pwd(index):
    while True:
        pwd = input("new password >>:\t").strip()
        if pwd:
            user_list[index][1] = pwd
            print("修改成功！")
            with open("user_info.txt", "w", encoding="utf-8") as f:
                for i in user_list:
                    f.write(",".join(i) + "\n")
            return True
        else:
            print("不能输入为空！")

choice_list = [modify_info,print_info,modify_pwd]
index = login()

if index:
    index = int(index)
    while True:
        choice = input('''请输入您的选择：\n0 ：修改个人信息\n1 ：打印个人信息\n2 ：修改密码\nq ：退出程序！\n''').strip()
        if choice.upper() == "Q":
            exit()
        elif choice in ['0', '1', '2']:
            choice_list[int(choice)](index)
        else:
            print("输入有误，请重新输入！")



