def md5_sign(json_data):
    import hashlib
    # json_data["key"] = "YJF123456A"
    m=hashlib.md5()
    list_data = []
    for key,value in json_data.items():
        if type(value)!='dict':
            str_data = key+"="+str(value)
        else:
            print(type(value))
            str_data = key + "=" + str(value[0])
        list_data.append(str_data)
    list_data_sorted=sorted(list_data)
    str_to_md5="&".join(list_data_sorted)
    str_to_md5=str_to_md5+"&key=cma"
    print(str_to_md5)
    m.update(str_to_md5.encode())
    sign = m.hexdigest()
    return sign

def secrete_md5(passwd):#密码加密的函数
    import hashlib
    md=hashlib.md5()
    md.update(passwd.encode())
    first=md.hexdigest()
    md.update(first.encode())
    return md.hexdigest()

def get_sign(json_data):
    import hashlib
    m=hashlib.md5()
    str_to_md5='sign_test_key'+json_data
    print(str_to_md5)
    m.update(str_to_md5.encode())
    sign = m.hexdigest()
    return sign

def oprate_sql(sql, HOST, USER, PASSWD, port=3306, DBNAME='', charset='utf8'):#定义操作sql语句的函数，如果是select或show则返回查询内容
    import pymysql
    if DBNAME:
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, db=DBNAME, charset=charset,port=port)
    else:
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, charset=charset,port=port)
    cur = conn.cursor()
    cur.execute(sql)
    if sql.strip().lower().startswith('select') or sql.strip().lower().startswith('show'):
        res = cur.fetchall()
    else:
        conn.commit()
        res = 'ok'
    cur.close()
    conn.close()
    return res
