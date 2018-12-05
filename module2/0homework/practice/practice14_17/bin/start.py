# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/1


import hashlib,json,os,sys,logging
from logging import handlers

ABS_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(ABS_PATH))
USER_PATH = os.path.join(BASE_PATH,'account')
LOG_PATH = os.path.join(BASE_PATH,'log')
LOG_NAME = os.path.join(LOG_PATH,'bank.log')
sys.path.append(BASE_PATH)

logger = logging.getLogger("my_bank")
logger.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler(LOG_NAME,when="S",interval=20,backupCount=3)
fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

#用户登陆状态
online = 0
#用户数据初始化
users = {}
for file in os.listdir(USER_PATH):
    if file.endswith(".json"):
        f = open(os.path.join(USER_PATH,file),"r")
        users[os.path.splitext(file)[0]] = json.load(f)
        f.close()

def get_md5(val):
    m = hashlib.md5()
    m.update(val.encode())
    return m.hexdigest()

def login():
    global online
    while True:
        user = input("your name:").strip()
        password = get_md5(input("your password:").strip())
        if user in users  and password == users.get(user).get("password"):
            online = 1
            print("欢迎 %s 登陆系统！"%user)
            logger.info("%s登陆系统"%user)
            return user
        else:
            print("账号或密码错误！")
            logger.warning("%s 输错登陆账户信息！"%user)

def check_online(func):
    def wrapper(*args,**kwargs):
        global online
        if online:
            return func(*args,**kwargs)
        else:
            login()
            return func(*args, **kwargs)
    return wrapper

@check_online
def transfer_amount(out_user,in_user,amount):
    if in_user not in users:
        logger.warning("%s转账时，入账账户%s不存！"%(out_user,in_user))
        return "入账账户不存在！"
    if not amount.isdigit() or not(float(amount) > 0):
        logger.warning("%s转账时，输入的金额：%s 非正数"%(out_user,amount))
        return "金额必须是正数！"
    amount = float(amount)
    if users[out_user]["amount"] < (amount+0.05*amount):
        logger.warning("%s转账时，账户余额 %s 已不足！"%(out_user,users[out_user]["amount"]))
        return "金额不足！"
    users[out_user]["amount"] -= (amount+0.05*amount)
    users[in_user]["amount"] += amount
    logger.info("%s 转账给 %s 金额 %s 元！"% (out_user,in_user,amount))
    return "转账成功"

@check_online
def look_info(user):
    logger.debug("%s 查询余额！"% user)
    print("您当前的账户余额为：%s 元"%users[user]["amount"])


@check_online
def withdraw_amount(user,amount):
    if not amount.isdigit() or not(float(amount) > 0):
        logger.warning("%s提现时，输入的金额：%s 非正数"%(user,amount))
        return "金额必须是正数！"
    amount = float(amount)
    if users[user]["amount"] < (amount+0.05*amount):
        logger.warning("%s提现时，账户余额 %s 已不足！"%(user,users[user]["amount"]))
        return "金额不足！"
    users[user]["amount"] -= (amount+0.05*amount)
    logger.info("%s 提现金额 %s 元！"% (user,amount))
    return "提现成功！提现金额：%s"%amount

def run():
    user = login()
    while True:
        choice = input("1.查看账户信息\n2.转账\n3.提现\n4.退出程序\n>>:").strip()
        if choice == "1":
            look_info(user)
        elif choice == "2":
            in_user = input("请输入入账账户号：").strip()
            amount = input("请输入转账金额：").strip()
            res = transfer_amount(user,in_user,amount)
            print(res)
        elif choice == "3":
            amount = input("请输入提现金额：").strip()
            res = withdraw_amount(user,amount)
            print(res)
        elif choice == "4":
            for file_name in users:
                f2 = open(os.path.join(USER_PATH,(file_name+".json")),"w")
                json.dump(users[file_name],f2)
            exit("退出程序！")
        else:
            print("选择有误，只能选123！")

run()


