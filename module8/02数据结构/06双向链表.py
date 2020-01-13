# 双链表的每个节点有两个指针：一个指向后一个节点，另一个指向前一个节点。

# 节点
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None

# 链表遍历
def print_linklist(lk, reverse=False):
    '''
    :param lk: 链表
    :param reverse:
    默认正向输出，从头到尾
    如果值为True，反向输出，从尾到头
    '''
    while lk:
        print(lk.item, end=' -> ')
        lk = lk.prior if reverse else lk.next
    print()

#创建链表，头插法
def create_linklist_head(li):
    head = Node(li[0])
    tail = head
    for var in li[1:]:
        node = Node(var)
        node.next = head
        head.prior = node
        head = node
    return head,tail
head_lk,tail_lk = create_linklist_head([1,2,3,6,8])
print_linklist(head_lk)
# 8 -> 6 -> 3 -> 2 -> 1 ->
print_linklist(tail_lk,True)
# 1 -> 2 -> 3 -> 6 -> 8 ->

# 创建链表，尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for var in li[1:]:
        node = Node(var)
        tail.next = node
        node.prior = tail
        tail = node
    return head,tail
head_lk,tail_lk = create_linklist_tail([1,2,3,6,8])
print_linklist(head_lk)
# 1 -> 2 -> 3 -> 6 -> 8 ->
print_linklist(tail_lk,True)
# 8 -> 6 -> 3 -> 2 -> 1 ->

# 链表的插入 第n个节点插入数据p
def insert_linklist(insert_lk, n, p):
    cur = insert_lk
    for i in range(n-1):
        cur = cur.next
    p.next = cur.next
    cur.next.prior = p
    cur.next = p
    p.prior = cur
    return insert_lk
head_lk,tail_lk = create_linklist_head([1,2,3,6,8])
node = Node(10086)
insert_linklist(head_lk, 2, node)
print_linklist(head_lk)
# 8 -> 6 -> 10086 -> 3 -> 2 -> 1 ->
print_linklist(tail_lk,True)
# 1 -> 2 -> 3 -> 10086 -> 6 -> 8 ->

# 链表的删除  删除第n个节点
def del_linklist(del_lk, n):
    cur = del_lk
    for i in range(n-1):
        cur = cur.next
    p = cur.next
    p.next.prior = cur
    cur.next = p.next
    del p
    return del_lk
head_lk,tail_lk = create_linklist_head([1,2,3,6,8,9])
del_lk = del_linklist(head_lk,2)
print_linklist(del_lk)
# 9 -> 8 -> 3 -> 2 -> 1 ->
print_linklist(tail_lk,True)
# 1 -> 2 -> 3 -> 8 -> 9 ->