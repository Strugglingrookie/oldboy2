# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/23


import queue

# 先进先出
q = queue.Queue(3)

q.put(1)
q.put(2)
q.put(3)
# q.put(4)  # 再放阻塞，等待队列消费
# q.put(4，block = False)  # 不阻塞，强制放数据，如果满的情况下直接报错  等价与 q.put_nowait(4)
# q.put(4，block = True)  # 阻塞，等待放数据，如果满的情况下阻塞，默认是True
# q.put(4, block=True, timeout=3)  # 阻塞等待3秒，3秒还在阻塞，强制放数据，满的情况下报错
print(q.full())
print(q.empty())

print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 再拿阻塞，等待队列新增数据  block timeout同put
print(q.full())
print(q.empty())

# 后进先出  同堆栈原理
q = queue.LifoQueue(3)

q.put(1)
q.put(2)
q.put(3)
# q.put(4)  # 再放阻塞，等待队列消费
# q.put(4，block = False)  # 不阻塞，强制放数据，如果满的情况下直接报错  等价与 q.put_nowait(4)
# q.put(4，block = True)  # 阻塞，等待放数据，如果满的情况下阻塞，默认是True
# q.put(4, block=True, timeout=3)  # 阻塞等待3秒，3秒还在阻塞，强制放数据，满的情况下报错
print(q.full())
print(q.empty())

print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 再拿阻塞，等待队列新增数据  block timeout同put
print(q.full())
print(q.empty())

# 优先级进出  优先级越小的先出
q = queue.PriorityQueue(3)

q.put([50, 1])
q.put([20, 2])
q.put([30, 3])
# q.put([50, 4])  # 再放阻塞，等待队列消费
print(q.full())
print(q.empty())

print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 再拿阻塞，等待队列新增数据  block timeout同put
print(q.full())
print(q.empty())