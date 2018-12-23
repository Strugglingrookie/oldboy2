# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23


# 单纯的切换（在没有io的情况下或者没有重复开辟内存空间的操作），反而会降低程序的执行速度
# greenlet只是提供了一种比generator更便捷的切换方式，当切到一个任务执行时如果遇到io，那就原地阻塞，仍没解决遇到IO自动切换来提升效率的问题。
'''
from greenlet import greenlet


def sayhi(name):
    print("%s say hi 1" % name)
    g2.switch("xg")
    print("%s say hi 2" % name)
    g2.switch("xg")


def sayhello(name):
    print("%s say hello 1" % name)
    g1.switch()
    print("%s say hello 2" % name)


g1 = greenlet(sayhi)
g2 = greenlet(sayhello)
g1.switch("miller")
'''


# Gevent 是第三方库，可通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
# Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
#用法
# g1=gevent.spawn(func,1,,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，后面跟参数
# g2=gevent.spawn(func2)
# g1.join() #等待g1结束
# g2.join() #等待g2结束
# #或者上述两步合作一步：gevent.joinall([g1,g2])
# g1.value#拿到func1的返回值
'''
import gevent

def sayhi(name):
    print("%s say hi 1" % name)
    gevent.sleep(3)  # gevent 只会在遇到自己的这个sleep方法时才会切换任务，time.sleep不会
    print("%s say hi 2" % name)


def sayhello(name):
    print("%s say hello 1" % name)
    gevent.sleep(5)
    print("%s say hello 2" % name)


g1 = gevent.spawn(sayhi, "miller")
g2 = gevent.spawn(sayhello, "xg")
g1.join() 
g2.join()
print("all over!")
'''


# 上例gevent.sleep(2)模拟的是gevent可以识别的io阻塞,
# 而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了
# from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面，如time，socket模块之前
# 或者我们干脆记忆成：要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头
from gevent import monkey;monkey.patch_all()
import gevent, time

def sayhi(name):
    print("%s say hi 1" % name)
    time.sleep(3)
    print("%s say hi 2" % name)


def sayhello(name):
    print("%s say hello 1" % name)
    time.sleep(5)
    print("%s say hello 2" % name)


g1 = gevent.spawn(sayhi, "miller")
g2 = gevent.spawn(sayhello, "xg")
g1.join()
g2.join()
print("all over!")

