# 基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
# 多关键字排序：假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序。先按照年年龄进行排序，再按照薪资进行稳定的排序。
#
# 对数字的排序，是否可以看做多关键字排序？
# 先按个位数进行桶排序，排完后个位数是有序的了；
# 再按十位数进行桶排序，排完后十位数是有序的了；
# ......
# 到最后一个数的时候就是有序的了。

def radix_sort(li):
    max_num = max(li)
    # 最大值对应的位数 9->1, 99->2, 888->3, 10000->5
    for i in range(len(str(max_num))):
        buckets = [[] for _ in range(10)]
        for num in li:
            # 987
            # i=0  987//1->987  987%10->7
            # i=1  987//10->98  98%10->8;
            # i=2  987//100->9  9%10=9
            j = (num // 10 ** i) % 10
            buckets[j].append(num)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)


import random
li = [random.randint(0,10000) for i in range(10000)]
print(li)
radix_sort(li)
print(li)