#_*_coding:utf-8_*_
import os

f_name = "兼职白领学生空姐模特护士联系方式utf8.txt"
f_new_name = "%s.new" % f_name

old_str = "乔亦菲"
new_str = "[乔亦菲 Yifei Qiao]"

f = open(f_name,'r',encoding="utf-8")
f_new = open(f_new_name,'w',encoding="utf-8")

for line in f:

    if old_str in line:
        new_line = line.replace(old_str,new_str)
    else:
        new_line = line

    f_new.write(new_line)

f.close()
f_new.close()

os.rename(f_new_name,f_name) #把新文件名字改成原文件 的名字，就把之前的覆盖掉了

