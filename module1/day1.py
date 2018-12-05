# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/17

'''
# 7
n=0
while n<3:
    name=input("login_name:").strip()
    pwd=input("password:").strip()
    if (name == "seven" or name == "alex") and pwd == "123":
        print("success")
        break
    else:
        print("fail")
    n+=1


# 8
# a
i=2
tmp=0
while i<=100:
    if i%2 == 0:
        tmp+=i
    else:
        tmp-=i
    i+=1
print(tmp)

# b
n=1
while n<=12:
    if n != 10:
        print(n)


# c
n=100
while n >= 0:
    if n > 50:
        print(n)
    elif n == 50:
        print(n)
        print(50-n)
    else:
        print(50-n)
    n-=1

# d
n=1
while n <= 100:
    if n%2 == 1:
        print(n)
    n+=1

# e
n=1
while n <=  100:
    if n%2 == 0:
        print(n)
    n+=1

'''

# 9
# n1和n2指向的都是同一个内存地址

# 91
# name=input("name:")
# add=input("address:")
# hubby=input("hubby:")
# str="敬爱可爱的%s，最喜欢在%s地方干%s"%(name,add,hubby)
# print(str)

# 92
# year=int(input("year:"))
# if (year%4 == 0 and year%100 !=0) or year%400 == 0:
#     print("%s年是闰年"%(year))
# else:
#     print("%s年不是闰年"%(year))

# 93
# n=1
# m=10000
# while  1:
#     m+=m*0.0325
#     if m>=20000:
#         print(n)
#         break
#     n+=1

# 作业
# n=0
# while n<3:
#     name=input("login_name:").strip()
#     pwd=input("password:").strip()
#     if name == "seven" and pwd == "123":
#         print("欢迎%s登陆"%name)
#         break
#     else:
#         print("fail")
#     n+=1

# # 作业升级
# lis=['alex','miller','xg']
# locked_users=[]
# n=0
# with open("user.txt","a+",encoding="utf-8") as f:
#     f.seek(0)
#     for line in f:
#         locked_users.append(line)
# while n<3:
#     name=input("login_name:").strip()
#     pwd=input("password:").strip()
#     if name in locked_users:
#         print("用户已锁定，不能登陆")
#         break
#     elif name in lis and pwd == "123":
#         print("欢迎%s登陆"%name)
#         break
#     else:
#         print("fail")
#     n+=1
#     if n == 3:
#         with open("user.txt","a+",encoding="utf-8") as f:
#             f.write(name+"\n")



lis = ['a','b','c']
for index,value in enumerate(lis):
    print(index,value)