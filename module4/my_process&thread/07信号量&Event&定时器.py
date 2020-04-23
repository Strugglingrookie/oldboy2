# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23


# 信号量
# 互斥锁或者递归锁都只能在一个时间点为同一个线程服务，一个萝卜一个坑。但是多个萝卜可以同时占用多个坑就没办法了，这里就用到了信号量。
# 信号量，体现在量，批量，也就是说支持同一时间点可以给多个线程用，原理实际是计数器，占用一个-1，释放一个+1，计数不能小于0。
# Semaphore管理一个内置的计数器，每当调用acquire()时内置计数器-1；调用release() 时内置计数器+1；
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
'''
from threading import Thread, Semaphore, current_thread
import time,datetime
se = Semaphore(3)  # 最多只能同时占用3次


def toilet():
    # 用法同文件操作，将打开和关闭合并在with语法里。  等价于  se.acquire()  se.release()
    with se:
        thread_name = current_thread().getName()
        now = datetime.datetime.now()
        print("%s go in，%s: " % (thread_name,now),end='\n')
        time.sleep(3)


if __name__ == "__main__":
    for i in range(10):
        t = Thread(target=toilet)
        t.start()
'''


# Event
# event.isSet()：返回event的状态值；
# event.wait()：如果 event.isSet()==False将阻塞线程；
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
# event.clear()：恢复event的状态值为False。
'''
from threading import Thread, Event
import time
e = Event()

def student(name):
    print("%s is learning" % name)
    e.wait(10)  # 一直等event.set()，最多等10秒
    print("%s is playing" % name)

def teacher(name):
    print("%s is teaching" % name)
    time.sleep(2)
    print("%s said class over!" % name)
    e.set()


if __name__ == "__main__":
    for i in range(3):
        s = Thread(target=student, args=(i,))
        s.start()
    t = Thread(target=teacher,args=('teacher',))
    t.start()
'''


# 定时器  定时执行任务

from threading import Timer


def toilet(name):
    print("%s go in" % name)


if __name__ == "__main__":
    for i in range(10):
        t = Timer(3, toilet, args=("xg %s" % i,))  # 3秒后 启动toilet
        t.start()


from threading import Timer
import random

class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self,interval=5):
        self.cache=self.make_code()
        print(self.cache)
        self.t=Timer(interval,self.make_cache)
        self.t.start()

    def make_code(self,n=4):
        res=''
        for i in range(n):
            s1=str(random.randint(0,9))
            s2=chr(random.randint(65,90))
            res+=random.choice([s1,s2])
        return res

    def check(self):
        while True:
            code=input('请输入你的验证码>>: ').strip()
            if code.upper() == self.cache:
                print('验证码输入正确')
                self.t.cancel()
                break


obj=Code()
obj.check()


