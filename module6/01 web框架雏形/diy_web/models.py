# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:32
# @Author  : Xiao


from lib import Mysql

sql_check_db = "show databases like 'oldboy';"
sql_create_db = 'create database oldboy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'
sql_check_table = 'show tables;'
sql_create_table ='create table user_info(id int(10) PRIMARY KEY auto_increment,name VARCHAR(20),password VARCHAR(20),age int(10))'
sql_check_data = 'select count(*) from oldboy'
sql_create_data = "INSERT into user_info(name,password,age) values ('xg','a123456',18),('xk','a123456',38),('xh','a123456',28)"


mysql_check = Mysql('localhost', 3306, 'root', 'root', charset="utf8")

if mysql_check.exec_sql(sql_check_db):
    mysql_create = Mysql('localhost', 3306, 'root', 'root',dbname='oldboy', charset="utf8")
    if mysql_create.exec_sql(sql_check_table):
        if not mysql_create.exec_sql(sql_check_data):
            mysql_create.exec_sql(sql_create_data)
    else:
        mysql_create.exec_sql(sql_create_table)
        mysql_create.exec_sql(sql_create_data)
else:
    mysql_check.exec_sql(sql_create_db)
    mysql_create = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
    mysql_create.exec_sql(sql_create_table)
    mysql_create.exec_sql(sql_create_data)
