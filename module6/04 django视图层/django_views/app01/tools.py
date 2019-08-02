# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:42
# @Author  : Xiao

import pymysql


class Mysql(object):
    def __init__(self, host, port, user, pwd, dbname="", charset="utf8"):
        """初始化数据库信息以及连接"""
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.charset = charset
        self.conn = None  # 给析构函数用的，如果存在链接，则需要关闭链接，没有就不用管
        self.conn = self.get_conn
        self.cur = None
        self.cur = self.get_cur

    @property
    def get_conn(self):
        """根据传参判断是否有传数据库名，然后做不同的链接操作"""
        try:
            if self.dbname:
                conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                            password=self.pwd, database=self.dbname, charset=self.charset)
                return conn
            else:
                conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                            password=self.pwd, charset=self.charset)
                return conn
        except Exception as e:
            print(e)

    @property
    def get_cur(self):
        """获取游标"""
        if self.conn:
            return self.conn.cursor()

    def exec_sql(self, sql, *args):
        """
        执行sql，根据不同的sql语法做不同的操作：
        查询就返回查询结果列表，其他成功就返回受影响的行数整型，报错返回报错信息字符串
        *args是为了防止sql注入，自己拼接的sql语法字符串可能被sql注入,
        这里的用法是sql不需要自己拼接，直接将变量按顺序传进来，pymysql自动拼接，而且避免了sql注入的问题
        如：
        sql = "insert into test.student VALUES (19,%s,'English',%s);"
        res = test_mysql.exec_sql(sql,"yangxga",100)
        """
        try:
            rows = self.cur.execute(sql, args)  # rows记录受影响的行
            if sql.strip().lower().startswith('select') or sql.strip().lower().startswith('show'):
                res = self.cur.fetchall()
                res = self.format_res(res)
                print(res)
                return res
            else:
                self.conn.commit()  # 非查询语句需要提交才能生效
                res = rows
                print(res)
                return res
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def format_res(res):
        """格式化数据库查找到的结果，如果"""
        res_lis = []
        if res:
            for i in res:
                res_lis.append(i)
        return res_lis

    def __del__(self):
        """析构函数，关闭鼠标，断开连接"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
