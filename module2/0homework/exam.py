# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/4


import chardet,os


content = "给岁月以文明，而不是给文明以岁月\n"
content2 = "给时光以生命，而不是给生命以时光\n"
count = 1

f1 = open("02第二模块之三体语录.","r",encoding="utf-8")
f2 = open("02第二模块之三体语录.new","w",encoding="utf-8")
lis = f1.readlines()
lis.insert(4,content)
lis.append(content2)
f2.writelines(lis)
f1.close()
f2.close()
os.rename("02第二模块之三体语录.new","02第二模块之三体语录.")


import time
def get_run_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(run_time)
        return res
    return wrapper

def func(n):
    if n == 1 :
        return 1
    return n * func(n-1)



