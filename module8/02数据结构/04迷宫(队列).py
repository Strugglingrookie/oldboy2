'''
给一个二维列表，表示迷宫（0表示通道，1表示围墙）。给出算法，求一条走出迷宫的路径。
思路：从一个节点开始，寻找所有接下来能继续走的点，继续不断寻找，直到找到出口。
使用队列存储当前正在考虑的节点
'''
from collections import  deque

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

def mase_queue(maze):
    size = len(maze[0])
    start = size + 1
    end = ((len(maze) - 1) * size - 1) - 1
    q = deque()

    # 存坐标，以及上一个关联路径
    q.append((start, -1))
    path = []
    while len(q) > 0:
        # 取队列坐标
        cur = q.pop()

        #将该坐标加入到路径
        path.append(cur)

        # 如果当前路径已经是终点，退出
        if cur[0] == end:
            print(len(path),path)
            new_path = []
            new_path.append(path[-1])
            while new_path[0][-1] != -1:
                ind = new_path[0][-1]
                new_path.insert(0,path[ind])
            for var in new_path:
                print([var[0] // size,var[0] % size])
            return True

        # urdl 存 上 右 下 左 的坐标
        urdl = [cur[0] - size, cur[0] + 1, cur[0] + size, cur[0] - 1]

        # 循环上 右 下 左 的坐标，将坐标都放进队列
        for load in urdl:
            val = maze[load // size][load % size]
            if val == 0:

                # 存坐标，以及上一个关联路径
                q.append((load,len(path)-1))

                # 走过的路标为2
                maze[load // size][load % size] = 2

    # 如果队列为空，则没有路径
    else:
        return False

mase_queue(maze)



