#_*_coding:utf-8_*_

iphone7 = ['alex', 'rain', 'jack', 'old_driver']
iphone8 = ['alex', 'shanshan', 'jack', 'old_boy']

both_list = []

for name in iphone8:
    if name in iphone7:
        both_list.append(name)

print(both_list)


s = {1,3,4,5,6}
s.discard()