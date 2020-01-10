'''
队列(Queue)是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除。
进行插入的一端称为队尾(rear)，插入动作称为进队或入队
进行删除的一端称为队头(front)，删除动作称为出队
队列的性质：先进先出(First-in, First-out)

队列的实现方式——环形队列
环形队列：当队尾指针front == Maxsize + 1时，再前进一个位置就自动到0.
队首指针前进1：front = (front + 1) % MaxSize
队尾指针前进1：rear = (rear + 1) % MaxSize
队空条件：rear == front
队满条件：(rear + 1) % MaxSize == front
'''


class MyQueue:
    def __init__(self, size=100):
        # size+1 是因为有一个位置是不存元素的
        self.queue = [0 for _ in range(size + 1)]
        self.size = size + 1
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = MyQueue(3)
print(q.is_empty())  # True
print(q.is_filled())  # False
for i in range(3):
    q.push(i)
print(q.is_empty())  # False
print(q.is_filled())  # True
for i in range(3):
    print(q.pop())  # 0 1 2
print(q.is_empty())  # True
print(q.is_filled())  # False
