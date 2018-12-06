


f = open("兼职白领学生空姐模特护士联系方式.txt",'r+',encoding="gbk")
data = f.read()
print("content",data)

f.write("\nnewline 1哈哈")
f.write("\nnewline 2哈哈")
f.write("\nnewline 3哈哈")
f.write("\nnewline 4哈哈")

print("new content",f.read())

f.close()