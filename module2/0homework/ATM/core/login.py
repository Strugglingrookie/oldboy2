# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2


import hashlib,json
from conf.settings import USER_FILE
from core.log_write import user_logger

def json_func(file,content=None):
    f = open(file,"r+")
    if not content:
        res = json.load(f)
    else:
        f.truncate()
        f.seek(0)
        res = json.dump(content,f,ensure_ascii=False)
    f.close()
    return res

#用户登陆状态
online = 0
#用户数据初始化
users= json_func(USER_FILE)

def get_md5(val):
    m = hashlib.md5()
    m.update(val.encode())
    return m.hexdigest()

def login_func():
    global online
    while True:
        user = input("your name:").strip()
        password = get_md5(input("your password:").strip())
        if user in users  and password == users.get(user).get("password"):
            online = 1
            print("欢迎 %s 登陆系统"%user)
            user_logger.info("%s 登陆系统"%user)
            role = users.get(user).get("role")
            return user,role
        else:
            print("账号或密码错误！")
            user_logger.warning("%s 登陆时，输错登陆账户信息！"%user)

def check_online(func):
    def wrapper(*args,**kwargs):
        global online
        if online:
            return func(*args,**kwargs)
        else:
            login_func()
            return func(*args, **kwargs)
    return wrapper