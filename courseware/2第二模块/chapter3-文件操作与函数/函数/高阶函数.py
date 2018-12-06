#_*_coding:utf-8_*_



#变量可以指向函数，
# 函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

# def func(x,y):
#     return x+y

# def calc(x):
#     #pass
#     return x
#
# f = calc(func)

# print(f(5,9))


def func2(x,y):

    return abs,x,y

res = func2(3,-10)

# print(res[0](res[1]+res[2]) )