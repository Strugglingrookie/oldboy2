#_*_coding:utf-8_*_

#
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print('before yield')
#         yield b # 把函数的执行过程冻结在这一步，并且把b的值 返回给外面的next()
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# f = fib(15) #turn function into a generator
#
# next(f) #first time call next()
# next(f) #first time call next()
# next(f) #first time call next()
# next(f) #first time call next()





# def range2(n):
#
#     count = 0
#     while count < n :
#         print(count)
#         stop_flag = yield count #中断并返回
#         if stop_flag == 'stop':
#             print('stop iteration...')
#             break
#         count += 1
#
#
#
#
# r = range2(10)
#
# next(r)
# next(r)
#
# r.send('stop')
# #next(r)


#
# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了2个包子!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")



def logger(filename,channel='file'):
    """
    日志方法
    :param filename: log filename 
    :param channel:  输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
    :return: 
    """
    print('start logger')
    while True:

        msg = yield
        print("msg",msg)


# l = logger()
# l.__next__()
#
# l.send('hi ')
# l.send('hi ','file')