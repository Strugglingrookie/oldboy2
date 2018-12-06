# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/30


#本来字典够用，但很多如那件都会以config这种形式存储配置文件，所以python里内置了这个模块，本质和字典一样，嵌套字典
import configparser


conf = configparser.ConfigParser()  #实例化一个config文件解析的对象
conf.read("conf.ini")  #读取配置文件为一个字典对象
print(dir(conf))  #可以看到很多和字典类似
print(dir(conf["bitbucket.org"])) #可以看到很多和字典类似

#读
print(conf.sections())  #不会打印default
print(conf.default_section)
print(conf["bitbucket.org"]["User"]) #获取配置项的值
for k in conf["bitbucket.org"]: #打印包含default的所有key，default默认所有节点都有该项配置，所以在循环其中一个节点，会打印default
    print(k)
for k,v in conf["bitbucket.org"].items():  #打印包含default的所有key/value
    print(k,v)
print(conf.has_section("asd"))  #判断是否存在该节点
print(conf.has_section("bitbucket.org"))
print(conf.has_option("bitbucket.org","asdfg"))  #判断该节点是否存在该key
print(conf.has_option("bitbucket.org","User"))

#增删改  任何一个操作都要重新写文件才会生效
conf.read("test.ini")
print(conf.options("group1"))
print(conf["group1"]["k1"])

conf["group2"]["k1"] = "54321"
conf.set("group1","k1","123456")
conf.write(open("test1.ini","w"))  #写入文件才会生效

conf.remove_section("group2")  #删除节点，不指定group2的话，会删除所有section
conf.remove_option("group1","k1")  #删除节点下的项，必须指定项，不然报错
conf.write(open("test.ini","w"))  #可以直接以之前的文件命名，内容会覆盖

conf.add_section("group3")  #添加一个节点
conf["group3"]["name"] = "xg"  #节点下添加一个k,v
conf["group3"]["age"] = "22"
conf.write(open("test_new.ini","w"))  #将修改后的值写入新文件，这样才能生效







