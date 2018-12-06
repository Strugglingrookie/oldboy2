#_*_coding:utf-8_*_

import shelve

d = shelve.open('shelve_test')  # 打开一个文件

print(d['names'])
print(d['info_dic'])


#del d['test'] #还可以删除