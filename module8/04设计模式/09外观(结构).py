# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/16 8:41
# @File   : 09外观(结构).py


'''
内容：为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
角色：
外观（facade）
子系统类（subsystem classes）

优点：
减少系统相互依赖
提高了灵活性
提高了安全性

'''


class CPU:
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")


class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")


class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")


class Computer:  # Facade
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# Client

computer = Computer()
computer.run()
computer.stop()
