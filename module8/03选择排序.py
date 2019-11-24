#选择排序，选出最小的数，放左边，然后选出剩下数组的最小数，放左边，依次选下去
lis=[6,11,3,9,8,9,2,4,5,7,8,7,4]
def select_sort(lis):
    for i in range(len(lis)-1):
        min_index = i
        for j in range(i+1, len(lis)):
            if lis[min_index] > lis[j]:
                min_index = j
        if min_index != i:
            lis[i], lis[min_index] = lis[min_index], lis[i]

select_sort(lis)
print(lis)
