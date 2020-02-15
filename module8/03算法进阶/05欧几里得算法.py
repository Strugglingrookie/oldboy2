# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 19:56
# @File   : 05欧几里得算法.py

'''
最大公约数
约数：如果整数a能被整数b整除，那么a叫做b的倍数，b叫做 a的约数。
给定两个整数a,b，两个数的所有公共约数中的最大值即为最大公约数（Greatest Common Divisor, GCD）。
例：12与16的⼤大公约数是4

欧几里得算法：gcd(a, b) = gcd(b, a mod b)
例：gcd(60, 21) = gcd(21, 18) = gcd(18, 3) = gcd(3, 0) = 3
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(12, 16))   # 4
print(gcd2(12, 16))  # 4
