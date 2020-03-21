# # 装饰器
# import re
#
#
# def decorator1(func):
#     def wrapper(*args,**kwargs):
#         print('装饰器一')
#         func(*args,**kwargs)
#     return wrapper
#
# def out(n):
#     def decorator2(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 print('装饰器%d'%i)
#             func(*args,**kwargs)
#         return wrapper
#     return decorator2
#
# class decorator3:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs)
#
# @decorator1
# def count1(a,b):
#     print(a+b)
#
# @out(3)
# def count2(a,b):
#     print(a+b)
#
# @decorator3
# def count3(a,b):
#     print(a+b)
#
# # count1(1,2)
# # count2(1,2)
# # count3(1,2)
#
# '''
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 示例 1:
# s = "abc", t = "ahbgdc"
# 返回 true.
# 示例 2:
# s = "axc", t = "ahbgdc"
# 返回 false.
# '''
#
# s = "abd"
# t = "ahbgdc"
#
# def fun(s,t):
#     my_t = iter(t)
#     try:
#         for i in s:
#             while True:
#                 tmp = next(my_t)
#                 if tmp == i:
#                     break
#     except Exception as e:
#         return False
#     else:
#        return True
#
# # print(fun(s,t))
#
# res = re.search(r'a*',"gfdaaasd!#%^b")
# if res:
#     print(res.group())

# li = [10,4,6,3,8,2,5,7]
# tmp = [4,10]
# li[0:2] = tmp
# print(li)
# print(2017%4)

# li = [4.3, 1.2, 5, 11, 8.444, 5.333]
#
#
# def bubble_sort(l):
#     for i in range(len(l) - 1):
#         exchange = False
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#                 exchange = True
#         if not exchange:
#             break
#     return l
#
#
# print(bubble_sort(li))

def sub_sequence1(a,b):
    i,j = 0,0
    while i<len(a) and j<len(b):
        if a[i] == b[j]:
            i+=1
            j+=1
        else:
            j+=1
    if i==len(a):
        return True
    return False

def sub_sequence(a,b):
    b = iter(b)
    return all(i in b for i in a)

# print(sub_sequence([1, 3, 5], [1, 2, 3, 4, 5]))
# print(sub_sequence([1, 4, 5], [1, 2, 3, 4, 5]))
# print(sub_sequence([1, 6, 5], [1, 2, 3, 4, 5]))



def is_subsequence(a, b):
    b = iter(b)
    # print(b)
    #
    # gen = (i for i in a)
    # print(gen)
    #
    # for i in gen:
    #     print(i)
    #
    # gen = ((i in b) for i in a)
    # print(gen)
    #
    # for i in gen:
    #     print(i)

    return all(((i in b) for i in a))

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
# print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

print('哈哈哈哈')

