# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/22


# 队列
# 进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的
# 创建队列的类（底层就是以管道和锁定的方式实现）：
# Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。

# maxsize是队列中允许最大项数，省略则无大小限制。但需要明确：
#     1、队列内存放的是消息而非大数据
#     2、队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小

# from multiprocessing import Queue
# q = Queue(3)
#
# q.put(123)  # 往队列里塞一个数据，可以是任何数据类型
# q.put([4, 5, 6])
# print(q.full())  # 判断队列大小是否已经达到最大项数，这里才塞了俩数据，所以false
# q.put({"a": "apple"})
# print(q.full())  # 已经达到最大项数了，True
# print(q.empty())  # 判断队列里的是否不存在数据了，这里队列了有三数据，所以为false
#
# print(q.get())  # 根据先进先出原则，从队列里取一个数据
# print(q.get())
# print(q.get())
# print(q.empty())  # True


# 生产者/消费者模型
# from multiprocessing import Queue
# from multiprocessing import Process
# import time
#
#
# def producer(name, q):
#     for i in range(5):
#         time.sleep(0.5)
#         res = "%s生产的馒头%s" % (name, i)
#         q.put(res)
#         print(res)
#
#
# def consumer(name, q):
#     while True:
#         time.sleep(0.2)
#         res = q.get()
#         if not res:
#             break
#         print("%s 吃了 %s" % (name, res))
#
#
# if __name__ == "__main__":
#     q = Queue()
#     p_lis = []
#     for i in range(3):
#         p = Process(target=producer, args=("xg%s" % i, q))
#         p_lis.append(p)
#         p.start()
#     s = Process(target=consumer, args=("yy", q))
#     s.start()
#     for p in p_lis:
#         p.join()
#     q.put(None)  # 注意，有几个消费者就要发送几个None
#     print("over")


# JoinableQueue 的使用  可以用join方法的Queue
# JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
# q.task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
# q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止
from multiprocessing import JoinableQueue
from multiprocessing import Process
import time


def producer(name, q):
    for i in range(5):
        time.sleep(0.5)
        res = "%s生产的馒头%s" % (name, i)
        q.put(res)
        print(res)
    q.join()  # 等待q结束(即q队列数据全部调用了q.task_done()方法，才往下继续运行代码)


def consumer(name, q):
    while True:
        time.sleep(0.2)
        res = q.get()
        print("%s 吃了 %s" % (name, res))
        q.task_done()  # 没消费一个数据，调用一次task_done方法，为了给join方法用


if __name__ == "__main__":
    q = JoinableQueue()
    p_lis = []
    for i in range(3):
        p = Process(target=producer, args=("xg%s" % i, q))
        p_lis.append(p)
        p.start()
    s = Process(target=consumer, args=("yy", q))
    s.daemon = True  # 主线程运行完，就销毁掉生产者的进程
    s.start()
    for p in p_lis:
        p.join()
    print("over")  # 走到这一步说明，生产者已经运行完了，生产者运行完，代表队列里的数据都调用了task_done方法，也就是消费者运行也结束了

