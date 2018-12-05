# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 9:49
# @Author  : Xiao


lis = [{"k1":"v1","k2":"v2"},{"k3":"v3","k4":"v4"}]

def store(file_name,lis):
    lis_new = []
    for i in lis:
        lis_new.append(str(i).replace(":","/").replace(",",";").replace("{","").replace("}","").replace("'","").replace(" ",""))
    lis_str = r'\n'.join(lis_new)
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(lis_str)

def load(file_name):
    lis = []
    with open(file_name, "r", encoding="utf-8") as f:
        tmp_lis = f.read().split(r"\n")
        for i in tmp_lis:
            for k in i.split(";"):
                tmp = k.split(r"/")
                tmp_dic = {}
                tmp_dic[tmp[0]] = tmp[1]
                lis.append(tmp_dic)
    return lis

store("b.txt",lis)
new_lis = load("b.txt")
print(type(new_lis),new_lis)