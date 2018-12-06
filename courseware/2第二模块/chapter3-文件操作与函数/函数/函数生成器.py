#_*_coding:utf-8_*_



def range2(n):

    count = 0
    while count < n:
        print('count',count)
        count += 1
        sign = yield count  # return
        if sign == 'stop':
            print("---sign", sign)
            break
        print('sin...',sign)
    return 3333

new_range = range2(3)

# n1=next(new_range)
next(new_range)
new_range.send(None)
#new_range.send("stop")
#1. 唤醒并继续执行
#2. 发送一个信息到生成 器内部


#
#
# python 2
#
# 	range = list
# 	xrange = 生成器
#
# python 3
# 	range = 生成器
# 	xrange  没有
#
# 生成器的创建方式
# 	1. 列表 生成 式（）
# 	2. 函数
#
#
# 	yield vs return
#
# 	return  返回 并中止function
# 	yield 返回 数据 ，并冻结当前的执行过程 。。。
#
#
# 	next 唤醒冻结的函数执行过程，继续执行，直到遇到下一个yield
#
#
# 函数有了yield之后
# 	1. 函数名加()就变得到了一个生成器，
# 	2. return 在生成器里， 代表 生成器的中止， 直接 报错
#
# next
# 	唤醒 生成器并继续 执行
# send("stop")
# 	#1. 唤醒并继续执行
# 	#2. 发送一个信息到生成 器内部
#
