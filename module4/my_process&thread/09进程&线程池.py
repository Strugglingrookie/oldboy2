# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23


# 进程池/线程池
# 1、submit(fn, *args, **kwargs)
# 异步提交任务
#
# 2、map(func, *iterables, timeout=None, chunksize=1)
# 取代for循环submit的操作
#
# 3、shutdown(wait=True)
# 相当于进程池的pool.close()+pool.join()操作
# wait=True，等待池内所有任务执行完毕回收完资源后才继续
# wait=False，立即返回，并不会等待池内的任务执行完毕
# 但不管wait参数为何值，整个程序都会等到所有任务执行完毕
# submit和map必须在shutdown之前
#
# 4、result(timeout=None)
# 取得结果
#
# 5、add_done_callback(fn)
# 回调函数

'''
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread
import time, random, os


def sayhi(name):
    print("%s say hi... pid:%s; current_thread:%s" % (name, os.getpid(), current_thread().getName()))
    time.sleep(random.randint(1, 3))
    print("%s say bye... pid:%s; current_thread:%s" % (name, os.getpid(), current_thread().getName()))


if __name__ == "__main__":
    # pool = ProcessPoolExecutor(3)  # 实例化进程池，指定最大进程数为3
    pool = ThreadPoolExecutor(3)  # 实例化线程池，指定最大线程数为3
    for i in range(10):
        pool.submit(sayhi, "xg%s" % i,)
    # 关闭pool的submit功能，不可以再丢进程或线程进线程池。
    pool.shutdown(wait=True)  # 此刻统计当前pool里的所有进程或线程数，每运行完一个-1，直到等于0时，往下运行代码。等同于进程线程的join
    print("all over!")
'''



# 同步回调  开启的多线程变成了串行，拿到第一个线程的执行结果才继续往下继续运行
"""
# 钓鱼大赛，参赛者钓鱼，然后称重。
from concurrent.futures import ThreadPoolExecutor
import time, random, os


def fishing(name):
    print("%s is fishing..." % name)
    time.sleep(random.randint(2, 5))
    fish = random.randint(5, 15) * "m"
    res = {"name": name, "fish": fish}
    return res


def weigh(res):
    name = res["name"]
    size = len(res["fish"])
    print("%s 钓到的鱼大小为 %s kg" % (name, size))


if __name__ == "__main__":
    pool = ThreadPoolExecutor(3)
    res1 = pool.submit(fishing, "xt").result()  # 同步拿结果，拿到结果才继续往下走
    weigh(res1)
    res2 = pool.submit(fishing, "dj").result()
    weigh(res2)
    res3 = pool.submit(fishing, "hh").result()
    weigh(res3)
"""


# 异步回调
'''
from concurrent.futures import ThreadPoolExecutor
import time, random, os


def fishing(name):
    print("%s is fishing..." % name)
    time.sleep(random.randint(2, 5))
    fish = random.randint(5, 15) * "m"
    res = {"name": name, "fish": fish}
    return res


def weigh(pool_obj):
    res = pool_obj.result()  # 拿到线程对象的运行结果，因为是线程运行完才会调用weigh，所以马上能拿到结果
    name = res["name"]
    size = len(res["fish"])
    print("%s 钓到的鱼大小为 %s kg" % (name, size))


if __name__ == "__main__":
    pool = ThreadPoolExecutor(3)
    pool.submit(fishing, "xt").add_done_callback(weigh)  # 当线程执行完后，将线程对象当参数传给weigh
    pool.submit(fishing, "dj").add_done_callback(weigh)
    pool.submit(fishing, "hh").add_done_callback(weigh)
'''


# map用法：
'''
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import os,time,random
def task(n):
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':

    executor=ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task,range(1,12)) #map取代了for+submit
'''
