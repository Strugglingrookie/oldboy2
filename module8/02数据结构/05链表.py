# 链表是由一系列节点组成的元素集合。
# 每个节点包含两部分，数据域item和指向下一个节点的指针next。
# 通过节点之间的相互连接，最终串联成一个链表。

# 单向链表
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

# 链表遍历
def print_linklist(lk):
    while lk:
        print(lk.item, end=' -> ')
        lk = lk.next
    print()

#创建链表，头插法
def create_linklist_head(li):
    head = Node(li[0])
    for var in li[1:]:
        node = Node(var)
        node.next = head
        head = node
    return head
head_lk = create_linklist_head([1,2,3,6,8])
print_linklist(head_lk)
# 8,6,3,2,1,

# 创建链表，尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for var in li[1:]:
        node = Node(var)
        tail.next = node
        tail = node
    return head
tail_lk = create_linklist_tail([1,2,3,6,8])
print_linklist(tail_lk)
# 1,2,3,6,8,

# 链表的插入 第n个节点插入数据p
def insert_linklist(insert_lk, n, p):
    cur = insert_lk
    for i in range(n-1):
        cur = cur.next
    p.next = cur.next
    cur.next = p
    return insert_lk
insert_lk = create_linklist_tail([1,2,3,6,8])
node = Node(10086)
insert_linklist(insert_lk, 2, node)
print_linklist(insert_lk)
# 1,2,10086,3,6,8,

# 链表的删除  删除第n个节点
def del_linklist(del_lk, n):
    cur = del_lk
    for i in range(n-1):
        cur = cur.next
    p = cur.next
    cur.next = cur.next.next
    del p
    return del_lk
del_lk = create_linklist_tail([1,2,3,6,8])
del_lk = del_linklist(del_lk,2)
print_linklist(del_lk)
# 1,2,6,8,