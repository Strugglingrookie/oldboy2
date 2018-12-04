# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 14:50
# @Author  : Xiao


import re

#定义文件操作函数，如果传了内容，则写入，如果没传，则读取文件里的内容以字典嵌套的方式写入 datas列表，元素单位为每个员工的信息
def operate_file(filename,content=''):
    if content:
        with open(filename, "w", encoding="utf-8") as f:  #
            for i in content:
                f.write(",".join(i) + "\n")
    else:
        with open(filename, "r",encoding="utf-8") as f:
            datas = []
            for line in f:
                datas.append(line.strip().split(","))
            return datas

# 初始化全局数据
title = ["id", "name", "age", "phone", "dept", "enroll_date"]
print_title = title.copy()  # 这个是给查询打印用的，当用户只查询个别列，就展示个别列，不能对全局的title进行修改
datas = operate_file("employee_info.txt", content='')

#定义一个公共函数，返回符合条件的数据，查询、修改、删除都公用(修改、删除的前提条件是找到需要修改的员工信息)
def find_info(sql):
    global print_title  #如果不是全部列，那么需要重新赋值，因为删除不存在的咧比较麻烦，所以用了申明全局变量
    sql_lis = sql.split(" ", 7)  # 接收到的语法以' '空字符分割，可取到查找的目标列、条件列、条件、条件值
    target_colums = sql_lis[1]  # 查询目标列
    condition_colums_index = title.index(sql_lis[-3])  # 条件列的索引
    condition = sql_lis[-2]  # 条件 > = like
    condition_value = sql_lis[-1]  # 条件值
    infos = []  # 存查到的所有列信息，嵌套字典
    for i in datas:  # 将满足条件的员工信息追加到infos列表
        if condition == ">" and i[condition_colums_index].isdigit() and condition_value.isdigit():
            if float(i[condition_colums_index]) > float(condition_value):
                infos.append(i)
        if condition == "<" and i[condition_colums_index].isdigit() and condition_value.isdigit():
            if float(i[condition_colums_index]) < float(condition_value):
                infos.append(i)
        if condition == "=" and i[condition_colums_index] == condition_value:
            infos.append(i)
        if condition.lower() == "like" and condition_value in i[condition_colums_index]:
            infos.append(i)
    if target_colums != "*":  # 如果不是查询所有列，那么去掉其他列
        target_colums = target_colums.split(",")
        print_title = target_colums
        target_colums_indexs = []
        for i in target_colums:
            target_colums_indexs.append(title.index(i))  # 获取需要查找的列索引
        new_infos = []
        for i in infos:
            tmp = []  # 只保存查询目标列的数据
            for j in target_colums_indexs:
                tmp.append(i[j])
            new_infos.append(tmp)
        infos = new_infos
    return infos

# 5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、修改语句就显示修改了多少条等。
# 这里使用装饰器，装饰器内部根据调用函数前后datas的变化进行判断影响函数，如果是find语法，则根据find查询返回的列表数据判断影响的行数。
def influence(method):
    def outer(func):
        def wrapper(sql):
            berore_operate = {str(x) for x in datas}
            res = func(sql)
            if method == 'find':
                if res:
                    print("查询出了 %s 条数据!"%(len(res)-1))
                else:
                    print("没有受影响的行!")
            else:
                after_operate = {str(x) for x in datas}
                set1 = berore_operate - after_operate
                set2 = after_operate - berore_operate
                print(set1)
                print(set2)
                n = len(set1) if len(set1) > len(set2) else len(set2)
                if n:
                    print("操作影响了 %s 条数据!" %n)
                else:
                    print("没有受影响的行!")
            return res
        return wrapper
    return outer

# 1.可进行模糊查询，语法至少支持下面3种查询语法:
# find name,age from staff_table where age > 22
# find * from staff_table where dept = "IT"
# find * from staff_table where enroll_date like "2013"
@influence("find")
def print_find_info(sql):
    infos = find_info(sql)
    if infos: #当有查询到的数据时，打印数据
        infos.insert(0,print_title)
        for i in infos:
            for j in i:
                print(j.center(15," "),end="\t")
            print()
    else:
        print("没有符合条件的数据！")
    return infos

# 2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
# 语法: add staff_table Alex Li,25,134435344,IT,2015‐10‐29
@influence("add")
def add_info(sql):
    phones = [i[3] for i in datas]
    val = sql.split(" ", 2)[-1]# 接收到的语法以' '空字符分割
    if val.split(",")[-3] not in phones:
        val = str(int(datas[-1][0])+1) + "," + val
        val = val.split(",")
        print(val)
        datas.append(val)
        print("Insert success！")
    else:
        print("手机号已存在！")

# 3.可删除指定员工信息纪录，输入员工id，即可删除
# 语法: del from staff where id = 3
@influence("del")
def del_info(sql):
    find_sql ='find * from staff_table where ' + sql.split(" ", 4)[-1]  # 接收到的语法以' '空字符分割
    infos = find_info(find_sql)
    if infos:
        new_datas = datas.copy()  #这里copy下是为了下面删除，不能循环当前列表来删除列表的元素，不然索引会错乱
        for i in new_datas:
            if i in infos:
                datas.remove(i)
        print("Del success！")
    else:
        print("不存在符合条件的记录！")
    return infos

# 4.可修改员工信息，语法如下:
# update staff_table set dept="Market" where dept = "IT" 把所有dept=IT的纪录的dept改成Market
# update staff_table set age=25 where name = "Alex Li" 把name=Alex Li的纪录的年龄改成25
@influence("modify")
def modify_info(sql):
    explain_sql = sql.split(" ", 5)
    find_sql ='find * from staff_table where ' + explain_sql[-1]  # 接收到的语法以' '空字符分割
    infos = find_info(find_sql)
    modify_colum_index = title.index(explain_sql[3].split("=")[0])
    modify_value = explain_sql[3].split("=")[1]
    if infos:
        for i in datas:
            if i in infos:
                i[modify_colum_index] = modify_value
        print("Modify success！")
    else:
        print("不存在符合条件的记录！")

#启动程序，且对用户输入的sql语句进行校验，通过则调相应的函数进行操作。在用户退出程序的时候把最新的值更新到文件里保存。
def run():
    while True:
        sql = input("输入sql(语法关键字需用小写)进行员工信息操作或者输入q退出程序：\n").strip().replace('"',"")
        if sql == "q":
            operate_file("employee_info.txt", datas)
            exit("欢迎老板下次来耍！")
        if sql.lower().startswith("find"):
            match_find = re.match(r'(find|FIND) (\S*) (from|FROM) staff_table (where|WHERE) (id|name|age|phone|dept|enroll_date) ([>=<]|like|LIKE) (.*)', sql)
            if not match_find:
                print("语法有误！")
                continue
            print_find_info(sql)
        elif sql.lower().startswith("add"):
            match_add = re.match(r'(add|ADD) staff_table (.*)', sql)
            if not match_add:
                print("语法有误！")
                continue
            add_info(sql)
        elif sql.lower().startswith("del"):
            match_del = re.match(r'(del|DEL) (from|FROM) staff (where|WHERE) (id|name|age|phone|dept|enroll_date) ([>=<]|like|LIKE) (.*)',sql)
            if not match_del:
                print("语法有误！")
                continue
            del_info(sql)
        elif sql.lower().startswith("update"):
            print("update")
            match_update = re.match(r'(update|UPDATE) staff_table (set|SET) (\w*)=(.*) (where|WHERE) (id|name|age|phone|dept|enroll_date) ([>=<]|like|LIKE) (.*)',sql)
            if not match_update:
                print("语法有误！")
                continue
            modify_info(sql)
        else:
            print("语法有误！")

if __name__ == "__main__":
    run()