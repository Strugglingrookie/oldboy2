#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 18:40
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : cma_db_server.py
# @Software: PyCharm

import  sys
import pymysql
from fun import  public
from settings import  config


class DBConnection:
    def __init__(self):
        self.__conn_dict = config.cma_mysql_default_conn
        self.conn = None
        self.cursor = None

    def connect(self, cursor=pymysql.cursors.DictCursor):
        # 创建数据库连接
        self.conn = pymysql.connect(**self.__conn_dict)
        # 创建游标
        self.cursor = self.conn.cursor(cursor=cursor)
        return self.cursor

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

#用户表和推荐人表
class UserToRcmdRecord:
    def __init__(self):
        self.conn = DBConnection()

    def handel_query(self, *args, **kwargs):
        cursor = self.conn.connect()

        if len(args) == 0:
            columns = '*'
        else:
            columns = str(args).replace('(', '').replace(')', '').replace("'", '')[:-1]

        is_null = ''
        condition = ''

        for k, v in kwargs.items():
            is_null += v

        if is_null == '':

            sql = """
           select %s from app_user t1,app_rcmd_record t2
           where t1.id = t2.rcmder  
           and t1.id != ''
           and t1.cert_no != ''
           order by t2.rcmd_time desc
           limit 1;
             """ %(columns)


        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = """
             select %s from app_user t1,app_rcmd_record t2
             where t1.id = t2.rcmder  
             and t1.id != ''
             and t1.encrypt_cert_no != ''
             and t2.status = '06' 
             and %s
                  """ % (columns,condition)

            sql = sql.strip()[:-4]
            sql = sql + ' order by t2.rcmd_time desc limit 1;'

        public.log_record('查询CMA推荐人信息:', sys._getframe().f_lineno, sql)
        cursor.execute(sql)

        result = cursor.fetchone()

        self.conn.close()

        return result


if __name__ == '__main__':
	pass

   

