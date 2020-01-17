# 二叉搜索树是一颗二叉树且满足性质：
# 设x是二叉树的一个节点
# 如果y是x左子树的一个节点，那么y.key ≤ x.key；
# 如果y是x右子树的一个节点，那么y.key ≥ x.key。

from collections import deque

class BiTreeNode(): # 树节点
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None  # 父节点

class BST():  # 创建二叉搜索树对象
    def __init__(self, li=None):
        self.root = None
        if li:
            for var in li:
                self.insert(var)

    # 插入值
    def insert(self, var):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(var)
            return
        while True:
            if var < p.data: # 往左
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(var)
                    p.lchild.parent = p
                    return
            if var > p.data: # 往右
                if p.rchild:
                    p = p.rchild
                else:  # 右孩子不存在
                    p.rchild = BiTreeNode(var)
                    p.rchild.parent = p
                    return
        else:  # 正常结束说明该值已存在
            return

    # 搜索值
    def query(self, var):
        p = self.root
        while p:
            if var == p.data:
                return p
            elif var > p.data:
                p = p.rchild
            else:
                p = p.lchild
        else:
            return None

    # 前序遍历：EACBDGF
    def pre_order(self, root):
        if root:
            print(root.data, end=' -> ')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历：ABCDEGF
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=' -> ')
            self.in_order(root.rchild)

    # 后序遍历：BDCAFGE
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=' -> ')

    # 层次遍历：EAGCFBD
    def level_order(self, root):
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            print(node.data, end=' -> ')
            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)

    # 删除情况1：node是叶子节点
    def __remove_node1(self, node):
        # 如果node是根节点
        if not node.parent:
            self.root.data = None

        # 如果node是左孩子
        if node == node.parent.lchild:
            node.parent.lchild = None

        # 如果node是右孩子
        else:
            node.parent.rchild = None

    # 删除情况2.1：node只有一个左孩子
    def __remove_node21(self, node):
        # 如果node是根节点
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None

        # 如果node是左孩子
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent

        # 如果node是右孩子
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # 删除情况2.2：node只有一个右孩子
    def __remove_node22(self, node):
        # 如果node是根节点
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None

        # 如果node是左孩子
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent

        # 如果node是右孩子
        if node == node.parent.rchild:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    # 删除
    def delete(self, var):
        if self.root: # 不是空树
            node = self.query(var)

            # 如果不存在
            if not node:
                return False

            # 1.如果是叶子节点，直接删除
            if not node.lchild and not node.rchild:
                self.__remove_node1(node)

            # 2.1只有一个左孩子
            elif not node.rchild:
                self.__remove_node21(node)

            # 2.2只有一个右孩子
            elif not node.lchild:
                self.__remove_node22(node)

            # 3.俩孩子都有，从右子树中找到最小的min_node
            # min_node 替换 node，删除原 min_node
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                #删除min_node
                if min_node.rchild:
                    self.__remove_node22(min_node)
                else:
                    self.__remove_node1(min_node)

mytree = BST([6,3,1,8,9,4,7,5])
mytree.pre_order(mytree.root)
print()
# 6 -> 3 -> 1 -> 4 -> 5 -> 8 -> 7 -> 9 ->

mytree.in_order(mytree.root)
print()
# 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 ->

mytree.post_order(mytree.root)
print()
# 1 -> 5 -> 4 -> 3 -> 7 -> 9 -> 8 -> 6 ->

print(mytree.query(9))
# <__main__.BiTreeNode object at 0x0000000003F17400>

print(mytree.query(2))
# None

mytree.insert(2)
mytree.in_order(mytree.root)
print()
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 ->

mytree.delete(6)
mytree.in_order(mytree.root)
print()
# 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 ->