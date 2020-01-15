# 二叉树的链式存储：
# 将二叉树的节点定义为一个对象，节点之间通过类似链表的链接方式来连接。
#
# 节点定义：
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

# 二叉树的遍历方式：
# 前序遍历：EACBDGF
def pre_order(root):
    if root:
        print(root.data,end=' -> ')
        pre_order(root.lchild)
        pre_order(root.rchild)
pre_order(root)
print()
# E -> A -> C -> B -> D -> G -> F ->

# 中序遍历：ABCDEGF
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end=' -> ')
        in_order(root.rchild)
in_order(root)
print()
# A -> B -> C -> D -> E -> G -> F ->

# 后序遍历：BDCAFGE
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=' -> ')
post_order(root)
print()
# B -> D -> C -> A -> F -> G -> E ->

# 层次遍历：EAGCFBD
from collections import deque

def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.data, end=' -> ')
        if node.lchild:
            q.append(node.lchild)
        if node.rchild:
            q.append(node.rchild)
level_order(root)
print()
# E -> A -> G -> C -> F -> B -> D ->
