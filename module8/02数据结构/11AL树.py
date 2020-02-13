'''
AVL树：AVL树是一棵自平衡的二叉搜索树。

1.性质
根的左右子树的高度之差的绝对值不能超过1
根的左右子树都是平衡二叉树


2.插入
插入一个节点可能会破坏AVL树的平衡，可以通过旋转操作来进行修正。
插入一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变。
我们需要找出第一个破坏了平衡条件的节点，称之为K。K的两颗子树的高度差2。
不平衡的出现可能有4种情况：
'''


###### 二叉搜索树  ######
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


###### AVL树  ######
class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

# 1.不平衡是由于对K的右孩子的右子树插入导致的：左旋
    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

# 2.不平衡是由于对K的左孩子的左子树插入导致的：右旋
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

# 3.不平衡是由于对K的右孩子的左子树插入导致的：右旋-左旋
    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        #更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else: # 插入的是g
            p.bf = 0
            c.bf = 0
        return g

# 4.不平衡是由于对K的左孩子的右子树插入导致的：左旋-右旋
    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        return g

    def insert_no_rec(self, val):
        # 1. 和BST一样，插入
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val == p.data
                return

        # 2. 更新balance factor
        while node.parent:  # node.parent不空
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉了
                # 更新node.parent的bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1, 更新后变成-2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得：把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0，更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递是从右子树来的，右子树更沉了
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1, 更新后变成2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0:  # node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:  # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来
                elif node.parent.bf < 0:  # 原来node.parent.bf = -1，更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0，更新之后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = g
            if g:  # g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break

tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])

tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)