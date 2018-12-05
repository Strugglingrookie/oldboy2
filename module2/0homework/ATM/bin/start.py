# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2


import os,sys

ABS_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(ABS_PATH))
sys.path.append(BASE_PATH)

from core.login import login_func
from core.buy import user_run
from core.admin_operation import admin_run

def run():
    user,role = login_func()
    if role == 1:  #如果是管理员，走管理员运行分之
        admin_run(user)
    else:
        user_run(user)

if __name__ == "__main__":
    run()