#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 11:34
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : wk_db_server.py
# @Software: PyCharm

import  sys
from fun import  public
import pymysql
from settings import  config


class DBConnection:
    def __init__(self):
        self.__conn_dict = config.wk_mysql_default_conn
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



class ApplyRepository:

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
            sql = " select %s from apply order by update_time desc limit 100; " % (columns)

        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = " select %s from apply where %s " % (columns, condition)
            sql = sql.strip()[:-4]
            sql = sql + ' order by create_time desc limit 1;'

            public.log_record('查询申请单信息:', sys._getframe().f_lineno,sql)

        cursor.execute(sql)

        if limit >1:
            results = cursor.fetchall()
        else:
            results =cursor.fetchone()

        return results

        self.conn.close()

    def handel_delete(self,apply_id):

        cursor = self.conn.connect()

        sql = " delete from apply  where apply_id = '%s' ; "%apply_id

        cursor.execute(sql)

        self.conn.close()

    def handel_update(self,**kwargs):

        cursor = self.conn.connect()

        sql = " update apply set %s = '%s' where apply_id = '%s' ;"

        for k,v in kwargs.items():
            new_sql = sql%(k,v,kwargs['apply_id'])
            public.log_record('修改申请单状态:',sys._getframe().f_lineno,new_sql)
            cursor.execute(new_sql)

        self.conn.close()


class AttachmentRepository:

    def __init__(self):
        self.conn = DBConnection()

    def handel_query(self, *args, **kwargs):
        cursor = self.conn.connect()

        if len(args) == 0 :
            columns = '*'
        else:
            columns = str(args).replace('(','').replace(')','').replace("'",'')[:-1]

        is_null = ''
        condition = ''

        for k, v in kwargs.items():
            is_null += v

        if is_null == '':
            sql = " select %s from attachment ; " % (columns)

        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = " select %s from attachment where %s " % (columns, condition)
            sql = sql.strip()[:-4]+';'

            public.log_record('查询影像附件信息:', sys._getframe().f_lineno,sql)

        cursor.execute(sql)


        results = cursor.fetchall()

        self.conn.close()

        return results


class ApplyToCuBaseInfoRepository:
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
          select %s from  apply t1,cu_base_info t2
          where t1.apply_id = t2.apply_id
          order by t1.create_time desc
          limit 1;
         """ %(columns)

        else:
            for k, v in kwargs.items():
                condition += " %s = '%s' and " % (k, v)

            sql = """
                   select %s from  apply t1,cu_base_info t2
                   where t1.apply_id = t2.apply_id
                   and %s
                  """ % (columns,condition)

            sql = sql.strip()[:-4]
            sql = sql + ' order by t1.create_time desc limit 1;'

            public.log_record('查询申请信息及客户信息:', sys._getframe().f_lineno, sql)

        cursor.execute(sql)

        result = cursor.fetchone()

        self.conn.close()
        return result







if __name__ == '__main__':
	pass
   