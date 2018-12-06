#_*_coding:utf-8_*_

import json

# f = open("json_file",'w',encoding="utf-8")
#
#
# d = {'name':'alex','age':22}
#
# l = [1,2,3,4,'rain']
#
# json.dump(d,f)
# json.dump(l,f)


f = open("json_file",'r',encoding="utf-8")


print(json.load(f))
print(json.load(f))

