# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/22


# 开启进程的两种方式：

from multiprocessing import Process
import time
import os


# 方式一：
def task(name):
    print("%s is running...,pid: %s; ppid: %s " % (name, os.getpid(), os.getppid()))  # 拿到进程pid以及父进程pid
    time.sleep(1)
    print("%s is done..." % name)


# 方式二
class CreateProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name  # 如果没指定名字，会有自己的名称，类名+编号

    def run(self):
        print("%s is running...,pid: %s; ppid: %s " % (self.name, os.getpid(), os.getppid()))
        time.sleep(3)
        print("%s is done..." % self.name)


if __name__ == "__main__":
    # 方式一：
    p1 = Process(target=task, args=("方式一子进程",))
    p1.start()  # 告诉操作系统帮忙开启新的子进程，操作系统开辟一个新的内存空间给子进程使用，并把主进程的内存数据复制到子进程的内存空间里
    print(p1.name)  # 进程名称，Process-编号 也可以自己指定
    p4 = Process(target=task, name="我是方式一的子进程4444", args=("方式一子进程4",))
    print(p4.name)

    # 方式二：
    p2 = CreateProcess("方式二子进程1")
    p3 = CreateProcess("方式二子进程2")
    p2.start()
    p3.start()

    print(p1.is_alive())  # true
    print(p3.is_alive())  # true
    p3.terminate()  # 杀调子进程，将子进程变成僵尸进程。实质是发送杀掉进程命令给操作系统，操作系统回收内存资源，保留子进程状态信息
    p1.join()  # 等待子进程p1运行结算才往下运行
    print("after terminate p3:", p3.is_alive())  # false
    print(p1.pid, p2.pid, p3.pid)  # 查看子进程的pid
    print(p1.is_alive())  # 判断进程存活状态，因为上面join了，所以p1已经是结束了的，只是保留了状态，所以false
    print("主进程结束！ pid: %s" % os.getpid())  # 拿到进程pid


# 僵尸进程：子进程运行完后，内存空间被操作系统收回，但是进程状态需要保留给父进程查看；
# 也就是说子进程实际上是死了，但是还留有状态信息给父进程可查，等父进程也运行完后，才会清理掉这个已经死掉的子进程状态信息。

# 孤儿进程：父进程挂掉后，子进程还在运行，这个时候就由操作系统的 init(linux操作系统中国呢所有进程的父进程) 进程监管/回收这些子进程


