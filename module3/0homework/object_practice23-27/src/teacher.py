# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:43
# @Author  : Xiao


import pickle, re, os
from config.settings import TEACHER_FILE
# TEACHER_FILE = r"E:\Study\oldboy\module3\0homework\object_practice23-27\db\teachers.pkl"


class Myteacher:
    def __init__(self):
        self.teachers = self.__get_teachers

    @property
    def __get_teachers(self):
        if os.path.exists(TEACHER_FILE):
            f = open(TEACHER_FILE,"rb")
            res = pickle.load(f)
            f.close()
            return res
        return {}

    def __write_teachers(self):
        f = open(TEACHER_FILE, "wb")
        pickle.dump(self.teachers, f)
        f.close()

    def show_teacher(self):
        if self.teachers:
            for teacher in self.teachers:
                print(teacher,self.teachers[teacher])
        else:
            print("还没有老师，赶快去添加吧！")

    def add_teacher(self):
        while True:
            info = input("请以逗号隔开输入账号(英文或数字),姓名(非空字符),密码(英文或数字)\n")
            if re.fullmatch("^(\w)+[,|，]{1}\S+[,|，]{1}\w+", info):
                user_lis = re.split("[，|,]", info)
                user_dict = {user_lis[0]:{"name":user_lis[1],"password":user_lis[2]}}
                if user_lis[0] not in self.teachers:
                    self.teachers.update(user_dict)
                    print("添加老师 %s 成功" % user_lis[0])
                    self.__write_teachers()
                    break
                else:
                    print("%s 老师已存在" % user_lis[0])
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_teacher(self):
        while True:
            info = input("请输入待删除的老师账号：\n")
            if info in self.teachers:
                del self.teachers[info]
                self.__write_teachers()
                print("删除老师 %s 成功！" % info)
            else:
                print("教师不存在")

    def teacher_operation(self):
        choices = ["show_teacher","add_teacher","del_teacher"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出教师操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self,choices[int(choice)])()
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Myteacher()
    t.teacher_operation()