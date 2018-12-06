# 1、开进程的开销远大于开线程
# import time
# from threading import Thread
# from multiprocessing import Process
#
# def piao(name):
#     print('%s piaoing' %name)
#     time.sleep(2)
#     print('%s piao end' %name)
#
# if __name__ == '__main__':
#     # p1=Process(target=piao,args=('egon',))
#     # p1.start()
#
#     t1=Thread(target=piao,args=('egon',))
#     t1.start()
#     print('主线程')



# 2、同一进程内的多个线程共享该进程的地址空间
# from threading import Thread
# from multiprocessing import Process
#
# n=100
# def task():
#     global n
#     n=0
#
# if __name__ == '__main__':
#     # p1=Process(target=task,)
#     # p1.start()
#     # p1.join()
#
#     t1=Thread(target=task,)
#     t1.start()
#     t1.join()
#
#     print('主线程',n)


# 3、瞅一眼pid
# from threading import Thread
# from multiprocessing import Process,current_process
# import os
#
# def task():
#     # print(current_process().pid)
#     print('子进程PID:%s  父进程的PID:%s' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p1=Process(target=task,)
#     p1.start()
#
#     # print('主线程',current_process().pid)
#     print('主线程',os.getpid())


from threading import Thread
import os

def task():
    print('子线程:%s' %(os.getpid()))

if __name__ == '__main__':
    t1=Thread(target=task,)
    t1.start()

    print('主线程',os.getpid())