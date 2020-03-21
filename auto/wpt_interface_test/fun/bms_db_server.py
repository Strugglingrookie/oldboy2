#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 16:13
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : bms_db_server.py
# @Software: PyCharm



import  sys
from fun import  public
import pymysql
from settings import  config


class DBConnection:
    def __init__(self):
        self.__conn_dict = config.bms_mysql_default_conn
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



class SellerRepository:

    def __init__(self):
        self.conn = DBConnection()

    def handel_query(self,seller_id):

        cursor = self.conn.connect()

        sql = " select is_scene,user_id from bms_seller where seller_id = '%s'; "

        new_sql = sql%(seller_id)

        public.log_record('查询营销人员信息是否有现调权:', sys._getframe().f_lineno,new_sql)

        cursor.execute(new_sql)

        result = cursor.fetchone()

        self.conn.close()

        return result


    def query_seller_depart_unit(self,org_id):

        cursor = self.conn.connect()
        sql = """
            select t.seller_name,t.user_id,t.seller_id,t.belong_team,t1.department_name,t2.unit_name 
            from bms_seller  t , bms_department_info t1,bms_business_unit t2
            where t.belong_team = t1.department_code
            and t1.unit_code = t2.unit_code
            and t.`status` = '1'
            and t2.org_id = '%s';
        """

        new_sql = sql%(org_id)

        cursor.execute(new_sql)

        result = cursor.fetchone()

        public.log_record('查询【%s】具有现调权限的营销人员信息'%result['unit_name'], sys._getframe().f_lineno, new_sql)

        cursor.close()

        return result


    def handel_update(self,seller_id,is_scene='1'):

        cursor = self.conn.connect()

        sql = " update bms_seller set is_scene = '%s'  where seller_id = '%s';"

        new_sql = sql%(is_scene,seller_id)


        public.log_record('将营销人员是否有现调权置为【%s】(1:有现调权;0:无现调权)'%is_scene, sys._getframe().f_lineno, new_sql)

        cursor.execute(new_sql)

        self.conn.close()





if __name__ == '__main__':
	pass	
  



