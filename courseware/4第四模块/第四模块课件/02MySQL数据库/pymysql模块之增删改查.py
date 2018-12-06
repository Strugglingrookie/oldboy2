#1、增删改
import pymysql

# 建立链接
conn=pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db9',
    charset='utf8'
)

# 拿游标
cursor=conn.cursor()

# 执行sql
# 增、删、改
sql='insert into userinfo(user,pwd) values(%s,%s)'
# rows=cursor.execute(sql,('wxx','123'))
# print(rows)
# rows=cursor.executemany(sql,[('yxx','123'),('egon1','111'),('egon2','2222')])
# print(rows)

rows=cursor.executemany(sql,[('egon3','123'),('egon4','111'),('egon5','2222')])
print(cursor.lastrowid)

conn.commit()
# 关闭
cursor.close()
conn.close()



#2、查询
# import pymysql
#
# # 建立链接
# conn=pymysql.connect(
#     host='192.168.10.15',
#     port=3306,
#     user='root',
#     password='123',
#     db='db9',
#     charset='utf8'
# )

# 拿游标
# cursor=conn.cursor(pymysql.cursors.DictCursor)

# 执行sql
# 查询
# rows=cursor.execute('select * from userinfo;')
# print(rows)
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())


# print(cursor.fetchmany(2))

# print(cursor.fetchall())
# print(cursor.fetchall())



# cursor.scroll(3,mode='absolute') # 相对绝对位置移动
# print(cursor.fetchone())
# cursor.scroll(2,mode='relative') # 相对当前位置移动
# print(cursor.fetchone())

#

# 关闭
# cursor.close()
# conn.close()

























