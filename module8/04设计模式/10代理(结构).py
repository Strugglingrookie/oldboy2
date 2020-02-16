# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/16 8:41
# @File   : 09外观(结构).py


'''
内容：为其他对象提供一种代理以控制对这个对象的访问。
应用场景：
远程代理：为远程的对象提供代理
虚代理：根据需要创建很大的对象
    例：流量不够的时候可以设置图片显示为图标，当需要看这张图片才点击加载。
    图标即为虚代理
保护代理：控制对原始对象的访问，用于对象有不同访问权限时

角色：
抽象实体（Subject）
实体（RealSubject）
代理（Proxy）

优点：
远程代理：可以隐藏对象位于远程地址空间的事实
虚代理：可以进行优化，例如根据要求创建对象
保护代理：允许在访问一个对象时有一些附加的内务处理
'''

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")


# subj = RealSubject("test.txt")
# subj.get_content()

subj = ProtectedProxy("test.txt")
print(subj.get_content())
subj.set_content("abc")
