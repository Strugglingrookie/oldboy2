#_*_coding:utf-8_*_




# names = ['alex','jack',2,'rain','mack',2,'racheal','shanshan',2,'longting']




# question 10
# count = 0
# for i in names:
#     print(count,i)
#     count += 1

# #
# for index,i in enumerate(names): #枚举
#     print(index,i)


#question 11
#
# for index,i in enumerate(names): #枚举
#
#     if index%2 == 0:#偶数
#         names[index] = -1
#         print(index, i)
#
# print(names)

#
# #question 12
# names = ['alex','jack','peiqi',2,'rain','mack',2,'racheal','shanshan',2,'longting']
#
# fisrt_index = names.index(2)
#
#
# new_list = names[fisrt_index+1:]
# second_index = new_list.index(2)
# second_val = names[fisrt_index+second_index+1]
# print(new_list,fisrt_index,second_index)
#
# print('second values:', second_val)


#question 13
# products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
#
#
# print("--------商品列表---------")
# for index,p in enumerate(products):
#     print("%s. %s   %s" %(index,p[0],p[1]  ) )


#question 14
products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

shopping_cart = []

#run_flag = True #标志位
exit_flag = False
while not exit_flag:
    print("--------商品列表---------")
    for index,p in enumerate(products):
        print("%s. %s   %s" %(index,p[0],p[1]  ) )

    choice = input("输入想买的商品编号:")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(products):
            shopping_cart.append(products[choice])
            print("Added product %s into shopping cart." %(products[choice]))
        else:
            print("商品不存在")
    elif choice == 'q':
        if len(shopping_cart) >0:
            print("-------你已购买以下商品-------")
            for index,p in enumerate(shopping_cart):
                print("%s. %s   %s" % (index, p[0], p[1]))

        #break
        #run_flag = False
        exit_flag = True