# 列列表进行排序，已知列列表中的数范围都在0到100之间。设计时间复杂度为O(n)的算法。


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0,100) for _ in range(100000)]
count_sort(li)