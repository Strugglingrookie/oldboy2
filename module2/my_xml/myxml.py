# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/29


import xml.etree.ElementTree as ET

tree = ET.parse("test.xml") #类似文件的打开open
root = tree.getroot() #f.seek(0)
print(dir(root))  #查看根的方法 append,clear,extend,find,findall,findtext,get,getchildren,getiterator,insert,items,iter,iterfind,itertext,keys,makeelement,remove,set
print(root.tag)  #拿到根标签

# 遍历xml文档
for child in root:
    print("--------",child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib,i.text)

# 只遍历year节点
for node in root.iter("year"):
    print(node.tag,node.attrib,node.text)

#增删改查
#把每年+1
for node in root.iter("year"):
    new_year = int(node.text)+1
    node.text = str(new_year)
    node.set("attr_test2","yes")
tree.write("test.xml")

#删除node
for country in tree.findall("country"):
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)
tree.write("out_put.xml")

#创建xml文档
root = ET.Element("namelist")
name = ET.SubElement(root,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text="female"

name2 = ET.SubElement(root,"name",attrib={"enrolled":"no"})
age2 = ET.SubElement(name2,"age",attrib={"checked":"no"})
age2.text = "18"

et = ET.ElementTree(root)  #生成文档对象
et.write("test2.xml",encoding = "utf-8",xml_declaration=True)  #xml_declaration=True xml版本说明

ET.dump(root)


