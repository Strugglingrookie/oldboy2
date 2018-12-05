# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/29


import json,pickle
# my_json&pickle&shelve：把内存里的数据类型转成字符串，才能够存到硬盘，或者网络传输
data = {"a":123,"b":456}
lis = [1,2,3,4,5,6,7]

#json 跨语言/体积小  只支持 int/str/list/list/tuple/dict
# 1.可以存到内存 2.将字符串网络传输给别人(网络传输必须是bytes类型) 3.跨平台/语言共享数据,定义了不同语言之间的交互规则
# d = json.dumps(data)   #将python数据类型转换为字符串：
# print(d,type(d))
#
# d2 = json.loads(d)  #将字符串转换为python数据类型
# print(d2,type(d2))

# f = open("test.list","w")  #打开一个文件对象，写模式
# json.dump(lis,f)  #将python数据类型直接以字符串形式存到文件里

# f = open("test.list","r")  #打开一个文件对象，读模式
# d3 = json.load(f)  #直接将文件内容以python数据类型读取
# print(d3,type(d3))


#pickle 专为python，支持所有python数据类型(set/float/函数/类都行)   但是只能在python里用，且占体积小
# f = open("data.pkl","wb")  #必须二进制打开
# pickle.dump(data,f)  #存的也是bytes类型

# f = open("data.pkl","rb")  #必须是二进制打开
# d = pickle.load(f)

# d = pickle.dumps(data)
# print(d,type(d))

# d2 = pickle.loads(d)
# print(d2,type(d2))


#shelve  解决需要序列化多种类型的python数据，以 k,v 形式存储
import shelve
f = shelve.open("shelve_test")

# f["data"] = data
# f["lis"] = lis

print(f.get("data"))
print(list(f.keys()))  #获取所有key
print(list(f.values()))  #获取所有 value
print(list(f.items()))  #获取所有 k,v
f["key2"] = [1,2,"a"]  #创建一个新的kv
# print(list(f.pop("data")))  #删除一个kv
# del f["data"]  #删除一个kv
# f.clear()  #清空所有内容

f.close()






