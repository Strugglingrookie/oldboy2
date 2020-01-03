# 生产者消费者模型
'''
from multiprocessing import Process,Queue
import time,random
def consumer(q,name):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[43m%s 吃 %s\033[0m' %(name,res))

def producer(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,'星爷','包子'))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,'孟达'))

    #开始
    p1.start()
    c1.start()
    print('主')


# 此时的问题是主进程永远不会结束，原因是：生产者p在生产完后就结束了，但是消费者c在取空了q之后，则一直处于死循环中且卡在q.get()这一步。
# 解决方式无非是让生产者在生产完毕后，往队列中再发一个结束信号，这样消费者在接收到结束信号后就可以break出死循环

from multiprocessing import Process,Queue
import time,random
def consumer(q,name):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('\033[43m%s 吃 %s\033[0m' %(name,res))

def producer(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=producer,args=(q,'星爷','包子'))

    c1=Process(target=consumer,args=(q,'华仔'))

    #开始
    p1.start()
    c1.start()

    p1.join()
    q.put(None)
    print('主')


# 但上述解决方式，在有多个生产者和多个消费者时，我们则需要用一个很low的方式去解决,有几个消费者就需要发送几次结束信号：相当low,例如

from multiprocessing import Process,Queue
import time,random,os
def consumer(q,name):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('\033[43m%s 吃 %s\033[0m' %(name,res))

def producer(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,'egon1','包子'))
    p2=Process(target=producer,args=(q,'egon2','骨头'))
    p3=Process(target=producer,args=(q,'egon3','泔水'))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,'alex1'))
    c2=Process(target=consumer,args=(q,'alex2'))

    #开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    q.put(None)
    print('主')

其实我们的思路无非是发送结束信号而已，有另外一种队列提供了这种机制

JoinableQueue([maxsize])

这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
参数介绍

maxsize是队列中允许最大项数，省略则无大小限制。
方法介绍

JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
q.task_done()：消费者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止
基于JoinableQueue实现生产者消费者模型
'''
from multiprocessing import Process, JoinableQueue
import time, random


def consumer(q, name):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))

        # 发送信号给q.join()，已经从队列中取走一个数据并处理完毕
        q.task_done()


def producer(q, name, food):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))

    # 等到消费者把自己放入队列中的所有数据都取走，生产者才结束
    q.join()


if __name__ == '__main__':
    q = JoinableQueue()  # 使用JoinableQueue()

    # 生产者们:即厨师们
    p1 = Process(target=producer, args=(q, '星爷1', '包子'))
    p2 = Process(target=producer, args=(q, '星爷2', '骨头'))
    p3 = Process(target=producer, args=(q, '星爷3', '泔水'))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q, '华仔1'))
    c2 = Process(target=consumer, args=(q, '华仔2'))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    # 1、主进程等生产者p1、p2、p3结束
    # 2、而p1、p2、p3是在消费者把所有数据都取干净之后才会结束
    # 3、所以一旦p1、p2、p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，因而需要将消费者们设置成守护进程
    print('主')
