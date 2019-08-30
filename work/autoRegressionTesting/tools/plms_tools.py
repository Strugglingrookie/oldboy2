import cx_Oracle


def oracle_sql(db_info, sql):
    conn=cx_Oracle.connect(db_info)
    c=conn.cursor()
    tmp=c.execute(sql)
    res = tmp.fetchall()
    c.close()
    conn.close()
    return res


def mysql_sql(sql, **kwargs):
    import pymysql
    conn = pymysql.connect(**kwargs)
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


if __name__ == "__main__":
    # db_info = 'yjsdata/wugeikaifa123@172.29.2.145:1522/YYFAX03'
    # sql = "SELECT PAY_OFF_FLAG from (select * from PH_LOANOUT_FEE_REPAY_RECORD f where f.LOAN_NO='LA20181022000018' ORDER BY UPDATE_TIME DESC) WHERE ROWNUM<2"
    # print(oracle_sql(db_info, sql))
    dic = {'host': '172.29.2.144', 'port': 3503, 'password': 'WuGeiKaiFa123', 'user': 'plmsapp', 'db': 'plmsdb08'}
    sql = "SELECT * FROM plms_case_distribute WHERE attribute_queue=300001 AND sterm+20<total_sterm LIMIT 1"
    print(mysql_sql(sql, **dic))


