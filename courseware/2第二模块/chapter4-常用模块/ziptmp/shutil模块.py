#_*_coding:utf-8_*_

import shutil




#
# f1 = open("sheve_test.py", "r")
# f2 = open("sheve_test_new.py",'w')
#
# shutil.copyfileobj(f1,f2,length=10)

# shutil.copytree("packages","pack3",ignore=shutil.ignore_patterns("__init__.py","views.py"))


# shutil.move("pack3","p3")

# shutil.make_archive("/tmp/p3","zip",'p3',owner='root')
#
# import zipfile
#
# # z = zipfile.ZipFile("test.zip","w")
# # z.write("mysql.log")
# # z.write("re模块.py")
# # z.write("p3")
# #
# # z.close()
#
# z = zipfile.ZipFile('../test.zip', 'r')
# z.extractall()
# z.close()


import tarfile

t = tarfile.open("test2.tar","w")

t.add("/Users/alex/Documents/work/PyProjects/luffy_课件/21天入门/chapter4-常用模块/pack2",arcname="pack5")
t.add("mysql.log")

t.close()