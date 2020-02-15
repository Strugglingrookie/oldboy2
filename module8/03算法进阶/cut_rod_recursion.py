# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 14:31
# @File   : cut_rod_recursion.py

# 自顶向下用递归求解 钢条切割

import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        t = end_time - start_time
        print("%s running time %s second" %(func.__name__, t))
        return result
    return wrapper


p1 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
p2 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# 递归求解一，切割的两段都是最优解
def cut_rod_rec1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            # 切割的两段都是最优解
            res = max(res, cut_rod_rec1(p, i) + cut_rod_rec1(p, n - i))
        return res


# 递归求解二，对切割的左边那段不取最优解，对右边的那段取最优解
def cut_rod_rec2(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            # 切割的左边这段不再切割，只对右边这段取最优解
            # 因为所有情况都会考虑到，所以没必要对两段都取最优解
            # 假如，9的最优解是 4的最优解 和 5的最优解
            # 那么说明4和5都有其最优解的子项 如4=2+2 5=2+3
            # 那么也可以组成 2 和 2+2+3 的组合，也就是，2+7的组合满足条件
            res = max(res, p[i] + cut_rod_rec2(p, n-i))
        return res


# 因为cut_rod_rec是递归，不能直接加装饰器
@cal_time
def c1(p, n):
    return cut_rod_rec1(p, n)


@cal_time
def c2(p, n):
    return cut_rod_rec2(p, n)


# print(c1(p1, 15))
# c1 running time 1.9559204578399658 second
# 42

print(c2(p1, 15))
# c2 running time 0.007940530776977539 second
# 42

# 可以看到时间相差很大，因为第一种对左边的又继续进行了最优求解

# 分析：
# 15的长度对于计算器来说是很短的，但为什么运行这么慢呢
# 原因就是在于，子问题的重复计算
# 比如求r[9]和r[8]的时候都求解了r[7],就是说r[7]被求解了两次
# 时间复杂度是 2 的 n 次方

