
lis=[6,3,11,9,8,9,2,4,5,7,8,7,4]  #[2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 11]

def partion(lis,left,right):
    temp = lis[left]
    while left < right:
        while left < right and lis[right] >= temp:
            right -= 1
        lis[left] = lis[right]
        while left < right and lis[left] <= temp:
            left += 1
        lis[right] = lis[left]
    lis[left] = temp
    return left

def quick_sort(lis,left,right):
    if left < right:
        mid = partion(lis,left,right)
        quick_sort(lis, left, mid-1)
        quick_sort(lis, mid+1, right)


quick_sort(lis,0,len(lis)-1)
print(lis)