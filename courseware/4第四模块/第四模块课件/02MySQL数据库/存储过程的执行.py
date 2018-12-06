#1、增删改
import pymysql

# 建立链接
conn=pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db7',
    charset='utf8'
)

# 拿游标
cursor=conn.cursor()

# 执行sql
# cursor.callproc('p1')
# print(cursor.fetchall())

cursor.callproc('p2',(2,4,0))
# print(cursor.fetchall())

cursor.execute('select @_p2_2')
print(cursor.fetchone())

# 关闭
cursor.close()
conn.close()




























