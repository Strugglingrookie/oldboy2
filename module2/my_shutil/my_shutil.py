# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 15:52
# @Author  : Xiao

import shutil,zipfile,tarfile

f1 = open("a.txt","r")
f2 = open("b.txt","w")
shutil.copyfileobj(f1,f2)  #拷贝文件对象
f2.flush()
shutil.copyfile("a.txt","x.txt")  #拷贝文件内容
shutil.copy("a.txt","c.txt")  #拷贝文件内容和权限
shutil.copy2("a.txt","c.txt")  #拷贝文件内容和状态信息
shutil.copytree("myproj","myproj_new") #拷贝整个目录及目录下的所有文件(递归拷贝)
shutil.copytree("myproj","myproj_new",ignore=shutil.ignore_patterns("*.txt")) #拷贝整个目录,除了忽略的文件
shutil.rmtree("myproj_new2") #删除整个目录及目录下的所有文件(递归删除)
shutil.move("myproj_new","myproj_new2") #剪切目录
shutil.make_archive("myproj","zip","myproj") #压缩shutil.make_archive("可以是路径+压缩文件名","zip;tar等","被压缩文件") 实质是调用了zipfile模块

#zipfile 压缩zip 压缩了文件大小
z = zipfile.ZipFile("test.zip","w")
z.write("a.txt")
z.write("moudle_practice.py")
z.write("myproj")  #只压缩了文件夹名，不会递归压缩
z.close()
#解压
z = zipfile.ZipFile(r"E:\Study\Automantic\old_boy\module2\home_work\test.zip","r")
z.extractall()
z.close()

# tarfile 打包 tar 文件大小不会变
t = tarfile.open("your1.tar","w")
t.add("a.txt")
t.add("moudle_practice.py")
t.add(r"E:\Study\Automantic\old_boy\module2\module\myproj\crm",arcname="crm1")  #如果没有指定arcname，那么打的包里会有E:\Study\Automantic\old_boy\module2\module\myproj\crm这么多鞥路径
t.close()
# 解压
t = tarfile.open("your.tar","r")
t.extractall(r"E:\Study\Automantic\old_boy\module2\module\myproj") #可指定解压地址
t.close()


