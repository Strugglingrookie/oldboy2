import queue

# q=queue.Queue(3) #先进先出->队列
#
# q.put('first')
# q.put(2)
# q.put('third')
# # q.put(4)
# # q.put(4,block=False) #q.put_nowait(4)
# # q.put(4,block=True,timeout=3)
#
#
# #
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q.get(block=False)) #q.get_nowait()
# # print(q.get_nowait())
#
# # print(q.get(block=True,timeout=3))


# q=queue.LifoQueue(3) #后进先出->堆栈
# q.put('first')
# q.put(2)
# q.put('third')
#
# print(q.get())
# print(q.get())
# print(q.get())

#
# q=queue.PriorityQueue(3) #优先级队列
#
# q.put((10,'one'))
# q.put((40,'two'))
# q.put((30,'three'))
#
# print(q.get())
# print(q.get())
# print(q.get())