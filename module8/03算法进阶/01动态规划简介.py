# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2020/2/12


# 斐波那契数列列: F(n) = F(n-1) + F(n-2)
# 练习:使⽤递归和⾮递归的方法来求解斐波那契数列的第n项
# 问题：用递归会有重复计算的情况，所以效率比没有用递归的方式慢很多

# 子问题的重复计算
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# 动态规划（DP）的思想 = 递推式 + 重复子问题
def fibnacci_no_rec(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


# print(fibnacci(100)) # 运算很久都没有结果
print(fibnacci_no_rec(100))  # 不到1秒出结果
