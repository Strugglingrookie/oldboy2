#pip3 install pymysql
import pymysql

user=input('user>>: ').strip()
pwd=input('password>>: ').strip()

# 建立链接
conn=pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db9',
    charset='utf8'
)

# 拿到游标
cursor=conn.cursor()

# 执行sql语句

sql='select * from userinfo where user = "%s" and pwd="%s"' %(user,pwd)
rows=cursor.execute(sql)

cursor.close()
conn.close()

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')