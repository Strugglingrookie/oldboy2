import pymysql
from config.setting import MYSQL_INFO
class MySQL:
    def __init__(self):
        self.conn = pymysql.connect(**MYSQL_INFO)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('连接已经被关闭了')

    def execute_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()
    def execute_many(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

my = MySQL()

