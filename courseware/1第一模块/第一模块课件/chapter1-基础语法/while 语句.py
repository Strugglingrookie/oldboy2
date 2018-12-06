#_*_coding:utf-8_*_


#
# count = 0
#
# while count <= 100:
#     print("loop ", count)
#     count += 1
#
#
# print('----loop is ended----')



# 打印偶数
# count = 0
#
# while count <= 100:
#
#     if count % 2 == 0: #偶数
#         print("loop ", count)
#
#     count += 1
#
#
# print('----loop is ended----')


# 第50次不打印，第60-80打印对应值 的平方
count = 0

while count <= 100:

    if count == 50:
        pass #就是过。。

    elif count >= 60 and count <= 80:
        print(count*count)

    else:
        print('loop ', count)



    count += 1


print('----loop is ended----')