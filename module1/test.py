# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 9:49
# @Author  : Xiao

#格式化输出，就是设计好套路，在输出的时候按这个套路来输出,主要有四种
name='进击的菜鸟'
money=100
#用+号连接
print("Welcome to 'From zero single row':"+name)
#用,号连接
print("Welcome to 'From zero single row':",name)
#用百分号占位符,%s只是先占了一个位置在这里，然后再输出的时候把后面的值依次填充到占位的位置
print("Welcome to 'From zero single row':[%s]! Let's study!"%name)
#多个占位时，这样用，需要括弧括起来，必须是按照占位的顺序才可以
print("Welcome to 'From zero single row':[%s]! Your have money:[%s]元"%(name,money))
#拓展，%s占位的是字符类型的位置，%d占位的是整数类型的位置，%.2f占位的是小数类型(会四舍五入)的位置
print("Welcome to 'From zero single row':[%s]! Your have money:[%d]元!Your height is[%.2f]cm"%(name,money,180.235))
#用format格式，这个格式，就不用担心顺序问题，但参数夺得时候用这个
print("Welcome to 'From zero single row':[{name}]! 'Your have money:[{money}]元'".format(money=money,name=name))
#format传list或字典需要加*号，如字典：
dic={"name":"Xiao","age":18}
print("My name is {name},I'm {age} years old.".format(**dic))
#练习，输入名字和年龄，然后格式化打印：你的名字是：xxx，你的年龄是：xx。