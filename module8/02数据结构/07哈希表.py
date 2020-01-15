'''
直接寻址表：key为k的元素放到k位置上

改进直接寻址表：哈希（Hashing）
构建大小为m的寻址表T
key为k的元素放到h(k)位置上
h(k)是一个函数，其将域U映射到表T[0,1,...,m-1]

哈希表（Hash Table，又称为散列表），是一种线性表的存储结构。哈希表由一个直接寻址表和一个哈希函数组成。
哈希函数h(k)将元素关键字k作为自变量，返回元素的存储下标。
假设有一个长度为7的哈希表，哈希函数h(k)=k%7。元素集合{14,22,3,5}的存储方式如下：
[14,22,None,3,None,5,None,None]

哈希冲突
由于哈希表的大小是有限的，而要存储的值的总数量是无限的。
因此对于任何哈希函数，都会出现两个不同元素映射到同一个位置上的情况，这种情况叫做哈希冲突。
比如h(k)=k%7, h(0)=h(7)=h(14)=...

解决哈希冲突：开放寻址法
如果哈希函数返回的位置已经有值，则可以向后探查新的位置来存储这个值。
线性探查：如果位置i被占用，则探查i+1, i+2,……
二次探查：如果位置i被占用，则探查i+12,i-12,i+22,i-22,……
二度哈希：有n个哈希函数，当使用第1个哈希函数h1发生冲突时，则尝试使用h2,h3,……

解决哈希冲突：拉链法
拉链法：哈希表每个位置都连接一个链表，当冲突发生时，冲突的元素将被加到该位置链表的最后。

哈希表：常见哈希函数
除法哈希法：
h(k) = k % m
乘法哈希法：
h(k) = floor(m*(A*key%1))
全域哈希法：
ha,b(k) = ((a*key + b) mod p) mod m   a,b=1,2,...,p-1

哈希表的应用：集合与字典
字典与集合都是通过哈希表来实现的。
a = {'name': 'Alex', 'age': 18, 'gender': 'Man'}
使用哈希表存储字典，通过哈希函数将字典的键映射为下标。
假设h('name') = 3, h('age') = 1, h('gender') = 4，
则哈希表存储为[None, 18, None, 'Alex', 'Man']
如果发生哈希冲突，则通过拉链法或开发寻址法解决

'''