#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 19:09
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : fatp_db_server.py
# @Software: PyCharm



import  sys
import pymysql
from fun import  public
from settings import  config


class DBConnection:
    def __init__(self):
        self.__conn_dict = config.fatp_mysql_default_conn
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



class LoadApplyRepository:

    def __init__(self):
        self.conn = DBConnection()

    def handel_query(self,limit = '', *args, **kwargs):
        cursor = self.conn.connect()

        try:
            limit = int(limit)
        except Exception:
            limit = 1

        if len(args) == 0 :
            columns = '*'
        else:
            columns = str(args).replace('(','').replace(')','').replace("'",'')[:-1]

        is_null = ''
        condition = ''

        for k, v in kwargs.items():
            is_null += v

        if is_null == '':
            sql = " select %s from fatp_loan_apply order by create_time desc limit 100; " % (columns)

        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = " select %s from fatp_loan_apply where %s " % (columns, condition)
            sql = sql.strip()[:-4]
            sql = sql + ' order by create_time desc limit 1;'

            public.log_record('查询借款申请信息', sys._getframe().f_lineno,sql)

        cursor.execute(sql)

        if limit >1:
            results = cursor.fetchall()
        else:
            results =cursor.fetchone()

        return results

        self.conn.close()

   


class ApplyToContractRepository:
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
         select  %s from fatp_loan_apply t1,fatp_contract_info t2
          where t1.contract_serial_no  = t2.serial_no
          order by t2.create_time desc
          limit 1;
         """ %(columns)

        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = """
            select  %s from fatp_loan_apply t1,fatp_contract_info t2
            where t1.contract_serial_no  = t2.serial_no
            and %s
                  """ % (columns,condition)

            sql = sql.strip()[:-4]
            sql = sql + ' order by t2.create_time desc limit 1;'

            public.log_record('查询合同及借据信息', sys._getframe().f_lineno, sql)

        cursor.execute(sql)

        result = cursor.fetchone()

        self.conn.close()

        return result




if __name__ == '__main__':
	pass
   