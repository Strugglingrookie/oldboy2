#快速排序
#1.归位，先把第一个元素拿出来，用一个临时变量tmp存储，接下来需要把大的放右边，小的放左边
#2.lit[-1]和tmp比较，如果lit[-1]>tmp,继续比较lit[-2]和tmp，如果lit[-2]<=tmp,那么需要把lit[-2]放到之前tmp的位置0，即lis[0]=lit[-2]
#3.上面把lis[-2]这个提前面来了，那么，lis[-2]这个位置空出来了，需要找一个比tmp大的数填进去
#4.lis[0]后面就开始比较lis[1]和tmp了，如果lit[1]<tmp，那么lit[1]不用动，接着比较lis[2]与tmp，如果lit[2]>tmp,那么把lit[2]放到之前lis[-2]这个位置
#5.现在lis[2]这个位置空出来了，那么需要找一个比tmp小的数塞进去，就从lis[-3]开始找，重复234的步骤，一直找下去，直到都比对完成，最后把拿出来的tmp再塞回去
#6.塞tmp，当最后只剩下一个位置的时候，那这个位置就是tmp的，这个位置下标是多少呢？6
#比如lis=[6,11,3,9,8]，那么比对完成的结果是：lis=[3,11,11,9,8]  塞进去的位置就是1
#7.上面的过程就是归位，这个步骤完成后，就需要左边的再来一次上述的步骤，右边再来一次上述的步骤，也就是递归，一直递归下去，直到下标重合，也就是左下标等于右下标

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