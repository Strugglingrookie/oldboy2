# 时间维度：是指执行当前算法所消耗的时间，我们通常用「时间复杂度」来描述
# 常数阶O(1)  无论代码执行了多少行，只要是没有循环等复杂结构，那这个代码的时间复杂度就都是O(1)
def fun1(x):
    print(x)

# 对数阶O(logN) 全称是 O(log2N) 每次循环后次数减半
def fun2(x):
    while x>1:
        print(x)
        x = x//2

# 线性阶O(n)  for循环里面的代码会执行n遍，因此它消耗的时间是随着n的变化而变化的，因此这类代码都可以用O(n)来表示它的时间复杂度
def fun3(lis):
    for i in lis:
        print(i)

# 线性对数阶O(nlogN) 即 O(logn) 与  O(n)的组合
def fun4(x, lis):
    while x>1:
        for i in lis:
            print(i)
        x = x // 2

# 平方阶O(n²)
def fun5(lis):
    for i in lis:
        for j in (lis):
            print(j)

# 平方对数阶 O(n²2logn) 即 O(logn) 与  O(n²)的组合
def fun6(x, lis):
    while x>1:
        for i in lis:
            for j in (lis):
                print(j)
        x = x // 2

# 立方阶O(n³)
def fun7(lis):
    for i in lis:
        for j in (lis):
            for k in (lis):
                print(k)


# 注意算法的时间复杂度只跟类型有关，跟数量无关，如下代码的复杂度是 O(1) 并不是 O(3)
def fun8():
    print('hello world1')
    print('hello world2')
    print('hello world3')

# 如下代码的复杂度是 O(1) 并不是 n 并不是 O(n^2) 并不是 O(n^2+n)
def fun9(n):
    for i in range(n):
        print('Hello World')
        for j in range(n):
            print('Hello World')

# 时间复杂度总结：
'''
时间复杂度是用来估计算法运行时间的一个式子（单位）。一般来说，时间复杂度高的算法比复杂度低的算法快。
常见的时间复杂度（按效率排序） O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^2logn)<O(n^3)
如何一眼判断时间复杂度？
1.循环减半的过程O(logn)
2.几次循环就是n的几次方的复杂度
'''


# 空间维度：是指执行当前算法需要占用多少内存空间，我们通常用「空间复杂度」来描述
'''
算法的存储量包括:
1．程序本身所占空间
2．输入数据所占空间；
3．辅助变量所占空间
输入数据所占空间只取决于问题本身，和算法无关，则只需要分析除输入和程序之外的辅助变量所占额外空间。
空间复杂度是对一个算法在运行过程中临时占用的存储空间大小的量度，一般也作为问题规模n的函数，以数量级形式给出，记作：S(n) = O(g(n))
'''
# O(1)  如果算法执行所需要的临时空间不随着某个变量n的大小而变化，即此算法空间复杂度为一个常量，可表示为 O(1)
def fun10(x):
    print(x)

# 数据列表占用的大小为n，虽然有循环，但没有再分配新的空间
def fun11(lis):
    for i in lis:
        print(i)