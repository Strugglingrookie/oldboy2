# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城
# 博客地址：http://www.cnblogs.com/alex3714/articles/8955091.html

import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
#
# def recursion(n):
#
#     print(n)
#     recursion(n+1)
#
#
#
# recursion(1)
#
#


# 10／2 ＝ 5
# 5／2 ＝ 2
# 2／2 ＝ 1

# def calc(n):
#
#     v = int(n/2)
#     print(v)
#     if v == 0:
#         return 'Done'
#
#     calc(v)
#     print(v)
#
#
# calc(10)

#n! = n * (n-1)!


# 4* 6
# 3 * 2
# 2*1
#
def factorial(n):

    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))



def cal(n):

    print(n)
    return cal(n+1)
    #print('sdfsfsdf')

cal(1)