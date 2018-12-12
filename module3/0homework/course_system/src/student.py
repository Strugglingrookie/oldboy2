# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:44
# @Author  : Xiao


import re
from src.school import Myschool
from src.group import Myclass
from src.course import Mycourse
from src.tools import read_datas, write_datas
from config.settings import MYSTUDENT_FILE
from config.settings import MYCLASS_FILE



class Mystudent:
    def __init__(self):
        self.stus = read_datas(MYSTUDENT_FILE)
        self.school = Myschool()
        self.group = Myclass()
        self.course = Mycourse()

    def show_mystudent(self):
        if self.stus:
            for student in self.stus:
                print(student,self.stus[student])
        else:
            print("还没有学生，赶快去添加吧！")

    def add_stu(self):   # 学校名称 班级列表 姓名 成绩 学费状态 角色编号
        while True:
            print(self.school.myschooles)
            info = input("请以逗号隔开输入学生号(英文或数字),学校编号,学生名称(非空字符),密码\n").strip()
            if re.fullmatch("^(\w)+[,|，]{1}(\d)+[,|，]{1}(\S)+", info):
                student_lis = re.split("[，|,]", info)
                if student_lis[1] in self.school.myschooles:
                    stu_id = "S"+ student_lis[0]
                    sch_id = student_lis[1]
                    sch_name = self.school.myschooles[student_lis[1]]["sch_name"]
                    stu_name = student_lis[2]
                    pwd = student_lis[-1]
                    stu_body = {"sch_id":sch_id,"sch_name":sch_name,"stu_name":stu_name,"is_pay":0,"role":0,"pwd":pwd}
                    student_dict = {stu_id:stu_body}
                    if student_lis[0] not in self.stus:
                        self.stus.update(student_dict)
                        print("学生 %s 注册成功" % student_lis[2])
                        write_datas(MYSTUDENT_FILE, self.stus)
                        return stu_id
                    else:
                        print("%s 学生已存在" % student_lis[0])
                else:
                    print("输入学校编号不存在,请参照提示按格式输入！")
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_mystudent(self):
        while True:
            info = input("请输入待删除的学生编号：\n").strip()
            if info in self.stus:
                del self.stus[info]
                write_datas(MYSTUDENT_FILE, self.stus)
                print("删除学生 %s 成功！" % info)
                break
            else:
                print("学生不存在")

    def choose_class(self,stu_id):
        if self.stus[stu_id].get("group_name"):
            print("你已经选择了班级 %s " % self.stus[stu_id].get("group_name"))
            return self.stus[stu_id].get("group_name")
        if not self.group.myclasses:
            print("还没有班级，请稍后！")
            return None
        while True:
            for k,v in self.group.myclasses.items():
                print(k,v)
            choice = input("请输入班级编号选择班级\n").strip()
            if choice in self.group.myclasses:
                self.stus[stu_id]["group_id"] = choice
                self.stus[stu_id]["group_name"] = self.group.myclasses[choice]["group_name"]
                self.group.myclasses[choice]["students"].append(stu_id)
                write_datas(MYSTUDENT_FILE, self.stus)
                write_datas(MYCLASS_FILE, self.group.myclasses)
                self.group.write_myclass()
                print("选择班级 %s 成功，赶快去缴费吧！" % self.stus[stu_id]["group_name"])
                break
            print("选择的班级序号不存在！")

    def pay_class(self,stu_id):
        if self.stus[stu_id].get("group_id"):
            if not self.stus[stu_id]["is_pay"]:
                group_id = self.stus[stu_id]["group_id"]
                crs_id = self.group.myclasses[group_id]["crs_id"]
                course_price = self.course.mycourses[crs_id]["price"]
                while True:
                    money = input("请缴费 %s \n" % course_price).strip()
                    if money.isdigit() and float(money) == course_price:
                        self.stus[stu_id]["is_pay"] = 1
                        write_datas(MYSTUDENT_FILE, self.stus)
                        print("缴费成功！")
                        break
                    else:
                        print("缴费金额不是 %s " % course_price)
            else:
                print("学费已经交过了！")
        else:
            print("您还没添加课程！")

    def look_score(self,stu_id):
        if  self.stus[stu_id].get("score"):
            print("您当前的分数是 %s" % self.stus[stu_id].get("score"))
        else:
            print("还没有老师给你评价成绩！")

    def admin(self):
        choices = ["show_mystudent","add_stu","del_mystudent"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出管理员操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self,choices[int(choice)])()
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")

    def mystudent_operation(self,stu_id):
        choices = ["choose_class","pay_class","look_score"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self, choices[int(choice)])(stu_id)
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Mystudent()
    t.admin()
    t.mystudent_operation("1")


