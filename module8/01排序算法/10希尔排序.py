# 希尔排序(Shell Sort)是一种分组插入排序算法。

# 首先取一个整数d1=n/2，将元素分为d1个组，每组相邻两元素之间距离为d1，在各组内进行直接插入排序；

# 取第二个整数d2=d1/2，重复上述分组排序过程，直到i=1，即所有元素在同一组内进行直接插入排序。

# 希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序

# 插入排序代码
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j]> tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

# gap=n/2
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)): #i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

import random

li = list(range(1000))
random.shuffle(li)
print(li)
shell_sort(li)
print(li)
