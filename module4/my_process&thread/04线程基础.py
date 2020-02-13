# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/22


# 进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。
# 公司=Cpu，部门=进程，开发人员=线程
# 部门隔离数据，财务部的财务数据不会给开发部门看，开发部门不是实际干活的单位，部门里的开发人员才干活，一个部门至少要有一个人才能干活，这就是主线程。
# 多线程（即多个控制线程）的概念是，在一个进程中存在多个线程，多个线程共享该进程的地址空间，也就是说，同一个进程的线程是共享进程数据的
# 1.同一个进程内的多个线程共享该进程内的地址资源
# 2.创建线程的开销要远小于创建进程的开销（创建进程，需要申请内存，而且建至少一个线程来干活；建线程，只是在进程内造一个线程，无需申请内存）
# Thread实例对象的方法
#   # isAlive(): 返回线程是否活动的。
#   # getName(): 返回线程名。
#   # setName(): 设置线程名。
# threading模块提供的一些方法：
#   # threading.currentThread(): 返回当前的线程变量。
#   # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
#   # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# 跟多进程一样，开启线程也是两种方式
'''
from threading import Thread, currentThread, enumerate, activeCount
import time
import os

# 方式一：
def task(name):
    print("%s is running...,pid: %s;" % (name, os.getpid()))  # 拿到进程pid
    time.sleep(1)
    print("%s is done..." % name)
    print("子线程%s 当前的线程名：%s" % (name, currentThread()))


# 方式二
class CreateThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # 如果没指定名字，会有自己的名称，类名+编号

    def run(self):
        print("%s is running...,pid: %s;" % (self.name, os.getpid()))
        time.sleep(3)
        print("%s is done..." % self.name)


if __name__ == "__main__":
    # 方式一：
    p1 = Thread(target=task, args=("方式一子线程",))
    p1.start()  # 告诉操作系统帮忙开启新的子线程，操作系统直接创建一个子线程，数据和进程共享
    print(p1.name)  # 线程名称，Thread-编号 也可以自己指定
    # p4 = Thread(target=task, name="我是方式一的子线程4444", args=("方式一子线程4",))  # name 指定线程名称
    # print(p4.name)

    # 方式二：
    p2 = CreateThread("方式二子线程1")
    p3 = CreateThread("方式二子线程2")
    p2.start()
    p3.start()

    print(p1.is_alive())  # true
    print(p3.is_alive())  # true
    print("p1 join之前的线程数 %s" % activeCount())
    print("p1 join之前的线程对象列表 %s" % enumerate())
    p1.join()  # 等待子线程p1运行结算才往下运行
    print("p1 join之后的线程数 %s" % activeCount())
    print("p1 join之后的线程对象列表 %s" % enumerate())
    print(p1.is_alive())  # 判断线程存活状态，因为上面join了，所以p1已经是结束了的，只是保留了状态，所以false
    print("主线程结束！ pid: %s" % os.getpid())  # 拿到进程pid
    print("主线程的线程名：%s" % currentThread())
'''



# 进程与线程的区别
'''
# 1、开进程的开销远大于开线程
import time
from threading import Thread
from multiprocessing import Process

def piao(name):
    print('%s piaoing' %name)
    time.sleep(2)
    print('%s piao end' %name)

if __name__ == '__main__':
    # p1=Process(target=piao,args=('egon',))
    # p1.start()

    t1=Thread(target=piao,args=('egon',))
    t1.start()
    print('主线程')



# 2、同一进程内的多个线程共享该进程的地址空间
from threading import Thread
from multiprocessing import Process

n=100
def task():
    global n
    n=0

if __name__ == '__main__':
    # p1=Process(target=task,)
    # p1.start()
    # p1.join()

    t1=Thread(target=task,)
    t1.start()
    t1.join()

    print('主线程',n)


# 3、瞅一眼pid
from threading import Thread
from multiprocessing import Process,current_process
import os

def task():
    # print(current_process().pid)
    print('子进程PID:%s  父进程的PID:%s' %(os.getpid(),os.getppid()))

if __name__ == '__main__':
    p1=Process(target=task,)
    p1.start()

    # print('主线程',current_process().pid)
    print('主线程',os.getpid())


from threading import Thread
import os

def task():
    print('子线程:%s' %(os.getpid()))

if __name__ == '__main__':
    t1=Thread(target=task,)
    t1.start()

    print('主线程',os.getpid())
'''



# 守护线程
# 无论是进程还是线程，都遵循：守护xxx会等待主xxx运行完毕后被销毁
# 需要强调的是：运行完毕并非终止运行
# 强调：对进程和线程来说，运行完毕都不是指主代码运行完毕，而是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕，从而主进程才算完毕
# 1、主进程达到上述条件后结束（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束
# 2、主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。
# 因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。
'''
from threading import Thread
from multiprocessing import Process
import time


def syahi(name):
    time.sleep(1)
    print('%s say hi' % name)


def sayhello(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    # t1=Thread(target=syahi,args=('Thread',))
    t2=Thread(target=sayhello,args=('Thread',))
    # t1.setDaemon(True)  # 必须在t.start()之前设置
    # t1.start()
    t2.start()

    p1=Process(target=syahi, args=('Process',))
    # p2=Process(target=sayhello, args=('Process',))
    p1.daemon = True  # 必须在t.start()之前设置
    p1.start()
    # p2.start()

    # print('主线程')
    # print(t1.is_alive())
    print(t2.is_alive())

    # print('主进程')
    print(p1.is_alive())
    # print(p2.is_alive())
'''


# 互斥锁，

# 下面的代码如果不加互斥锁的话，会n结果是99，因为每个线程都到了time.sleep(0.1)之前拿到的n都是100
from threading import Thread,Lock
import time
n = 100


def task():
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print('主', n)
