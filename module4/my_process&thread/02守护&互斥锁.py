# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/22


# 守护进程 子进程设置为主进程的守护进程，主进程运行完(重点，主进程运行完！！！)，子进程也跟着死掉。
'''
from multiprocessing import Process
import time
class my_process_thread(Process):
    def run(self):
        print("%s is running" % self.name)
        time.sleep(1)
        print("%s is done" % self.name)


if __name__ == "__main__":
    p1 = my_process_thread()
    p1.daemon = True  # 设置为守护线程后，这里主线程运行完，p1就死掉了，不会打印进程1
    p1.start()
    p2 = my_process_thread()
    p2.start()
    print("主线程 is over !")
'''


# 互斥锁
'''
# 问题：竞争资源会出现数据错乱，比如多个进程竞争终端，都要打印数据，大家都在打印，数据就乱了。
from multiprocessing import Process
import time


class my_process_thread(Process):
    def run(self):
        print("%s is running 第一行" % self.name)
        time.sleep(1)
        print("%s is running 第二行" % self.name)
        time.sleep(1)
        print("%s is running 第三行" % self.name)
        time.sleep(1)
        print("%s is done" % self.name)


if __name__ == "__main__":
    for i in range(3):
        p = my_process_thread()
        p.start()
    print("主线程 is over !")


#主线程 is over !
#my_process_thread-1 is running 第一行
#my_process_thread-2 is running 第一行
#my_process_thread-3 is running 第一行
#my_process_thread-1 is running 第二行
#my_process_thread-2 is running 第二行
#my_process_thread-3 is running 第二行
#my_process_thread-1 is running 第三行
#my_process_thread-2 is running 第三行
#my_process_thread-3 is running 第三行
#my_process_thread-1 is done
#my_process_thread-2 is done
#my_process_thread-3 is done
'''

# 互斥锁的意义在于将并发变回串行，一个进程用完下个进程才可以用,数据就有序了，但是效率降低，取决你需要数据安全性还是效率。
'''
from multiprocessing import Process, Lock
import time


class My_process_lock(Process):
    def __init__(self, lock):
        super().__init__()
        self.lock = lock

    def run(self):
        self.lock.acquire()  # 申请锁
        print("%s is running 第一行" % self.name)
        time.sleep(1)
        print("%s is running 第二行" % self.name)
        time.sleep(1)
        print("%s is running 第三行" % self.name)
        time.sleep(1)
        print("%s is done" % self.name)
        self.lock.release()  # 释放锁


if __name__ == "__main__":
    lock = Lock()   # 实例化锁，子进程拿到锁才可以运行
    for i in range(3):
        p = My_process_lock(lock)
        p.start()
    print("主线程 is over !")


# 主线程 is over !
# my_process&thread-1 is running 第一行
# my_process&thread-1 is running 第二行
# my_process&thread-1 is running 第三行
# my_process&thread-1 is done
# my_process&thread-2 is running 第一行
# my_process&thread-2 is running 第二行
# my_process&thread-2 is running 第三行
# my_process&thread-2 is done
# my_process&thread-3 is running 第一行
# my_process&thread-3 is running 第二行
# my_process&thread-3 is running 第三行
# my_process&thread-3 is done
'''

# join和互斥锁的区别
# join只能让整个子进程串行，互斥锁可以让局部代码串行(比如修改数据部分串行，其他查询可以继续并行)
from multiprocessing import Process,Lock
import json
import time

def search(name):
    time.sleep(1)
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    print('<%s> 查看到剩余票数【%s】' %(name,dic['count']))

def get(name):
    time.sleep(1)
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    if dic['count'] > 0:
        dic['count']-=1
        time.sleep(3)
        json.dump(dic,open('db.txt','w',encoding='utf-8'))
        print('<%s> 购票成功' %name)
    else:
        print('<%s> 购票失败' %name)

def task(name,mutex):
    search(name)
    mutex.acquire()
    get(name)
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=('路人%s' %i,mutex))
        p.start()
        # p.join()
