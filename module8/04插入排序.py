# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2019/11/24


#插入排序，有序区和无序区，第一个元素为有序区，其他元素为无序区，从无序区调一个元素到有序区，进行插入排序，直到无序区没有数据

lis=[11,3,9,8,9,2,4,5,7,8,7,4]
for i in range(1,len(lis)):
    tmp=lis[i]
    j=i-1
    while j >=0 and lis[j]>tmp:
        lis[j+1]=lis[j]
        j-=1
    lis[j+1]=tmp
print(lis)
