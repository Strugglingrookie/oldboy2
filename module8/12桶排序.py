# 在计数排序中，如果元素的范围比较大（比如在1到1亿之间），
# 如何改造算法？
# 桶排序(Bucket Sort)：首先将元素分在不同的桶中，再对每个桶中的元素排序。


import random


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)] # 创建桶
    for var in li:
        i = min(var // (max_num // n), n-1) # i 表示var放到几号桶里
        buckets[i].append(var) # 把var加到桶里边
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    li.clear()
    for buc in buckets:
        li.extend(buc)
    return li


li = [random.randint(0,10000) for i in range(10000)]
# print(li)
li = bucket_sort(li)
print(li)


# 桶排序的表现取决于数据的分布。也就是需要对不同数据排序时采取
# 不同的分桶策略略。
# 平均情况时间复杂度：O(n+k)
# 最坏情况时间复杂度：O(n2k)
# 空间复杂度：O(nk)