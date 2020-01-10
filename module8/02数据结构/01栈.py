"""
栈(Stack)是一个数据集合，可以理解为只能在一端进行插入或删除操作的列表。
栈的特点：后进先出 LIFO（last-in, first-out）
栈的概念：栈顶、栈底
栈的基本操作：
进栈（压栈）：push
出栈：pop
取栈顶：gettop
"""
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

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())  # False
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.is_empty()) # True

# 括号匹配问题：给一个字符串，其中包含小括号、中括号、大括号，求该字符串中的括号是否匹配。
# 例如：
# ()()[]{}		匹配
# ([{()}])		匹配
# [](			不匹配
# [(])			不匹配
dic = {"}":"{","]":"[",")":"(",}
def equal_symbol(str):
    stack = Stack()
    for sy in str:
        print(sy,stack.stack)
        if sy in ('(','[','{'):
            stack.push(sy)
            continue
        if not stack.is_empty() and dic.get(sy) == stack.pop():
            continue
        return False
    if stack.is_empty():
        return True
    return False

str1 = '()()[]'
str2 = '()()[]{'
print(equal_symbol(str1)) # True
print(equal_symbol(str2)) # False