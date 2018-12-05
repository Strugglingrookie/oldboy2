# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/2


import logging
from logging import handlers
from conf.settings import USER_LOG_NAME,BANK_LOG_NAME

#用户操作日志,之前考虑的是把拿日志和用户交互，但是打印到屏幕上时有一定延迟，不能及时和用户交互，所以还是用print和用户交互。
user_logger = logging.getLogger("my_user")
user_logger.setLevel(logging.DEBUG)
# user_ch = logging.StreamHandler()
user_fh = handlers.TimedRotatingFileHandler(USER_LOG_NAME,when="D",interval=1,backupCount=30)
# user_ch_formatter = logging.Formatter('%(asctime)s - %(message)s')
user_fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')
# user_ch.setFormatter(user_ch_formatter)
user_fh.setFormatter(user_fh_formatter)
user_logger.addHandler(user_fh)
# user_logger.addHandler(user_ch)

#ATM记录操作日志
bank_logger = logging.getLogger("my_bank")
bank_logger.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler(BANK_LOG_NAME,when="D",interval=1,backupCount=30)
fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')
fh.setFormatter(fh_formatter)
bank_logger.addHandler(fh)