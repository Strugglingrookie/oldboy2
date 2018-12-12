# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import re
from src.course import Mycourse
from src.tools import read_datas, write_datas
from config.settings import MYCLASS_FILE


class Myclass:
    def __init__(self):
        self.myclasses = read_datas(MYCLASS_FILE)
        self.course = Mycourse()

    def show_myclass(self):
        if self.myclasses:
            for mycls in self.myclasses:
                print(mycls,self.myclasses[mycls])
        else:
            print("还没有班级，赶快去添加吧！")

    def add_myclass(self):  # 学校名称 班级名称 课程名 教师列表 学员列表
        courses = self.course.mycourses
        while True:
            print(courses)
            info = input("请以逗号隔开输入课程编号，班级号(英文或数字),班级名称(非空字符)\n")
            if re.fullmatch("^(\w)+[,|，]{1}(\w)+[,|，]{1}(\S)+", info):
                group_lis = re.split("[，|,]", info)
                if group_lis[0] in self.course.mycourses :
                    group_body = {}
                    group_id = group_lis[1]
                    group_body["group_name"] = group_lis[-1]
                    group_body["sch_id"] = courses[group_lis[0]]["sch_id"]
                    group_body["sch_name"] = courses[group_lis[0]]["sch_name"]
                    group_body["crs_id"] = group_lis[0]
                    group_body["crs_name"] = courses[group_lis[0]]["crs_name"]
                    group_body["teachers"] = []
                    group_body["students"] = []
                    course_dict = {group_id: group_body}
                    if group_lis[1] not in self.myclasses:
                        self.myclasses.update(course_dict)
                        print("添加班级 %s 成功" % group_body["group_name"])
                        write_datas(MYCLASS_FILE,self.myclasses)
                        break
                    else:
                        print("%s 班级编号已存在" % group_lis[2])
                else:
                    print("输入学校或课程编号不存在,请参照提示按格式输入！")
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_myclass(self):
        while True:
            info = input("请输入待删除的班级账号：\n")
            if info in self.myclasses:
                del self.myclasses[info]
                write_datas(MYCLASS_FILE,self.myclasses)
                print("删除班级 %s 成功！" % info)
                break
            else:
                print("班级不存在")

    def admin(self):
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
    t.admin()

