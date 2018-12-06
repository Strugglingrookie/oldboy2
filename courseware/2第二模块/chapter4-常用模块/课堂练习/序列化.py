#_*_coding:utf-8_*_


#
# data = {
#
#     'roles':[
#         {'role':'monster','type':'pig','life':50},
#         {'role':'hero','type':'关羽','life':80},
#     ]
# }
#
#
# f = open("game_status","w")
#
# f.write(str(data))


f = open("game_status","r")

d = f.read()

d = eval(d)

print(d['roles'])