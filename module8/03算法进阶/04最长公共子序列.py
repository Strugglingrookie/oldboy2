# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/15 16:52
# @File   : 04最长公共子序列.py


'''
公共子序列：
一个序列的子序列是在该序列中删去若干元素后得到的序列。
例：“ABCD”和“BDF”都是“ABCDEFG”的子序列

最长公共子序列（LCS）问题：
给定两个序列X和Y，求X和Y长度大的公共子序列。
例：X="ABBCBDE" Y="DBBCDB" LCS(X,Y)="BBCD"

应用场景：字符串相似度比对，DNA的相似度

思考：长公共子序列是否具有优子结构性质？

例如：要求a="ABCBDAB"与b="BDCABA"的LCS：
由于后一位"B"≠"A"：
因此LCS(a,b)应该来源于LCS(a[:-1],b)与LCS(a,b[:-1])中 更大的那一个
'''


def lcs_len(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            # i j 位置上的字符匹配的时候，来自于左上方+1
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c


c = lcs_len("ABCBDAB", "BDCABA")
for line in c:
    print(line)
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 1, 1]
# [0, 1, 1, 1, 1, 2, 2]
# [0, 1, 1, 2, 2, 2, 2]
# [0, 1, 1, 2, 2, 3, 3]
# [0, 1, 2, 2, 2, 3, 3]
# [0, 1, 2, 2, 3, 3, 4]
# [0, 1, 2, 2, 3, 4, 4]

# 如何输出最长公共子序列的值？
# 创建一个同 c 的二维列表一样大小的列表，相同位置存相应的来源
# 比如 1左上方 2上方 3左方
# 然后打印来源是左上方位置的字符


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # o 存相应位置最长长度的来源 ↖左上方 ↑上方 ←左方
    o = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                o[i][j] = '↖'
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i - 1][j]
                o[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1]
                o[i][j] = '←'
    return c[m][n], o


def lcs_traceback(x, y):
    c, o = lcs(x,  y)
    i = len(x)
    j = len(y)
    trace = []
    while i > 0 and j>0:
        # 来自左上方匹配
        if o[i][j] == '↖':
            trace.append(x[i-1])
            i -= 1
            j -=1
        # 来自上方不匹配
        elif o[i][j] == '↑':
            i -= 1
        # 来自左方 不匹配
        else:
            j -=1
    return ''.join(reversed(trace))


c, o = lcs("ABCBDAB", "BDCABA")
for line in o:
    print(line)

# [0,   0,   0,   0,   0,    0,   0]
# [0, '←', '←', '←', '↖', '←', '↖']
# [0, '↖', '←', '←', '←', '↖', '←']
# [0, '↑', '←', '↖', '←', '←', '←']
# [0, '↖', '←', '↑', '←', '↖', '←']
# [0, '↑', '↖', '←', '←', '↑', '←']
# [0, '↑', '↑', '←', '↖', '←', '↖']
# [0, '↖', '↑', '←', '↑', '↖', '←']

print(lcs_traceback("ABCBDAB", "BDCABA"))
# BDAB