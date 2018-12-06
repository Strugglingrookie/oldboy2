#_*_coding:utf-8_*_


import shelve

f = shelve.open('shelve_test') # 打开一个文件



names = ["alex", "rain", "test"]
info = {'name':'alex','age':22}


f["names"] = names # 持久化列表
f['info_dic'] = info



f.close()