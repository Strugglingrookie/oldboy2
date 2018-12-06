#_*_coding:utf-8_*_

s = "路飞"

s2 = s.decode('utf-8') #unicode 
s3 = s2.encode("GBK") 

print(s3,s)  

