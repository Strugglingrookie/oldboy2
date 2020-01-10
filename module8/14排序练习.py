# 1. 给两个字符串s和t，判断t是否为s的重新排列后组成的单词
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
def count_letter(str):
    dic = {}
    for i in str:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    return dic

def eauql_str(str1,str2):
    dic1 =count_letter(str1)
    dic2 =count_letter(str2)
    if len(dic1) != len(dic2):
        return False
    else:
        for k in dic1:
            if dic1.get(k) != dic2.get(k):
                return False
    return True

# s = "anagram"
# t = "nagaram"
# y = "nagaramh"
# print(eauql_str(s,t)) # True
# print(eauql_str(s,y)) # False


# 2. 给定一个m*n的二维列表，查找一个数是否存在。列表有下列特性：
# 每一行的列表从左到右已经排序好。
# 每一行第一个数比上一行最后一个数大。
li = [
    [1,3,5,7],
    [8,10,12,16],
    [19,100,156,189]
 ]
def find_func(li, num):
    n = None
    if li != []:
        n = len(li[0])
    if n != None:
        left = 0
        right = n*len(li) - 1
        while left <= right:
            mid = (left+right) // 2
            i = mid // n
            j = mid % n
            if li[i][j] == num:
                return i,j
            elif li[i][j] > num:
                right -= 1
            elif li[i][j] < num:
                left += 1
    return False

print(find_func(li, 156))

# 3. 给定一个列表和一个整数，设计算法找到两个数的下标，
# 使得两个数之和为给定的整数。保证肯定仅有一个结果。
# 例如，列表[1,2,5,4]与目标整数3，1+2=3，结果为(0,1).
def find_two(li, sum):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]+li[j] == sum:
                return i,j
    return False

# lis = [1,3,5,7]
# print(find_two(lis, 12))