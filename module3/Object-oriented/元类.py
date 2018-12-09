# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 元类
# 一切皆对象
# 可以被引用 x = obj
# 可以当做参数传递给函数
# 可以当做函数的返回值return
# 可以当做容器的元素 l = [obj1,obj2]

# 类的三个特性
# 类名 基类(类的父类) 类的名称空间
class_name = "Student"
class_bases = (object,)
class_body = """
school = 'beijing_university'

def __init__(self,name):
    self.name = name
    
def call(self):
    print('my name is %s' % self.name)
"""
class_dict = {}
exec(class_body,globals(),class_dict)  # exec 生成类的名称空间

Student = type(class_name,class_bases,class_dict) # type 接类的三要素 类名 基类(类的父类) 类的名称空间  实例化生成一个类
print(Student)

stu1 = Student("xg")
print(stu1.name)
stu1.call()
