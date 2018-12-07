# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/6


# 练习1：编写一个学生类，产生一堆学生对象， (5分钟)
# 要求：
# 有一个计数器（属性），统计总共实例了多少个对象
class student:
    school = "haerbin"
    count = 0
    def __init__(self,name):
        self.name = name
        student.count  += 1

stu1 = student("stu1")
stu2 = student("stu2")
print(stu1.count)
stu3 = student("stu3")
print(student.count)

# 练习2：模仿王者荣耀定义两个英雄类， (10分钟)
# 要求：
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。

class hero:

    def __init__(self,name,attack_value,life_value):
        self.name = name
        self.attack_value = attack_value
        self.life_value = life_value

    def attack(self,other):
        if self.life_value < 0:
            print("您已经死亡，不可再发起攻击！")
        elif other.life_value < 0:
            print("%s 已经死亡，不可再发起攻击！"%other.name)
        else:
            other.life_value -= self.attack_value
            print("您攻击了 %s，损失生命值 %s"%(other.name,self.attack_value))

a = hero("a",10,30)
b = hero("b",10,30)
a.attack(b)
a.attack(b)
a.attack(b)
a.attack(b)
a.attack(b)
b.attack(a)