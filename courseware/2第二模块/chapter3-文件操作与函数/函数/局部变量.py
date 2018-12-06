# _*_coding:utf-8_*_



# 局部变量

#
# names = ['Alex','Black Girl','Peiqi']
#
#
# def change_name():
#     global  names
#     names = [12,3,4]
#     print(names)
#
# change_name()
# print(names)





# 嵌套函数

# def func1():
#     print('alex')
#
#     def func2():
#         print('eric')
#
#     func2()

# 1. func1() # alex
# func1()

# 2. func1()
# func1()
# =====> 1. 函数内部可以再次定义函数。2. 执行需要被调用 ，《＝＝＝＝＝

# age = 19
#
# def func1():
#     age = 73
#     def func2():
#         print(age)
#     func2()
#
# func1()




#
# age = 19
#
# def func1():
#
#     def func2():
#         print(age)
#
#     age = 73
#     func2()
#
# func1()



# age = 19
# def func1():
#     global age
#     def func2():
#         print(age)
#     age = 73
#     func2()
# func1()
# print(age)


# 3. func1() #
# func1()
# 4. func1()


# 作用域

# Python中函数就是一个作用域（JavaScript）,局部变量放置在其作用域中
# C＃ Java中作用域｛｝
# 代码定义完成后，作用域已经生成，作用域链向上查找

# age = 18
#
# def func1():
#     age = 73
#     def func2():
#         print(age)
#
#     return 666
#
# val = func1()
# print(val)



# age = 18
#
# def func1():
#     age = 73
#     def func2():
#         print(age)
#
#     return func2
#
# val = func1()
# val()

# 什么结果？
# 函数名返回值









