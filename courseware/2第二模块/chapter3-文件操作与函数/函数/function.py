


# def sayhi():
#
#     print("hello")
#     print("my name is black girl...")
#
# print(sayhi)
# sayhi()



# def sayhi(name):
#
#     print("hello",name)
# #     print("my name is black girl...。。")
# #
# #
# # sayhi("Alex")
#
# def calc(x,y):
#
#     res = x**y
#     print(res)
#
# calc(5,10)
# calc(2,10)


#
# def stu_register(name,age,course,country='CN'):
#     print("registriation info....")
#     print(name,age,country,course)


#stu_register("Alex",23,course='Python',age=22)
# stu_register("Jack",22,'Python','CN')
# stu_register("Rain",22,'Python','Korean')


# def send_alert(msg,*args):
#
#     print('sending msg ....',msg,args)
#
#     if args:
#         print(args[0])
#
# send_alert('cpu alert...')
# send_alert('cpu alert...','email')
# send_alert('cpu alert...','weixin',1)
#send_alert('cpu alert...','weixin',multiple=1)




def send_alert(msg,*users,age): # (['alex','xxx','iiii'],) --> ('alex','xxx','iiii')
    for u in users:
        print('报警发送给',u)


# 如果参数中出现 ＊users,传递的参数就可以不再是固定个数，传过来的所有参数打包元祖
# 方式一：
# send_alert('别他么狼了','alex','xxx','xxx','ooo')
# send_alert('别他么狼了','alex')
# send_alert('别他么狼了','alex','xxx')
# send_alert('别他么狼了','alex','xxx','iiii')
# 方式二：
# send_alert('别他么狼了',*['alex','xxx','iiii'])

# send_alert("alex","rain",'eric',age=22)
