# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/8


# 元类
# 一切皆对象
# 可以被引用 x = obj
# 可以当做参数传递给函数
# 可以当做函数的返回值return
# 可以当做容器的元素 l = [obj1,obj2]

# 用type产生类
# 类的三个特性    类名 基类(类的父类) 类的名称空间
# class_name = "Student"
# class_bases = (object,)
class_body = """
school = 'beijing_university'
def __init__(self,name):
    self.name = name
def call(self):
    print('my name is %s' % self.name)
"""
# class_dict = {}

# exec(str,globals,locals) exec在globals的作用域执行str代码，将执行产生的变量放到局部变量locals里。注意globals,locals必须都是字典
# exec(class_body,globals(),class_dict)  # exec 生成类的名称空间
# Student = type(class_name,class_bases,class_dict) # type 接类的三要素 类名 基类(类的父类) 类的名称空间  实例化生成一个类
# print(Student)
# stu1 = Student("xg")
# print(stu1.name)
# stu1.call()

# 既然知道了类就是type产生的，那么我们可以修改type来达到控制类的产生过程
# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dict):
#         if not class_name.istitle():
#             raise TypeError('类名的首字母必须大写')
#         if "__doc__" not in class_dict or not class_dict["__doc__"].strip():
#             raise TypeError('类必须要有注释')
#         super(Mymeta,self).__init__(class_name,class_bases,class_dict)
#

# class people(object,metaclass=Mymeta):  # 报错，因为类名首字母没有大写
#     pass
# class People(object,metaclass=Mymeta):  # 报错，因为没有注释
#     pass
# class People(object,metaclass=Mymeta):  # 没问题了
#     '''
#     这是People类
#     '''
#     pass


# 也可以控制实例化行为
# 实例化的实质是在调用类，然后返回了一个对象，可以想到的是调用类的时候，自动触发了元类的 __call__方法，而且返回了对象
# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dict):
#         if not class_name.istitle():
#             raise TypeError('类名的首字母必须大写')
#         if "__doc__" not in class_dict or not class_dict["__doc__"].strip():
#             raise TypeError('类必须要有注释')
#         super(Mymeta,self).__init__(class_name,class_bases,class_dict)
#
#     def __call__(self, *args, **kwargs):
#         # 创建一个对象
#         obj = object.__new__(self)
#         # 初始化对象
#         self.__init__(obj, *args, **kwargs)
#         # 返回对象
#         return obj

# class People(object,metaclass=Mymeta):
#     '''
#     这是People类
#     '''
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):  # 对象加上括弧直接就调用这个方法
#         print("my name is %s"%self.name)
#
# p1 = People("xg")
# p1()

# 控制实例化的应用  单例模式
#实现方式一：
# class MySQL:
#     __instance=None #__instance=obj1
#
#     def __init__(self):
#         self.host='127.0.0.1'
#         self.port=3306

#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             obj=cls()
#             cls.__instance=obj
#         return cls.__instance
#
#     def conn(self):
#         pass
#
#     def execute(self):
#         pass
#
# # obj1=MySQL()
# # obj2=MySQL()
# # obj3=MySQL()
# #
# # print(obj1)
# # print(obj2)
# # print(obj3)
#
# obj1=MySQL.singleton()
# obj2=MySQL.singleton()
# obj3=MySQL.singleton()
#
# print(obj1 is obj3)

#实现方式二：元类的方式
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名的首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)
        self.__instance=None

    def __call__(self, *args, **kwargs): #obj=Chinese('egon',age=18)
        if not self.__instance:
            obj=object.__new__(self)
            self.__init__(obj)
            self.__instance=obj

        return self.__instance



class Mysql(object,metaclass=Mymeta):
    '''
    mysql xxx
    '''
    def __init__(self):
        self.host='127.0.0.1'
        self.port=3306

    def conn(self):
        pass

    def execute(self):
        pass



obj1=Mysql()
obj2=Mysql()
obj3=Mysql()

print(obj1 is obj2 is obj3)
