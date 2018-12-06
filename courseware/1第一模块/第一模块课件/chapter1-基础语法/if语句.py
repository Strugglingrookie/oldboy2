#_*_coding:utf-8_*_

# age_of_you = 25
#
# if age_of_you > 22:
#     print("time to find a bf.")
# else:
#     print("还可以再谈几次恋爱....")
#
# print("-------hahah")


# _username = "shanshan"
# _password = "abc123"
#
# username = input("username:")
# password = input("password:")
#
# if username == _username and password ==  _password:
#     print("welcome ", _username)
# else:
#     print("wrong username or password!")


name = input("name:")
sex = input("sex:")
age = int(input("Age:"))

# if sex == 'f':
# # 1如果 是女生
#     1.1 如果年龄 小于28
#         1.1.1 打印喜欢女生
#     1.2 打印 姐弟恋很好
#   2. 如果是男生 ，打印 搞基

if sex == "f":
    if age < 28:
        print("I love girls")
        print("I love girls")
    else:
        print("姐弟恋也很好")
else:
    print("一起来搞基")



#同一级别的代码 缩进 必须 保持一致
#官方建议4个空格
#顶级代码必须 顶行写
print("----here ....")