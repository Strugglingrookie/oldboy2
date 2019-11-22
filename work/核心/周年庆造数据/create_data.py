from tools import Mysql

# mysql_check = Mysql('172.29.2.158', 3343, 'lcrmapp', 'WuGeiKaiFa123', dbname='lcrm03', charset="utf8")

# 造周年庆数据
'''
sql1 = "INSERT INTO `lcrm03`.`lcrm_share_coupon`(`share_coupon_id`, `referrer_id`, `activity_id`, `product_id`, `apply_no`, `read_status`, `status`, `create_user`, `create_time`, `update_user`, `update_time`) VALUES (%s, '0190218000000003', 'AI20190918000005', 'PI20190918000004', 'PA20200920000003', '0', '1', 'ADMIN', NOW(), 'ADMIN', NOW())"
sql2 = "INSERT INTO `lcrm03`.`lcrm_share_coupon_record`( share_coupon_record_id,share_coupon_id,amount,receive_message, sort, read_status, status, create_user, create_time, update_user, update_time) VALUES (%s,%s,  888, NULL, %s, '0', '1', 'ADMIN', NOW(), 'ADMIN', NOW())"
share_coupon_id = 24001015
share_coupon_record_id = 24100167
for i in range(1000):
    sort = 1
    share_coupon_id += 1
    share_coupon_id_str = "SC201909"+str(share_coupon_id)
    res = mysql_check.exec_sql(sql1, share_coupon_id_str)
    print(res)
    for j in range(100):
        sort += 1
        share_coupon_record_id += 1
        share_coupon_record_id_str = "CR201909" + str(share_coupon_record_id)
        res = mysql_check.exec_sql(sql2,share_coupon_record_id_str,share_coupon_id_str,sort)
print('done')
'''

# 参数化
'''
with open('new.txt','w') as f:
    with open('userid.txt','r') as f1:
        for line1 in f1:
            with open('share_id.txt', 'r') as f2:
                for line2 in f2:
                    line = line1.strip() + ',' + line2
                    f.write(line)


# 造用户.
mysql_cma = Mysql('172.29.2.143', 3507, 'cmaapp', 'WuGeiKaiFa123', dbname='cma03', charset="utf8")
sql = "INSERT INTO `cma03`.`app_user`(`id`, `login_name`, `password`, `name`, `cert_no`, `encrypt_cert_no`, `birthday`, `sex`, `phone`, `user_type`, `del_flag`, `rcmd_flag`, `parent_id`, `update_date`, `login_count`, `active_count`, `protocol_list`, `channel_type`, `open_id`, `spread_source_id`, `register_from`, `industry_type`, `ocr_flag`, `cert_front`, `cert_back`, `cert_address`, `cert_end_date`, `last_login_time`, `last_login_source`, `create_time`, `ascription_city_code`) VALUES (%s, %s, '8de244a6159779e97502f833ed8a871fa64fd970ced147d47c6786ed', '友金渠道公司20170612000009', '9144**********0009', 'OTE0NE4yMDE3MDYxMjAwMDAwOQ==', NULL, '0', %s, '2', '3', '0', NULL, NOW(), NULL, NULL, NULL, '001', '0', NULL, 'core', 'null', '0', '', '', NULL, NULL, NULL, NULL, NOW(), NULL)"

# id = 328078900001
# login_name = 13573370001
# print('start!')
# for i in range(100000):
#     id += 1
#     login_name += 1
#     res = mysql_cma.exec_sql(sql, id, login_name, login_name)
# print('done!')

import requests

# url = "https://testcmasit03.yylending.com/cma/basic/activity/anniversary/draw"
# data = {"shareCouponId":"7030726e65492b305876547077414b624956356448724f6e534b422b4a686e51462f7039736c38785579413d","userId":"000210401","source":"web","macId":"web","wid":""}
# header = {"Content-Type":"application/json"}
# res = requests.post(url, json=data, headers=header).json()
# print(res)

LAS = ["NA20190927000006","NA20190929000001","NA20190929000002","NA20190929000003","NA20190929000004","NA20190929000005","NA20190929000006","NA20190929000008","NA20190927000005"]
url = "http://172.30.1.71:8766/taskAllocation"
data = {"env":"sit02","applyNo":"NA20190927000006","operator":"SUNYUI"}
header = {"Content-Type":"application/json"}
for loan in LAS:
    data["applyNo"] = loan
    res = requests.post(url, json=data, headers=header).json()
    print(res)


mysql_check = Mysql('172.29.2.144', 3503, 'omsapp', 'WuGeiKaiFa123', dbname='etldb', charset="utf8")
for i in range(667):
    sql = 'SELECT id,targetrepaydatelist FROM bhzx_loan_account_info ORDER BY id limit %s,1;'
    res = mysql_check.exec_sql(sql,i)
    id = res[0][0]
    date_org = res[0][1]
    # print(date_org)
    date_lis = date_org.split(',')
    date_lis.sort()
    date_new = ','.join(date_lis)
    # print(date_new,type(date_new))
    sql_update = 'update bhzx_loan_account_info set targetrepaydatelist=%s WHERE id=%s'
    res_update = mysql_check.exec_sql(sql_update,date_new,id)
    print(res_update)
# print(date_lis)
 '''

# lis数组取三个数随机排列 取最大值
lis = [7,9,6,2,1,5,6,3,8]
for i in range(3):
    for j in range(len(lis)-i-1):
        if lis[j] > lis[j+1]:
            lis[j],lis[j+1] = lis[j+1],lis[j]
num = str(lis[-1])+str(lis[-2])+str(lis[-3])
# print(num)

def func4(x):
    if x>0:
        func4(x-1)
        print(x)
# func4(5)

def func3(x):
    if x>0:
        print(x)
        func3(x-1)
# func3(5)

def cal(n):
    while n>1:
        print(n)
        n = n//2
# cal(64)
