#_*_coding:utf-8_*_

import os

f_name = "兼职白领学生空姐模特护士联系方式.txt"
f_new_name = "%s.new" %f_name

old_str = "乔亦菲"
new_str = "肛娘"

f = open(f_name,"r",encoding="utf-8")
f_new = open(f_new_name,"w",encoding="utf-8")

for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)

    f_new.write(line)

f.close()
f_new.close()

os.rename(f_new_name,f_name)