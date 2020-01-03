
lis=[11,3,9,8,9,2,4,5,7,8,7,4]
def sift(lis, low, high):
    i = low
    j = 2*i + 1
    tmp = lis[i]
    while j<=high:
        if j < high and lis[j] < lis[j+1]:
            j += 1
        if tmp < lis[j]:
            lis[i] = lis[j]
            i = j
            j = 2*i +1
        else:
            break
    lis[i] = tmp


def heap(lis):
    n = len(lis)
    for i in range(n // 2, -1, -1):
        sift(lis,i,n-1)
    for i in range(n-1,-1,-1):
        lis[0],lis[i] = lis[i],lis[0]
        sift(lis,0,i-1)
# heap(lis)
print(lis)
for i in range(10 // 2, -1, -1):
    print(i)
