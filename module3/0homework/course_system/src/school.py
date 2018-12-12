# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import re
from src.tools import read_datas, write_datas
from config.settings import MYSCHOOL_FILE


class Myschool:
    def __init__(self):
        self.myschooles = read_datas(MYSCHOOL_FILE)

    def show_myschool(self):
        if self.myschooles:
            for mycls in self.myschooles:
                print(mycls,self.myschooles[mycls])
        else:
            print("还没有学校，赶快去添加吧！")

    def add_myschool(self):
        while True:
            info = input("请以逗号隔开输入学校号(英文或数字),学校名称(非空字符)\n")
            if re.fullmatch("^(\w)+[,|，]{1}\S+", info):
                school_lis = re.split("[，|,]", info)
                school_dict = {school_lis[0]:{"sch_name":school_lis[1]}}
                if school_lis[0] not in self.myschooles:
                    self.myschooles.update(school_dict)
                    print("添加学校 %s 成功" % school_lis[0])
                    write_datas(MYSCHOOL_FILE,self.myschooles)
                    break
                else:
                    print("%s 学校已存在" % school_lis[0])
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_myschool(self):
        while True:
            info = input("请输入待删除的学校账号：\n")
            if info in self.myschooles:
                del self.myschooles[info]
                write_datas(MYSCHOOL_FILE, self.myschooles)
                print("删除学校 %s 成功！" % info)
                break
            else:
                print("学校不存在")

    def admin(self):
        choices = ["show_myschool","add_myschool","del_myschool"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出学校操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self,choices[int(choice)])()
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Myschool()
    t.admin()

