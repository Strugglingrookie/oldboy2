# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os,time,random
#
# def task(name):
#     print('name:%s pid:%s run' %(name,os.getpid()))
#     time.sleep(random.randint(1,3))
#
#
# if __name__ == '__main__':
#     # pool=ProcessPoolExecutor(4)
#     pool=ThreadPoolExecutor(5)
#
#     for i in range(10):
#         pool.submit(task,'egon%s' %i)
#
#     pool.shutdown(wait=True)
#
#
#     print('主')


from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread
import os,time,random

def task():
    print('name:%s pid:%s run' %(currentThread().getName(),os.getpid()))
    time.sleep(random.randint(1,3))


if __name__ == '__main__':
    pool=ThreadPoolExecutor(5)

    for i in range(10):
        pool.submit(task,)

    pool.shutdown(wait=True)


    print('主')



    