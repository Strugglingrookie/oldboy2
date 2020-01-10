'''
双向队列的两端都支持进队和出队操作
双向队列的基本操作：
队首进队
队首出队
队尾进队
队尾出队
'''

from collections import deque

#起始队列为空，最大长度为3，队满时进队，溢出
q1 = deque([],3)
q1.append(6) # 队尾进队
q1.append(7) # 队尾进队
q1.append(8) # 队尾进队
print('q1队首出队', q1.popleft()) # 队首出队 6

#起始队列为[1,2,3,4,5]，最大长度为5
q2 = deque([1,2,3,4], 5)
q2.appendleft(5) # 队首进队
print('队尾出队', q2.pop()) # 队尾出队 4

#队满时，自动pop另一端,不会报错
for ch in 'abcde':
    q2.append(ch) # 队尾进队
print('队满溢出，队首出队', end='：')
for i in range(5):
    print(q2.popleft(),end=' ') # 队首出队
#队满溢出，队首出队：a b c d e

# 双向队列应用 tail 命令
def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end='')