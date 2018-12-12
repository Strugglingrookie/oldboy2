# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:43
# @Author  : Xiao


import re
from src.school import Myschool
from src.group import Myclass
from src.student import Mystudent
from src.tools import read_datas, write_datas
from config.settings import MYTEACHER_FILE
from config.settings import MYCLASS_FILE
from config.settings import MYSTUDENT_FILE


class Myteacher:
    def __init__(self):
        self.teachers = read_datas(MYTEACHER_FILE)
        self.groups = read_datas(MYCLASS_FILE)
        self.stus = read_datas(MYSTUDENT_FILE)
        self.group = Myclass()
        self.school = Myschool()
        self.student = Mystudent()

    def show_myteacher(self):
        if self.teachers:
            for teacher in self.teachers:
                print(teacher,self.teachers[teacher])
        else:
            print("还没有教师，赶快去添加吧！")

    def add_teacher(self):   # 学校名称 姓名 班级列表 角色编号1；
        schools = self.school.myschooles
        while True:
            print(schools)
            info = input("请以逗号隔开输入教师编号(英文或数字),学校编号,教师名称(非空字符),密码\n")
            if re.fullmatch("^(\w)+[,|，]{1}(\d)+[,|，]{1}(\S)+[,|，]{1}(\S)+", info):
                teacher_lis = re.split("[，|,]", info)
                if teacher_lis[1] in schools:
                    teacher_id = "T" + teacher_lis[0]
                    sch_id = teacher_lis[1]
                    sch_name = schools[teacher_lis[1]]["sch_name"]
                    teacher_name = teacher_lis[2]
                    pwd = teacher_lis[-1]
                    teacher_body = {"sch_id":sch_id,"sch_name":sch_name,"teacher_name":teacher_name,"role":1,"groups":[],"pwd":pwd}
                    teacher_dict = {teacher_id:teacher_body}
                    if teacher_lis[0] not in self.teachers:
                        self.teachers.update(teacher_dict)
                        print("添加教师 %s 成功" % teacher_lis[2])
                        write_datas(MYTEACHER_FILE,self.teachers)
                        break
                    else:
                        print("%s 教师已存在" % teacher_lis[0])
                else:
                    print("输入学校编号不存在,请参照提示按格式输入！")
            else:
                print("输入信息有误,请参照提示按格式输入！")

    def del_myteacher(self):
        while True:
            info = input("请输入待删除的教师编号：\n")
            if info in self.teachers:
                del self.teachers[info]
                write_datas(MYTEACHER_FILE, self.teachers)
                print("删除教师 %s 成功！" % info)
                break
            else:
                print("教师不存在")

    def choose_class(self,teacher_id):
        if not self.groups:
            print("还没有班级，请稍后！")
            return None
        while True:
            for k,v in self.groups.items():
                if v['sch_id'] == self.teachers[teacher_id]['sch_id']:
                    print(k,v)
            choice = input("请输入班级编号选择班级\n")
            if choice in self.teachers[teacher_id].get("groups"):
                print("你已经选择了班级 %s " % self.groups.get(choice)['group_name'])
                return self.groups.get(choice)
            if choice in self.groups:
                self.teachers[teacher_id].get("groups").append(choice)
                self.groups.get(choice)['teachers'].append(teacher_id)
                write_datas(MYTEACHER_FILE, self.teachers)
                write_datas(MYCLASS_FILE, self.groups)
                print("选择班级 %s 成功！" % self.groups.get(choice)['group_name'])
                return self.groups.get(choice)
            print("选择的班级编号不存在！")

    def look_stus(self,teacher_id):
        if not self.teachers[teacher_id]['groups']:
            print("还没有选择班级！")
            return None
        while True:
            for k in self.teachers[teacher_id]['groups']:
                print(k)
            choice = input("请输入班级编号选择查看的班级,q退出\n")
            if choice in self.teachers[teacher_id]['groups'] and self.groups[choice]['students']:
                for stu_id in self.groups[choice]['students']:
                    print(self.stus[stu_id])
                break
            if choice.lower() == "q":
                break
            print("选择的班级编号不存在 或 当前班级还没有加入学生！")

    def modify_stu_score(self,teacher_id):
        if not self.teachers[teacher_id]['groups']:
            print("还没有选择班级！")
            return None
        while True:
            has_stus = 0
            for k,v in self.stus.items():
                if v.get('group_id') in self.teachers[teacher_id]['groups']:
                    has_stus = 1
                    print(k,v)
            if has_stus:
                info = input("请以逗号隔开输入学生编号，成绩\n")
                if re.fullmatch("^(\w)+[,|，]{1}(\d)+", info):
                    info = re.split("[，|,]", info)
                    if info[0] in self.stus and info[1].isdigit():
                        self.stus[info[0]]["score"] = float(info[1])
                        write_datas(MYSTUDENT_FILE, self.stus)
                        print("修改 %s 的成绩为 %s 成功" % (self.stus[info[0]]["stu_name"],info[1]))
                        break
                    print("选择的学生编号不存在 或 输入的成绩不是数字！")
                print("未按格式输入！")
            else:
                print("您的课程还没有加入学生！")
                break

    def admin(self):
        choices = ["show_myteacher","add_teacher","del_myteacher"]
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

    def myteacher_operation(self,teacher_id):
        choices = ["choose_class","look_stus","modify_stu_score"]
        while True:
            for index, value in enumerate(choices):
                print("%10s:\t%s" % (index, value))
            choice = input("请输入以上功能编号进行操作，输入q退出教师操作！\n").strip()
            if choice.isdigit() and int(choice) in [i for i in range(len(choices))]:
                getattr(self, choices[int(choice)])(teacher_id)
            elif choice.lower() == "q":
                break
            else:
                print("输入有误！")


if __name__ == "__main__":
    t = Myteacher()
    t.admin()
    t.myteacher_operation("1")