#_*_coding:utf-8_*_


products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]


index = 0
print('---------商品列表----------')
for p in products:
    print("%s. %s    %s" %(index,p[0],p[1]))
    index += 1