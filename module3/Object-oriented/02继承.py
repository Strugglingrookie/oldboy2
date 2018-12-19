# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 继承 人类 -> 男人类/女人类
'''
子类拥有父类以及祖类(父类的父类，没上线，可以一直往上找)的一切属性(数据/方法属性)，属性查找顺序，从子类本身一直往上找
派生 就是在父类的基础上，子类有自己的数据或方法属性，这就是派生
class a:
    def f1(self):
        print("from a f111")

    def f2(self):
        print("from a f222")
        self.f1()

class b(a):
    def f1(self):
        print("from b f111")


print(b.__bases__)  #父类列表
c = b()
c.f1()  #from b f111
c.f2()  #from a f222  from b f111  调用f1的本质是 c.f1(),按照属性查找规则，先在子类本身找
'''


# 继承原理，每个类在生成的时候解释器都会为其解析一个顺序(MRO)列表(经典类没有mro)，这个列表就是对象在找属性的时候的一个顺序，从左至右
'''
经典类：python2中没有继承object的类以及它的子类
新式类：python2中继承了object的类以及它的子类
python3里只有新式类，如果在创建类的时候没有继承类，默认继承object，所以全是新式类
经典类 查找属性顺序为 深度优先
新式类 查找属性顺序为 广度优先
class A:
    def test(self):
        print('from A')
    pass

class B(A):
    # def test(self):
    #     print('from B')
    pass

class C(A):
    # def test(self):
    #     print('from C')
    pass

class D(B):
    # def test(self):
    #     print('from D')
    pass

class E(C):
    # def test(self):
    #     print('from E')
    pass

class F(D,E):
    # def test(self):
    #     print('from F')
    pass


# print(F.mro())  # python3里广度优先  列表顺序 F,D,B,E,C,A,object   如果是python2里 就是 F,D,B,A,E,C,A
f = F()
f.test()  # 查找顺序  F,D,B,E,C,A,
'''

# 重用父类方法
# 1.指名道姓，不依赖继承
'''
class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity


class Garen(Hero):
    camp='Demacia'

    def attack(self,enemy):
        Hero.attack(self,enemy) #指名道姓，不依赖继承
        print('from Garen Class')

class Riven(Hero):
    camp='Noxus'


g=Garen('草丛伦',100,30)
r=Riven('锐雯雯',80,50)

print(r.life_value)
g.attack(r)
print(r.life_value)

class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity


class Garen(Hero):
    camp='Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):
        # self.nickname=nickname
        # self.life_value=life_value
        # self.aggresivity=aggresivity
        Hero.__init__(self,nickname,life_value,aggresivity)

        self.weapon=weapon

    def attack(self,enemy):
        Hero.attack(self,enemy) #指名道姓
        print('from Garen Class')


g=Garen('草丛伦',100,30,'金箍棒')

print(g.__dict__)
'''

# 2.super() 依赖继承
class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity


class Garen(Hero):
    camp='Demacia'

    def attack(self,enemy):
        super(Garen,self).attack(enemy)  #依赖继承
        super().attack(enemy)  #python3的写法，可以直接写成super
        print('from Garen Class')

class Riven(Hero):
    camp='Noxus'


g=Garen('草丛伦',100,30)
r=Riven('锐雯雯',80,50)

g.attack(r)
print(r.life_value)


# 重用__init__构造函数
class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity


class Garen(Hero):
    camp='Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):
        # self.nickname=nickname
        # self.life_value=life_value
        # self.aggresivity=aggresivity

        # super(Garen,self).__init__(nickname,life_value,aggresivity)
        super().__init__(nickname,life_value,aggresivity)
        self.weapon=weapon

    def attack(self,enemy):
        Hero.attack(self,enemy) #指名道姓
        print('from Garen Class')


g=Garen('草丛伦',100,30,'金箍棒')
print(g.__dict__)

# super的实质是按照当前被调用的类的mro列表一直往后面找
class A:
    def f1(self):
        print('from A')
        super().f1()  #执行到这里的时候并不是去A的父类里找f1，而是沿着C的mro列表继续往后面找f1


class B:
    def f1(self):
        print('from B')

class C(A,B):
    pass


print(C.mro()) #[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
tmp = C()
tmp.f1()
# from A
# from B


