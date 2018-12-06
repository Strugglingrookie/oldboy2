#_*_coding:utf-8_*_


#匿名函数

# def calc(x,y):
#     if x < y :
#         return x*y
#     else:
#         return x/y
#
#
# func = lambda x,y: x*y if x < y else x/y #声明一个匿名函数
#
#
# print(calc(16,8) )
# print(func(16,8) )

data = list(range(10))
print(data)

# for index,i in enumerate(data):
#     data[index] =i*i
#
# print(data)

def f2(n):
    return n*n

print(list(map(lambda x:x*x, data)))

#1. 节省代码量
# 2. 看着高级