#_*_coding:utf-8_*_

#usage:
#>>> memoryview(b'abcd')
#<memory at 0x104069648>
#在进行切片并赋值数据时，不需要重新copy原列表数据，可以直接映射原数据内存，

import time
for n in (100000, 200000, 300000, 400000):
#for n in (100,200,300):
    data = b'x'*n

    start = time.time()
    b = data
    #print(data)
    while b:
        b = b[1:]
        #print(b)
    print('bytes', n, time.time()-start)


for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)