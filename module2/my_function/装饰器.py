# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/25


import time

def get_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        use_time = end_time - start_time
        return use_time,res
    return wrapper

@get_time
def calc(a,b):
    return a**b

print(calc(2,9000))