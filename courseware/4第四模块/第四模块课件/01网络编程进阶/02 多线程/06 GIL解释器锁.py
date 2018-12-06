# 计算密集型：用多进程
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     # print(os.cpu_count()) #本机为8核
#     start=time.time()
#     for i in range(8):
#         # p=Process(target=work) #耗时8s多
#         p=Thread(target=work) #耗时37s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))


# IO密集型：用多线程
from multiprocessing import Process
from threading import Thread
import threading
import os,time

def work():
    time.sleep(2)

if __name__ == '__main__':
    l=[]
    # print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        # p=Process(target=work) #耗时2.697多,大部分时间耗费在创建进程上
        p=Thread(target=work) #耗时2.02多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))
