#选择排序，选出最小的数，放左边，然后选出剩下数组的最小数，放左边，依次选下去
lis=[6,11,3,9,8,9,2,4,5,7,8,7,4]
def select_sort(lis):
    for i in range(len(lis)-1):
        min_no = i
        for j in range(i+1, len(lis)):
            if lis[min_no] > lis[j]:
                min_no = j
        if min_no != i:
            lis[i],lis[min_no] = lis[min_no],lis[i]

select_sort(lis)
print(lis)
