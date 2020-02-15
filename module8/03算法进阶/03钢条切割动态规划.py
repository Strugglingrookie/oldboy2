# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 15:01
# @File   : 03钢条切割动态规划.py

# 自底向上 动态规划求解 钢条切割：

# 由递归方法求解最优解的时候可以看懂子问题的重复计算
# 因此，动态规划算法安排求解的顺序，对每个子问题只求解一次，并将结果保存到数组中。
# 如果随后再次需要此子问题的解，只需查找保存的结果，不必重新计算。
# 综上：动态规划的方法是付出额外的内存空间来节省计算时间

from cut_rod_recursion import cal_time, c1, c2, p1, p2


@cal_time
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


cut_rod_dp(p1, 15)


# 42
# cut_rod_dp running time 0.0 second

# 可以看到相比较 递归方式求解 要快太多
# 时间复杂度是 n*n

# 输出切割方案


def cut_rod_extend(p, n):
    r = [0]  # 切割后的最优值
    s = [0]  # 对应长度下的左边不切割的长度
    for i in range(1, n + 1):
        res_r = 0  # 价格最大值
        res_s = 0  # 价格最大值对应的左边不切割的长度
        for j in range(1, i + 1):
            if res_r < p[j] + r[i - j]:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    solution = []
    while n > 0:
        solution.append(s[n])
        n -= s[n]
    return r, solution


r, s = cut_rod_solution(p2, 9)
print(r, s)
# 25 [3, 6]
