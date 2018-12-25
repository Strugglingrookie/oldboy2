# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/12/16


import os


PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME_PATH = os.path.join(PROJECT_PATH, "home")
DATA_PATH = os.path.join(PROJECT_PATH, "data", "config.ini")
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8089
MAX_CONNECT = 5
MAX_QUEUE = 5
MAX_RUN = 2



