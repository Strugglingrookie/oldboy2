# _*_coding:utf-8_*_
# created by Alex Li on 10/17/17



import xml.etree.ElementTree as ET

tree = ET.parse("xml test") #open
root = tree.getroot() #f.seek(0)
#print(dir(root))
print(root.tag)
#
#遍历xml文档
for child in root:
    print('----------',child.tag, child.attrib)
    for i in child:
        print(i.tag,i.text)

# #只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag,node.text)
