# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/6


# 面向过程概述
'''
定义：指解决问题的步骤，第一步第二步一直走下去，知道解决问题。好比流水线，是一种机械式的思维。
优点：复杂问题流程化，进而简单化（一个复杂的问题，分成一个个小的步骤去实现，实现小的步骤将会非常简单）
缺点：一旦解决问题的步骤都确定好了后，不好扩展，好比如体制化后要改革非常难，改其中一个步骤，其他步骤都必须得联动，扩展性极差。
应用；实用于一些不会轻易变化的场景，比如需要写一些简单的脚本做些一次性任务，面向过程实用。但如果处理非常复杂且需求多变的任务时就不好使了。

面向对象：
定义：万物皆对象，对象就是特征于技能的集合（比如孙悟空，毛脸雷公嘴是特征，七十二变是技能）
优点：可扩展性强
缺点：编程复杂度高，极容易出现过度设计的问题，而且在一些扩展性要求低的场景使用面向对象会徒增编程难度
应用：实用于客户需求频繁变化，如互联网/游戏/企业应用

类：在程序里实质就是一个模板，定义好类的特征/技能，就可以生成具有这些特征/技能的对象，这个过程就是类的实例化
定义：类就是一系列对象相似的特征与技能的结合体
强调：站在不同的角度，得到的分类不一样
'''

# 定义类
'''
# 知识点 类在定义的时候会执行里面的代码，跟函数不一样，函数在定义的时候只是保存在内存里，加括弧的时候才会调用
class BeijingStudent:
    school = "beijing_university"  #类的数据属性
    print(school)
    def learn(self):     #类的函数属性
        print("learning")

    def sleep(self):
        print("sleeping")

# 产生对象  即实例化
stu1 = BeijingStudent()  #BeijingStudent()跟函数调用是一样的，但这里不是执行类体里面的代码，只是得到一个对象
stu2 = BeijingStudent()
stu3 = BeijingStudent()

print(stu1)  #  <__main__.BeijingStudent object at 0x10bc56080>  生成的是一个对象
print(stu2)  #  <__main__.BeijingStudent object at 0x10db5f048>  都是同一个类生成的对象，内存地址不一样

# 查看类的名称空间  类内部：变量就是上面说的特征  函数就是上面说的技能
print(BeijingStudent.__dict__)  # 类的名称空间是一个字典形式 「'school': 'beijing_university', 'learn': <function BeijingStudent.learn at 0x109c152f0>」
# 查属性
print(BeijingStudent.__dict__['school'])  # 既然名称空间是一个字典，那么就可以用字典的方式拿到数据
print(BeijingStudent.__dict__['learn'])  # 既然名称空间是一个字典，那么就可以用字典的方式拿到数据，函数也一样，只要是属性就可以这样访问
#只是python提供了特别的访问方式，直接点就可以访问类里的属性
print(BeijingStudent.school)  # 实质就是上面那种访问方式，只是python简化了，跟模块一样，直接time.time()，本质都是一样的
print(BeijingStudent.learn)
# 增
BeijingStudent.country = "China"
print(BeijingStudent.__dict__['country'])
print(BeijingStudent.country)
# 删
del BeijingStudent.country
# 改
BeijingStudent.school = "Qinghua_university"

'''

# 使用对象
'''
# __init__ 为对象定制对象自己的特征  __init__ 构造函数
class BeijingStudent:
    school = "beijing_university"
                #stu1，name,sex,age  实例化的时候类会自动调用__init__函数，将对象本身和传递的参数一起放进来
    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

        # stu1.Name = name  # 实际就是做了这步操作
        # stu1.Sex = sex
        # stu1.Age = age

    def learn(self):
        print("learning")

    def sleep(self):
        print("sleeping")

# 产生对象  即实例化
stu1 = BeijingStudent("王大锤","男",18)
print(stu1.__dict__)  # >> {'Name': '王大锤', 'Sex': '男', 'Age': 18}
# 查
print(stu1.Name)
# 改
stu1.Name = "隔壁老王"
print(stu1.Name)
# 删
del stu1.Name
print(stu1.__dict__)
# 增
stu1.weight = "70KG"
print(stu1.__dict__)
print(stu1.weight)
'''

# 属性/方法查找
# 类中的方法，是给对象使用的，哪个对象调用就把那个对象本身作为第一个参数传递给方法，也就是给self
'''
x = "global_x"

class BeijingStudent:
    school = "beijing_university"

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print("learning")

    def sleep(self):
        print("%s is sleeping"%self.Name)

stu1 = BeijingStudent("王大锤","男",18)
stu2 = BeijingStudent("张全蛋","男",38)

#类中的数据属性是所有对象所共有的，也就是所有对象在访问类中的数据变量时，都是同一个变量，即内存地址都是相同的
print(BeijingStudent.school,id(BeijingStudent.school))  # beijing_university 4556931120
print(stu1.school,id(stu1.school))                      # beijing_university 4556931120
print(stu2.school,id(stu2.school))                      # beijing_university 4556931120

#类中的函数属性：是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象在调用方法时，会把对象本身当作第一个参数传给self
#类中定义的函数（没有被任何装饰器装饰的）是类的函数属性，类可以使用，但必须遵循函数的参数规则，有几个参数需要传几个参数
print(BeijingStudent.learn) #<function BeijingStudent.learn at 0x10f179730>
print(stu1.learn)    #<bound method BeijingStudent.learn of <__main__.BeijingStudent object at 0x10f19a6a0>>
print(stu2.learn)    #<bound method BeijingStudent.learn of <__main__.BeijingStudent object at 0x10f19a9b0>>
#learn这个函数在类和不同对象中的内存地址都不一样，也就是每一个对象都有了自己的learn方法，可以理解为不同学生在学习的时候感悟都是不一样的。

# 类不能调用类中定义的对象方法，因为上面说了，对象在调用方法的时候，程序自动把对象本身作为第一个参数传给了self
# BeijingStudent.learn() #报错，因为少了一个传参 self
BeijingStudent.learn("fgas") #当然你可以随便传一个参数给self就可以调用
# BeijingStudent.sleep("fgas") #但是sleep的时候又报错了，因为没有 fgas.Name这个属性，一般类不调对象方法，只给实例化后的对象使用
stu1.learn()  # 等价于 BeijingStudent.learn(stu1)

# 名称空间优先级 首先在对象本身中查找，找不到往类中找，类找不到往父类找，所有父类中找不到就报错，不会像函数一样往全局里去找了
print(stu1.x)  #报错，虽然全局变量中有x这个变量，但是对象的作用域只在类中
stu1.x = "from stu1"
BeijingStudent.x = "from BeijingStudent"
print(stu1.x)  #from stu1
'''

#扩展性  将数据与专门操作该数据的功能整合到一起。
'''
# 在没有学习类这个概念时，数据与功能是分离的
def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx

def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx

#每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')

# 解决方法是，把这些变量都定义成全局变量
HOST=‘127.0.0.1’
PORT=3306
DB=‘db1’
CHARSET=‘utf8’

def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx


def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx

exc1(HOST,PORT,DB,CHARSET,'select * from tb1;')
exc2(HOST,PORT,DB,CHARSET,'存储过程的名字')

# 我们必须找出一种能够将数据与操作数据的方法组合到一起的解决方法，这就是我们说的类了
class MySQLHandler:
    def __init__(self,host,port,db,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset
        self.conn=connect(self.host,self.port,self.db,self.charset)
    def exc1(self,sql):
        return self.conn.execute(sql)

    def exc2(self,sql):
        return self.conn.call_proc(sql)


obj=MySQLHandler('127.0.0.1',3306,'db1')
obj.exc1('select * from tb1;')
obj.exc2('存储过程的名字')
'''






