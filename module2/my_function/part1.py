# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/25


# import chardet
# f= open("a.txt","rb")
# data = f.read()
# print(chardet.detect(data))
# >> {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}

# 非固定参数，元祖
# def alarm(msg,*users):
#     for i in users:
#         print(msg,i)
# alarm("回家吃饭了","qwe","ert")
# lis=["qwe","ert"]
# # 如果传列表，必须在前面加*，才会被打包成元祖，否则整个列表会作为元祖的一个元素进行打包
# alarm("回家吃饭了",["qwe","ert"])  #整个列表会作为元祖的一个字典进行打包   >>回家吃饭了 ['qwe', 'ert']
# alarm("回家吃饭了",*["qwe","ert"])
# alarm("回家吃饭了",*lis)

# 非固定参数，字典，总体上和上述原则是一样的，定义用 **kwargs，用的时候如果传字典需要加 **kwargs,不传字典可以直接传关键字参数(key=value)，会自动加到字典里
# def func(name,*args,**kwargs):
#     print(name,args,kwargs)
# func("alex",degree="primary",age=18)  #>>:alex () {'degree': 'primary', 'age': 18}
# func("alex",{"degree":"primary","age":8})  #>>:alex ({'degree': 'primary', 'age': 8},) {}
# func("alex",**{"degree":"primary","age":8})  #>>:alex () {'degree': 'primary', 'age': 8}

# #代码在定义变量的时候，作用域已经时生成，不管以后在哪个地方调用，作用域都是在定义的位置从内往外找变量
# age = 18
# def func1():
#     age = 73
#     def func2():
#         print(age)
#     return func2
# val = func1()
# val() #>>: 调用的时候，会回到函数定义的地方，从内往外找变量age，所以这里输出的结果是73

# lambda
# lis2 = list(map(lambda x:x*x ,list(range(10))))
# lis3 = list(filter(lambda x:x%2 ,list(range(10))))
# print(lis2)
# print(lis3)

#递归,返回值，返回最里面那一层的计算值，必须要用两个return，最下面那个return是返回最后一层运算的值，上面那个return，是把返回的这个值一层层往最外面传递
# def func(n,count):
#     print(n,count)
#     if count < 5:
#         return func(n/2,count+1)
#     return n
# print(func(64,1))

# menus = [
#     {
#         "text":"beijing",
#         "children":[
#             {"text":"chaoyang","children":[]},
#             {"text":"changping","children":[
#                 {"text":"shahe","children":[]},
#                 {"text":"huilongguang","children":[]}
#             ]}
#         ]
#     },
# {
#         "text":"shanghai",
#         "children":[
#             {"text":"baoshan","children":[]},
#             {"text":"jinshan","children":[]}
#         ]
#     }
# ]
# #1.打印所有节点
# def fun1(lis):
#     for i in lis:
#         if i.get("text"):
#             print(i["text"])
#         if i.get("children"):
#             fun1(i["children"])
# fun1(menus)
# #2.输入节点名称，找到就返回true
# find_name = "shahe"
# def fun2(name,lis):
#     for i in lis:
#         if i.get("text") == name:
#             return True
#         elif i.get("children"):
#             return fun2(name,i["children"])
# print(fun2(find_name,menus))


#eval exec
# 1.eval只能运行单行代码，exec可以运行多行代码
# 2.eval可以接收返回值，exec接收不到

#zip函数
# a=[1,2,3,4,5]
# b=['a','b','c']
# print(list(zip(a,b)))     #>>:[(1, 'a'), (2, 'b'), (3, 'c')]

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

print(fac(4))



