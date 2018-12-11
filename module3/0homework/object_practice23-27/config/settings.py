# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:42
# @Author  : Xiao


import os, sys


FILE_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
TEACHER_FILE = os.path.join(BASE_PATH,"db","teachers.pkl")
MYCLASS_FILE = os.path.join(BASE_PATH,"db","myclasses.pkl")
MYSCHOOL_FILE = os.path.join(BASE_PATH,"db","myschooles.pkl")