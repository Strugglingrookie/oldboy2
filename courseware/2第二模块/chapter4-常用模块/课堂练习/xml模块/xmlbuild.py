# _*_coding:utf-8_*_
# created by Alex Li on 10/17/17

import xml.etree.ElementTree as ET


root = ET.Element("namelist") #root

name = ET.SubElement(root,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
n = ET.SubElement(name,"name")
n.text = "Alex Li"
sex.text = 'male'


name2 = ET.SubElement(root,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(root ) #生成文档对象

et.write("build_out.xml", encoding="utf-8",xml_declaration=True)
