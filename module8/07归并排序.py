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

li = [10,4,6,3,8,2,5,7]
mergesort(li, 0, len(li)-1)
print(li)
