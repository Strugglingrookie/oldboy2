# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:42
# @Author  : Xiao


from src.school import Myschool
from src.group import Myclass
from src.course import Mycourse
from src.teacher import Myteacher
from src.student import Mystudent
from src.login import login_func


group = Myclass()
teacher = Myteacher()
school = Myschool()
student = Mystudent()
course = Mycourse()


def admin_run():
    choices = [school, group, course, teacher, student]
    while True:
        choice = input("0.学校 1.班级 2.课程 3.教师 4.学生 q.退出 \n 请输入您要管理的方向:\n")
        if choice.lower() == "q":
            break
        elif choice in [str(i) for i in range(len(choices))]:
            choices[int(choice)].admin()
        else:
            print("没有这个选项！")


def run():
    while True:
        choice = input("1.注册 2.登录 q.退出程序 \nyour choice:\n")
        if choice == "1":
            stu_id = student.add_stu()
            student.mystudent_operation(stu_id)
        elif choice == "2":
            user_id,role = login_func()
            print(user_id,role)
            if role == 0:
                student.mystudent_operation(user_id)
            else:
                while True:
                    teacher_choice = input("1.管理基础信息 2.教学操作 q.退出 \nyour choice:\n")
                    if teacher_choice == "1":
                        admin_run()
                    elif teacher_choice == "2":
                        teacher.myteacher_operation(user_id)
                    elif teacher_choice.lower() == "q":
                        break
                    else:
                        print("没有这个选项！")
        elif choice.lower() == "q":
            exit("886")
        else:
            print("没有这个选项！")