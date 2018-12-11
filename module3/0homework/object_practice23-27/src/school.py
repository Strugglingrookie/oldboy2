# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import pickle, re, os
from config.settings import MYSCHOOL_FILE
# myschool_FILE = r"E:\Study\oldboy\module3\0homework\object_practice23-27\db\myschooles.pkl"


class Myschool:
    def __init__(self):
        self.myschooles = self.__get_myschool

    @property
    def __get_myschool(self):
        if os.path.exists(MYSCHOOL_FILE):
            f = open(MYSCHOOL_FILE,"rb")
            res = pickle.load(f)
            f.close()
            return res
        return {}

    def __write_myschool(self):
        f = open(MYSCHOOL_FILE, "wb")
        pickle.dump(self.myschooles, f)
        f.close()

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
                school_dict = {school_lis[0]:{"name":school_lis[1]}}
                if school_lis[0] not in self.myschooles:
                    self.myschooles.update(school_dict)
                    print("添加学校 %s 成功" % school_lis[0])
                    self.__write_myschool()
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
                self.__write_myschool()
                print("删除学校 %s 成功！" % info)
            else:
                print("学校不存在")

    def myschool_operation(self):
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
    t.myschool_operation()

