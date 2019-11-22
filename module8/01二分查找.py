# 二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。
# 非递归  时间复杂度 O(logn)
lis = [1,2,3,4,5,6,7,8,9,10]
def bin_search(lis,value):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low+high) // 2
        if lis[mid] == value:
            return mid
        elif lis[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    else:
        print('不存在该数据%s'%value)
# print(bin_search(lis, 10))

# 递归 时间复杂度 O(logn)
def bin_search_plus(lis,value,low,high):
    if low > high:  # 找不到的时候结束递归，不然会一直递归下去，导致报错
        return None
    mid = (low + high) // 2
    if lis[mid] == value:
        return mid
    elif lis[mid] > value:
        return bin_search_plus(lis, value, low, mid-1)  # 必须用 return 来接收最后一次递归返回来的值
    else:
        return bin_search_plus(lis, value, mid+1, high)
# print(bin_search_plus(lis,11,0,9))


# 习题：输入学生id，输出该学生在列表中的下标，并输出完整学生信息

stus=[{'id':1001, 'name':"张三", 'age':20},
{'id':1002, 'name':"李四",'age':25},
{'id':1003, 'name':"李四2",'age':25},
{'id':1004, 'name':"王五", 'age':23},
{'id':1005, 'name':"王五2", 'age':23},
{'id':1006, 'name':"王五3", 'age':23},
{'id':1007, 'name':"王五4", 'age':23},
{'id':1008, 'name':"王五5", 'age':23},
{'id':1009, 'name':"王五5", 'age':23},
{'id':10010, 'name':"王五7", 'age':23},
{'id':10011, 'name':"王五8", 'age':23},
{'id':10012, 'name':"赵六", 'age':33}]

# 非递归
def find_stu(stus,id):
    low = 0
    high = len(stus) - 1
    while low <= high:
        mid = (low+high) // 2
        if stus[mid]['id'] == id:
            return stus[mid]
        elif stus[mid]['id'] > id:
            high = mid -1
        else:
            low = low + 1
# print(find_stu(stus,10011))

# 递归
def find_stu_plus(stus,id,low,high):
    if low > high:
        return None
    mid = (low+high) // 2
    if stus[mid]['id'] == id:
        return stus[mid]
    elif stus[mid]['id'] > id:
        return find_stu_plus(stus, id, low, mid - 1)  # 必须用 return 来接收最后一次递归返回来的值
    else:
        return find_stu_plus(stus, id, mid + 1, high)
print(find_stu_plus(stus,10011,0,len(stus)-1))