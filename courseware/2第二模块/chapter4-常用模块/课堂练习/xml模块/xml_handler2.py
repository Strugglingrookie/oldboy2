# _*_coding:utf-8_*_
# created by Alex Li on 10/17/17


import xml.etree.ElementTree as ET

tree = ET.parse("xml test")
root = tree.getroot() #f.seek(0)


# #修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("attr_test","yes")



#删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')


#tree.write("xml test")