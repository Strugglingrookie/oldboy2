#_*_coding:utf-8_*_

import re

f = open("兼职白领学生空姐模特护士联系方式.txt",'r',encoding="gbk")

data = f.read()
phones = re.findall("[0-9]{11}", data)

print(phones)


# phones = []
#
# for line in f:
#     name,city,height,weight,phone = line.split()
#     if phone.startswith('1') and len(phone) == 11:
#         phones.append(phone)
#
# print(phones)

#print(data)
#
