# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 8:26
# @Author  : Xiao

#装饰器，给一下所有调用函数加上装饰器
user_flag = False

def login(func):
    def wrapper(*args,**kwargs):
        global user_flag
        if not user_flag:
            username = input("输入用户名：")
            pwd = input("输入密码：")
            with open("user.txt","r") as f:
                user_dic = eval(f.read())
            if pwd == user_dic.get(username):
                user_flag = True
            else:
                print("账号或密码有误！")
        else:
            val = func(*args,**kwargs)
            return val
    return wrapper


#修改文件内容的函数
import os,chardet
@login
def modify_file(file_name,old_str,new_str):
    if os.path.exists(file_name):
        char_set = chardet.detect(open(file_name,"rb").read())["encoding"]
        if char_set:
            with open(file_name,"r+",encoding = char_set) as f:
                tmp = f.read().replace(old_str,new_str)
                f.truncate(0)
                f.seek(0)
                f.write(tmp)
            return "修改完成！"
        return "文件内容为空！"

    else:
        return "文件不存在！"
# print(modify_file("a.txt","m","z"))
# print(modify_file("a.txt","z","m"))

#检查用户输入的内容中所有元素是否有空内容
@login
def contain_empty(content):
    content = str(content).replace("0","1").replace("None","1")
    if all(content):
        return "没有空元素"
# print(contain_empty([None,2,3]))

#如果字典的value长度大于2，截断，并返回新的字典
def get_dict(dic):
    for i,v in dic.items():
        if len(v) > 2:
            v = v[:2]
            dic[i] = v
    return dic
dic = {"1":"1235","2":"12","3":[1,2,3,4,5]}
# print(get_dict(dic))

#解释闭包
#A函数，内部嵌套B函数，返回值是B函数对象，在外部调用B函数时，其变量名作用于仍在A函数里

#写函数，返回扑克牌，共52项，每项是一个元祖
def get_card():
    car_lis = []
    color = ["黑桃","红桃","梅花","方块"]
    boss = ["J","Q","K","A"]
    for c in color:
        for b in boss:
            car_lis.append((c+b,))
        for i in range(2,11):
            car_lis.append((c,i))
    return car_lis
# print(get_card())

#函数，传n个数，返回最大和最小值
def get_min_max(*args):
    for i in args:
        if type(i) is not int:
            return "传参必须是数字！"
    return {"max":max(args),"min":min(args)}
# print(get_min_max(1,1,2,'a',5,8,0,10,25,-1,89))

#计算面积
def area(types,length1,length2=''):
    import math
    def circle_area():
        return math.pi*float(length1)*float(length1)
    def square_area():
        return float(length1)*float(length1)
    def shape_area():
        return float(length1)*float(length2)
    if types not in ["长方形","圆形" ,"正方形"] or not str(length1).isdigit() or not float(length1)>0:
        return "传参有误！"
    if types == "长方形" and  not str(length2).isdigit() or not float(length1) > 0:
        return "传参有误！"
    if types == "长方形":
        val = shape_area()
    elif types == "圆形" :
        val = circle_area()
    else:
        val = square_area()
    return val
# print(area("圆形",1,"12165"))

#函数，计算传参的阶乘[词典]	factorial
def factorial(n):
    if type(n) is int and n>0:
        sum = 1
        for i in range(1,n+1):
            sum *= i
        return sum
    return "传参有误！"
# print(factorial(5))

#生活器，日志调用方法
# 2017-10-19 22:07:38 [1] test log db backup 3
# 2017-10-19 22:07:40 [2] user alex login success
import time
def logging(filename,moudle):
    msg = "test log db backup 3"
    with open(filename,"a+")as f:
        f.read()
        count=1
        if moudle == "file":
            while True:
                yield f.write("%s [%s] %s\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),count,msg))
                f.flush()
                count+=1
        elif moudle == "terminal":
            while True:
                yield print("%s [%s] %s\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),count,msg))
                count+=1
        elif moudle == "both":
            while True:
                f.write("%s [%s] %s\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),count,msg))
                f.flush()
                yield print("%s [%s] %s\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),count,msg))
                count+=1
        else:
            print("传参有误！")
# val=logging("log.txt","both")
# while True:
#     choice = input("choice:")
#     if choice == "q":
#         exit()
#     elif choice == "s":
#         val.send("hhhahaha")
#     else:
#         next(val)

name=['alex','wupeiqi','yuanhao','nezha']
def to_sb(lis):
    lis = list(map(lambda x:x+"_sb",lis))
    return lis
# print(to_sb(name))

num = [1,3,5,6,7,8]
def get_double(lis):
    lis = list(filter(lambda x:not x%2,lis))
    return lis
# print(get_double(num))

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
def get_large(lis):
    lis = list(filter(lambda x:x['price']>100,lis))
    return lis

def get_sum(lis):
    res = sum([x['shares'] * x['price'] for x in lis])
    return res

# print(get_sum(portfolio))
# print(get_large(portfolio))



