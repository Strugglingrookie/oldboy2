# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 20:11
# @File   : operate_db.py


import pymysql, traceback


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


class MySql(Singleton):
    def __init__(self, host, user, pwd, dbname="", port=3306, charset="utf8"):
        """
        初始化数据库信息以及连接
        如果已经存在连接，不再初始化
        减少与数据库的连接，提升性能
        """
        if "conn" not in self.__dict__:
            self.host = host
            self.port = port
            self.user = user
            self.pwd = pwd
            self.dbname = dbname
            self.charset = charset
            self.conn = self.get_conn
            self.cur = self.get_cur

    @property
    def get_conn(self):
        """根据传参判断是否有传数据库名，然后做不同的链接操作"""
        try:
            if self.dbname:
                conn = pymysql.connect(host=self.host, port=self.port,
                                       user=self.user, password=self.pwd,
                                       database=self.dbname, charset=self.charset)
                return conn
            else:
                conn = pymysql.connect(host=self.host, port=self.port,
                                       user=self.user, password=self.pwd,
                                       charset=self.charset)
                return conn
        except:
            print(traceback.format_exc())
            return None

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
        这里的用法是sql不需要自己拼接，直接将变量按顺序传进来，
        pymysql自动拼接，而且避免了sql注入的问题
        如：
        sql = "insert into test.student VALUES (19,%s,'English',%s);"
        res = test_mysql.exec_sql(sql,"yangxga",100)
        """
        try:
            sql = sql.strip()
            if sql:
                rows = self.cur.execute(sql, args)  # rows记录受影响的行
                if sql.strip().startswith('select') or sql.strip().startswith('show'):
                    res = self.cur.fetchall()
                    res = self.format_res(res)
                else:
                    self.conn.commit()  # 非查询语句需要提交才能生效
                    res = rows
                return res
            else:
                raise TypeError("sql不能为空！")
        except:
            print(traceback.format_exc())
            return traceback.format_exc()

    @staticmethod
    def format_res(res):
        """格式化数据库查找到的结果,元组转换为字典"""
        res_list = []
        if res:
            for row in res:
                row_data = []
                for val in row:
                    row_data.append(val)
                res_list.append(row_data)
        return res_list

    def __del__(self):
        """析构函数，关闭鼠标，断开连接"""
        try:
            self.cur.close()
            self.conn.close()
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    DB_INFO = {
        "host": "localhost",
        "user": "root",
        "pwd": "123456",
        "dbname": "utp",
        "port": 3308
    }
    sql_obj = MySql(**DB_INFO)
    res = sql_obj.exec_sql("show databases;")
    print(res)
    # res2 = sql_obj.exec_sql("select id from a where age=18;")
    # print(res2)
    sql = "select * from userinfo where username=%s"
    # sql = "delete from userinfo where username=%s"
    res1 = sql_obj.exec_sql(sql, "xiaogang")
    print(res1)
