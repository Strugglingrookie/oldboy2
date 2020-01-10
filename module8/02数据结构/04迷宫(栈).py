'''
给一个二维列表，表示迷宫（0表示通道，1表示围墙）。给出算法，求一条走出迷宫的路径。
回溯法
思路：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点。
使用栈存储当前路径
'''

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, var):
        self.stack.append(var)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack.pop()

    def gettop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def find_way(maze):
    size = len(maze[0])
    start = size + 1
    end = ((len(maze) - 1) * size - 1) - 1
    stack = Stack()
    stack.push(start)

    # 如果栈不为空，一直循环找坐标
    while not stack.is_empty():
        #获取当前坐标
        current = stack.gettop()

        # 如果当前的坐标等于终点，输出路径，结束
        if current == end:
            loads = []
            while not stack.is_empty():
                cur = stack.pop()
                # 正确路径标为3 方便后面打印查看
                maze[cur // size][cur % size] = 3
                tmp = [cur // size,cur % size]
                loads.insert(0,tmp)
            return loads

        # urdl 存 上 右 下 左 的坐标
        urdl = [current - size, current + 1, current + size, current - 1]

        # 循环上 右 下 左 的坐标，找到下一个可以走的坐标
        for load in urdl:
            val = maze[load // size][load % size]
            if val == 0:
                stack.push(load)
                # 走过的路标为2
                maze[load // size][load % size] = 2
                break

        # 如果没找到，当前坐标出栈，进入下次循环
        if current == stack.gettop():
            stack.pop()

    # 如果栈为空，则没有路径
    else:
        return False

res = find_way(maze)
print(res)
for r in maze:
        for c in r:
            if c==3:
                print('\033[0;31m'+"*"+" "+'\033[0m',end="")
            elif c==2:
                print('\033[0;32m'+"#"+" "+'\033[0m',end="")
            elif c==1:
                print('\033[0;;40m'+" "*2+'\033[0m',end="")
            else:
                print(" "*2,end="")
        print()

