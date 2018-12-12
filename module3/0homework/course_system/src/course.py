# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import re
from src.school import Myschool
from src.tools import read_datas, write_datas
from config.settings import MYCOURSE_FILE


class Mycourse:
    def __init__(self):
        self.mycourses = read_datas(MYCOURSE_FILE)
        self.school = Myschool()

    def show_mycourse(self):
        if self.mycourses:
            for course in self.mycourses:
                print(course,self.mycourses[course])
        else:
            print("还没有课程，赶快去添加吧！")

    def add_mycourse(self):   # 学校名称 课程名 周期 价格
        while True:
            print(self.school.myschooles)
            info = input("请以逗号隔开输入课程号(英文或数字),学校编号,课程名称(非空字符),周期(月为单位),价格(单位元)\n")
            if re.fullmatch("^(\w)+[,|，]{1}(\d)+[,|，]{1}(\w)+[,|，]{1}(\d)+[,|，]{1}(\d)+", info):
                course_lis = re.split("[，|,]", info)
                if course_lis[1] in self.school.myschooles:
                    crs_id = course_lis[0]
                    sch_id = course_lis[1]
                    sch_name = self.school.myschooles[course_lis[1]]["sch_name"]
                    crs_name = course_lis[2]
                    period = course_lis[3]
                    price = int(course_lis[4])
                    course_body = {"sch_id":sch_id,"sch_name":sch_name,"crs_name":crs_name,"period":period,"price":price}
                    course_dict = {crs_id:course_body}
                    if course_lis[0] not in self.mycourses:
                        self.mycourses.update(course_dict)
                        print("添加课程 %s 成功" % course_lis[2])
                        write_datas(MYCOURSE_FILE, self.mycourses)
                        break
                    else:
                        print("%s 课程已存在" % course_lis[0])
                else:
                    print("输入学校编号不存在,请参照提示按格式输入！")
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_mycourse(self):
        while True:
            info = input("请输入待删除的课程编号：\n")
            if info in self.mycourses:
                del self.mycourses[info]
                write_datas(MYCOURSE_FILE, self.mycourses)
                print("删除课程 %s 成功！" % info)
                break
            else:
                print("课程不存在")

    def admin(self):
        choices = ["show_mycourse","add_mycourse","del_mycourse"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出课程操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self,choices[int(choice)])()
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Mycourse()
    t.admin()