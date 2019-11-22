# 冒泡排序就是把大的数据一步步往后面冒  时间复杂度：O(n2)
lis=[6,11,3,9,8,9,2,4,5,7,8,7,4]
def bubble_sort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
# bubble_sort(lis)
# print(lis)

# 冒泡排序-优化
# 如果冒泡排序中执行一趟而没有交换，则列表已经是有序状态，可以直接结束算法。
def bubble_sort_plus(lis):
    for i in range(len(lis)-1):
        exchange = False
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
                exchange = True
        if not exchange:
            return

bubble_sort_plus(lis)
print(lis)


