# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/22


# 1、思考开启进程的方式一和方式二各开启了几个进程？
# 2、进程之间的内存空间是共享的还是隔离的？下述代码的执行结果是什么？
# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     global n
#     n=0
#     print('子进程内: ', n)
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     p.join()
#     print('主进程内: ', n)
# 3、基于多进程实现并发的套接字通信？
# 将建立链接和收发数据分开写，循环等待链接，来一个就启动一个进程收发数据
# 4、思考每来一个客户端，服务端就开启一个新的进程来服务它，这种实现方式有无问题？
# 没有限制，但内存有限制，当链接数达到一定量，内存会撑爆



# # join
# # 1、改写下列程序，分别别实现下述打印效果
# from multiprocessing import Process
# import time
# import random
#
#
# def task(n):
#     time.sleep(random.randint(1, 3))
#     print('-------->%s' % n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')
#
# # 效果一：保证最先输出-------->4
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')
#
# # 效果二：保证最后输出-------->4
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     for p in [p1, p2, p3]:
#         p.join()
#     print('-------->4')
#
# # 效果三：保证按顺序输出
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print('-------->4')
#
# # 2、判断上述三种效果，哪种属于并发，哪种属于串行？
# # 前1/2是并发，最后是串行


# 思考下列代码的执行结果有可能有哪些情况？为什么？
from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")