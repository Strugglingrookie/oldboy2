def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


def mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(li, low, mid)
        mergesort(li, mid + 1, high)
        merge(li, low, mid, high)

str = 'asdddgdffffadfaa'
lis1 = []
lis2 = []
for i in str:
    if len(lis1) == 0 or i != lis1[-1]:
        lis1.append(i)
        lis2.append(1)
    else:
        lis2[-1] += 1
print('连续出现最多次数的是%s，出现次数%s'%(lis1[lis2.index(max(lis2))],max(lis2)))
