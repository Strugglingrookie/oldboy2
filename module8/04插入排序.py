# 列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
# 每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空
lis=[6,3,11,9,8,9,2,4,5,7,8,7,4]  #[2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 11]

def insert_sort(lis):
    for i in range(1,len(lis)):
        temp = lis[i]
        j = i - 1
        while lis[j] > temp and j >= 0:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = temp

insert_sort(lis)
print(lis)