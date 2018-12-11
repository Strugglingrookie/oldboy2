# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import pickle, re, os
from config.settings import MYCLASS_FILE
# MYCLASS_FILE = r"E:\Study\oldboy\module3\0homework\object_practice23-27\db\myclasses.pkl"


class Myclass:
    def __init__(self):
        self.myclasses = self.__get_myclass

    @property
    def __get_myclass(self):
        if os.path.exists(MYCLASS_FILE):
            f = open(MYCLASS_FILE,"rb")
            res = pickle.load(f)
            f.close()
            return res
        return {}

    def __write_myclass(self):
        f = open(MYCLASS_FILE, "wb")
        pickle.dump(self.myclasses, f)
        f.close()

    def show_myclass(self):
        if self.myclasses:
            for mycls in self.myclasses:
                print(mycls,self.myclasses[mycls])
        else:
            print("还没有班级，赶快去添加吧！")

    def add_myclass(self):
        while True:
            info = input("请以逗号隔开输入班级号(英文或数字),班级名称(非空字符)\n")
            if re.fullmatch("^(\w)+[,|，]{1}\S+", info):
                clas_lis = re.split("[，|,]", info)
                clas_dict = {clas_lis[0]:{"name":clas_lis[1]}}
                if clas_lis[0] not in self.myclasses:
                    self.myclasses.update(clas_dict)
                    print("添加班级 %s 成功" % clas_lis[0])
                    self.__write_myclass()
                    break
                else:
                    print("%s 班级已存在" % clas_lis[0])
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_myclass(self):
        while True:
            info = input("请输入待删除的班级账号：\n")
            if info in self.myclasses:
                del self.myclasses[info]
                self.__write_myclass()
                print("删除班级 %s 成功！" % info)
            else:
                print("班级不存在")

    def myclass_operation(self):
        choices = ["show_myclass","add_myclass","del_myclass"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出班级操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self,choices[int(choice)])()
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Myclass()
    t.myclass_operation()

