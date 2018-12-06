#_*_coding:utf-8_*_

def calc(n):
    v = int(n/2)
    print(v)
    if v > 0:
        calc(v)
    else:
        print('-------')
    print(n)

calc(10)