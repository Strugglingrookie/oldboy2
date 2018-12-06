#_*_coding:utf-8_*_


s = "路飞"
print s

s2 = s.decode("utf-8")
print(s2 )
print(type(s2)) #unicode

s3 = s2.encode("gbk")
print(  s3 ) #gbk
print(type(s3))
s4 = s2.encode("utf-8")


print(s4 ,s3,s2)

