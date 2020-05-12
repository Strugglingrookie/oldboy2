# # # 装饰器
# # import re
# #
# #
# # def decorator1(func):
# #     def wrapper(*args,**kwargs):
# #         print('装饰器一')
# #         func(*args,**kwargs)
# #     return wrapper
# #
# # def out(n):
# #     def decorator2(func):
# #         def wrapper(*args,**kwargs):
# #             for i in range(n):
# #                 print('装饰器%d'%i)
# #             func(*args,**kwargs)
# #         return wrapper
# #     return decorator2
# #
# # class decorator3:
# #     def __init__(self,func):
# #         self.func = func
# #
# #     def __call__(self, *args, **kwargs):
# #         return self.func(*args, **kwargs)
# #
# # @decorator1
# # def count1(a,b):
# #     print(a+b)
# #
# # @out(3)
# # def count2(a,b):
# #     print(a+b)
# #
# # @decorator3
# # def count3(a,b):
# #     print(a+b)
# #
# # # count1(1,2)
# # # count2(1,2)
# # # count3(1,2)
# #
# # '''
# # 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# # 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# # 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# # 示例 1:
# # s = "abc", t = "ahbgdc"
# # 返回 true.
# # 示例 2:
# # s = "axc", t = "ahbgdc"
# # 返回 false.
# # '''
# #
# # s = "abd"
# # t = "ahbgdc"
# #
# # def fun(s,t):
# #     my_t = iter(t)
# #     try:
# #         for i in s:
# #             while True:
# #                 tmp = next(my_t)
# #                 if tmp == i:
# #                     break
# #     except Exception as e:
# #         return False
# #     else:
# #        return True
# #
# # # print(fun(s,t))
# #
# # res = re.search(r'a*',"gfdaaasd!#%^b")
# # if res:
# #     print(res.group())
#
# # li = [10,4,6,3,8,2,5,7]
# # tmp = [4,10]
# # li[0:2] = tmp
# # print(li)
# # print(2017%4)
#
# # li = [4.3, 1.2, 5, 11, 8.444, 5.333]
# #
# #
# # def bubble_sort(l):
# #     for i in range(len(l) - 1):
# #         exchange = False
# #         for j in range(len(l) - i - 1):
# #             if l[j] > l[j + 1]:
# #                 l[j], l[j + 1] = l[j + 1], l[j]
# #                 exchange = True
# #         if not exchange:
# #             break
# #     return l
# #
# #
# # print(bubble_sort(li))
#
# # def sub_sequence1(a,b):
# #     i,j = 0,0
# #     while i<len(a) and j<len(b):
# #         if a[i] == b[j]:
# #             i+=1
# #             j+=1
# #         else:
# #             j+=1
# #     if i==len(a):
# #         return True
# #     return False
# #
# # def sub_sequence(a,b):
# #     b = iter(b)
# #     return all(i in b for i in a)
# #
# # # print(sub_sequence([1, 3, 5], [1, 2, 3, 4, 5]))
# # # print(sub_sequence([1, 4, 5], [1, 2, 3, 4, 5]))
# # # print(sub_sequence([1, 6, 5], [1, 2, 3, 4, 5]))
# #
# #
# #
# # def is_subsequence(a, b):
# #     b = iter(b)
# #     # print(b)
# #     #
# #     # gen = (i for i in a)
# #     # print(gen)
# #     #
# #     # for i in gen:
# #     #     print(i)
# #     #
# #     # gen = ((i in b) for i in a)
# #     # print(gen)
# #     #
# #     # for i in gen:
# #     #     print(i)
# #
# #     return all(((i in b) for i in a))
# #
# # print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
# # # print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
# #
# # print('哈哈哈哈')
#
#
# import requests
#
# def get_userinfo():
#     url = "https://testwechat3005.yylending.com/server"
#
#     # 校验手机号的请求，为了拿到cookies
#     check_data = {
#         "model": "user",
#         "action": "judgeInvestor",
#         "params": {
#             "accountNo": "13103290001"
#         }
#     }
#
#     # 发送验证按
#     sms_code_data = {
#         "model": "verify",
#         "action": "getSmsCode",
#         "mobile": "13103290001",
#         "type": "1",
#         "operation": "reg",
#         "captcha": "mobile",
#         "smsLogin": "true"
#     }
#
#     # 登陆
#     login_data = {
#         "model": "user",
#         "action": "smsLogin",
#         "params": {
#             "name": "13103290001",
#             "smsCode": "123456",
#             "userId": "undefined",
#             "channel": "cma",
#             "thirdSource": "",
#             "thirdId": ""
#         }
#     }
#
#     # 拿到用户信息
#     info_data = {
#         "model": "application",
#         "action": "getUserInfo",
#         "type": "baseInfo"
#     }
#
#     # 请求头
#     headers = {"content-type":"application/json;charset=UTF-8"}
#
#     # 手机号验证这个请求，主要是为了拿到cookies，下面三个请求都是基于这个cookies进行的
#     res = requests.request("post",url,json=check_data,headers=headers)
#     cookies = res.cookies
#
#     # 发送验证码
#     requests.request("post", url, json=sms_code_data, headers=headers,cookies=cookies)
#
#     # 登陆
#     requests.request("post", url, json=login_data, headers=headers,cookies=cookies)
#
#     # 拿到用户信息
#     res = requests.request("post", url, json=info_data, headers=headers, cookies=cookies).json()
#
#     return res
#
# print(get_userinfo())
#
#


# 给定一个循环递增数组a[]，有n个元素，如a[]={ 10, 13, 16, 20, 25, 2, 5, 8}，
# 给定一个元素num，找出可以把num插入到数组a[]中的位置，让插入num后的a[]仍然是循环递增的
# li = [10, 13, 16, 20, 25]
li = [10, 13, 16, 20, 25, 2, 5, 8]


def bin_search(li,num,low,high):
    while low <= high:
        mid = (low+high)//2
        if num > li[mid]:
            low = mid + 1
        else:
            high = mid -1
    return low


def insert_num(li, n,low,high):
    index = bin_search(li, n,low,high)
    if index == len(li) - 1 and li[index] < n:
        li.append(n)
    else:
        li.insert(index, n)

def circle(li, n):
    if li[-1] > li[0]:
        insert_num(li, n,0,len(li)-1)
    else:
        for i in range(len(li)-1):
            if li[i] < li[0]:
                break
        if li[0] < n:
            insert_num(li, n,0,i-1)
        else:
            insert_num(li, n,i,len(li)-1)

circle(li, 17)
circle(li, 24)
circle(li, 27)
circle(li, 9)
circle(li, 1)
circle(li, 6)
print(li)

print('testing!!')
