# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2


import os

ABS_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(ABS_PATH))
DATA_PATH = os.path.join(BASE_PATH,'data')
LOG_PATH = os.path.join(BASE_PATH,'log')
USER_LOG_NAME = os.path.join(LOG_PATH,'user.log')
BANK_LOG_NAME = os.path.join(LOG_PATH,'bank.log')
USER_BANK_FILE = os.path.join(DATA_PATH,'user_atm.json')
USER_FILE = os.path.join(DATA_PATH,'user_info.json')
PRODUCTS_FILE = os.path.join(DATA_PATH,'products.json')
