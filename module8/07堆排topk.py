# 现在有n个数，设计算法得到前k大的数。（k<n）
# 解决思路：
# 排序后切片 O(nlogn)
# 排序LowB三人组 O(mn)

# 解决思路：
# 取列表前k个元素建立一个小根堆。堆顶就是目前第k大的数。
# 依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元
# 素；如果大于堆顶，则将堆顶更换为该元素，并且对堆进行一次调整；
# 遍历列表所有元素后，倒序弹出堆顶。


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]

    # 1.建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)

    # 2.遍历
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    # 3.出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)

    return heap


import random

li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))
