# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2020/2/11


'''
1.贪⼼算法(⼜称贪婪算法)
在对问题求解时，总是做出在当前看来是最好的选择。
也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。


贪心算法并不保证会得到最优解，但是在某些问题上贪心算法的解就是最优解。
要会判断一个问题能否用贪⼼算法来计算。

2.找零问题
假设商店⽼板需要找零n元钱，
钱币的面额有:100元、50元、 20元、5元、1元，
如何找零使得所需钱币的数量最少?
'''

lis = [100, 50, 20, 5, 1]


def change(l, n):
    # tmp 存相应面额的数量
    tmp = [0 for _ in range(len(l))]
    for index, money in enumerate(l):
        tmp[index] = n // money
        n = n % money
    return tmp, n


print(change(lis, 274))
# ([2, 1, 1, 0, 4], 0)

'''
3.背包问题
⼀个⼩偷在某个商店发现有n个商品，第i个商品价值vi元，重wi千克。
他希望拿走的价值尽量高，但他的背包最多只能容纳W千克的东西。
他应该拿走哪些 商品?
0-1背包:
对于一个商品，小偷要么把它完整拿走，要么留下。
不能只拿⾛一部分，或把一个商品拿⾛多次。(商品为⾦条)
分数背包:
对于一个商品，⼩偷可以拿⾛其中任意一部分。(商品为⾦砂)
'''

# 每个商品元组表示(价格, 重量)
goods = [(60, 10), (100, 20), (120, 30)]

# 商品按商品的价值倒序
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_prize = 0
    for index, (prize, weight) in enumerate(goods):
        if weight <= w:
            m[index] = 1
            total_prize += prize
            w -= weight
        else:
            m[index] = w / weight
            total_prize += prize * m[index]
            break
    return total_prize, m


print(fractional_backpack(goods, 40))
# (200.0, [1, 1, 0.3333333333333333])

'''
4.拼接最大数字问题
有n个⾮负整数，将其按照字符串拼接的方式拼接为一个整数。
如何拼接可以使得到的整数最⼤?
例:32,94,128,1286,6,71可以拼接出的最⼤整数为 94716321286128
'''
li = [32, 94, 128, 1286, 6, 71]


def number_join(li):
    li = list(map(str, li))

    # 按两个元素拼接得到的值进行排序
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] + li[j+1] < li[j+1] + li[j]:
                li[j], li[j+1] = li[j+1], li[j]
    return(''.join(li))


print(number_join(li))

'''
活动选择问题
假设有n个活动，这些活动要占⽤用同一片场地，
而场地在某时刻只能供一个活动使用。
每个活动都有⼀个开始时间si和结束时间fi(题目中时间以整数表示)
表示活动在[si, fi)区间占⽤场地。
问:安排哪些活动能够使该场地举办的活动的个数最多?

贪⼼结论:最先结束的活动一定是最优解的一部分。 

证明:假设a是所有活动中最先结束的活动，b是最优解中最先结束的活动。
如果a=b，结论成⽴。
如果a≠b，则b的结束时间⼀定晚于a的结束时间，
则此时用a替换掉最优解中的b，a一定不与最优解中的其他活动时间重叠，
因此替换后的解也是最优解。
'''

activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
# 保证活动是按照结束时间排好序的
activities.sort(key=lambda x:x[1])


def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        # 当前活动的开始时间小于等于最后一个入选活动的结束时间
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res


print(activity_selection(activities))