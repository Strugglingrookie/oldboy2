# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:51
# @Author  : Xiao


# 1、简述计算机操作系统中的“中断”的作用？
# 中断是指在计算机执行期间，系统内发生任何非寻常的或非预期的急需处理事件，使得CPU暂时中断当前正在执行的程序而转去执行相应的时间处理程序。
# 待处理完毕后又返回原来被中断处继续执行或调度新的进程执行的过程。中断加大了操作系统的灵活性。

# 2、简述计算机内存中的“内核态”和“用户态”；
# 内核态管理硬件资源，用户态为应用程序员写的应用程序提供系统调用接口。

# 3、进程间通信方式有哪些？
# 队列，管道，信号量，套接字。

# 4、简述你对管道、队列的理解；
# 管道通常指无名管道
# 1、它是半双工的（即数据只能在一个方向上流动），具有固定的读端和写端
# 2、它只能用于具有亲缘关系的进程中通信（也就是父与子进程或者兄弟进程之间）
# 3、数据不可反复读取了，即读了之后欢喜红区中就没有了
# 消息队列
# 1、消息队列是面向记录的，其中的消息具有特定的格式以及特定的优先级
# 2、消息队列独立于发送与接收进程。进程终止时，消息队列及其内容不会被删除。
# 3、消息队列可以实现消息随机查询。

# 5、请列举你知道的进程间通信方式；
# 队列,信号量,Event事件,定时器Timer,线程queue,进程池线程池,异步调用+回调机制

# 6、什么是同步I/O，什么是异步I/O？
# 同步IO指的是同步传输 ，当发送一个数据请求时，会一直等待，直到有返回结果为止
# 异步IO指的是异步传输 ，当发送一个数据请求时，会立即去处理别的事情，当有数据处理完毕后，会自动的返回结果
# 一般同步传输能保证数据正确性 ，而异步能最大化性能。

# 7、请问multiprocessing模块中的Value、Array类的作用是什么？举例说明它们的使用场景
# 通常，进程之间彼此是完全孤立的，唯一的通信方式是队列或者管道，但是可以使用两个对象来表示共享数据。
# 子进程继承父进程的全局变量，而且是以复制的形式完成，所以子进程修改后的全局变量只对自己和自己的子进程有影响。
# 父子进程不共享这些全局变量，也就是说：父进程中对全局变量的修改不影响子进程中的全局变量，同理，子进程也不影响父进程的。
# multiprocessing模块中的Value、Array类就是解决进程间数据共享的问题的
# Value函数返回一个shared memory包装类，其中包含一个ctypes对象  一般 整数用 i, 字符用 c，浮点数用 d 就可以了
# Array函数返回一个shared memory包装类，其中包含一个数组，字符串需要用 Array 来传递

# 8、请问multiprocessing模块中的Manager类的作用是什么？与Value和Array类相比，Manager的优缺点是什么？
# Manager类的作用共享资源，manger的的优点是可以在poor进程池中使用，缺点是windows下环境下性能比较差，
# 因为windows平台需要把Manager.list放在if name='main'下，而在实例化子进程时，必须把Manager对象传递给子进程，
# 否则lists无法被共享，而这个过程会消耗巨大资源，因此性能很差。

# 9、写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；
'''
import time
from threading import Thread, currentThread
def sayhi():
    print("%s sayhi..." % currentThread().getName())
t_lis = []
for i in range(10):
    t = Thread(target=sayhi)
    t_lis.append(t)
time.sleep(10)
for t in t_lis:
    t.start()
'''

# 10、写一个程序，包含十个线程，同时只能有五个子线程并行执行；
"""
import time
from threading import currentThread
from concurrent.futures import ThreadPoolExecutor
def sayhi():
    print("%s say hi..." % currentThread().getName())
    time.sleep(3)
    print("%s say bye..." % currentThread().getName())
pool = ThreadPoolExecutor(5)
for i in range(10):
    pool.submit(sayhi)
pool.shutdown(wait=True)
print("all over")
"""

# 11、写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序；
# pass

# 12、写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求；

import socketserver
class Myhandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                if not self.data:
                    break
                print(self.data)
                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())  # sendall是重复调用send.
        except Exception as e:
            print(e)

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8089),Myhandler)
    server.serve_forever()
