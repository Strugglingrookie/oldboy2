# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 20:03
# @Author  : Xiao


import os,pickle


def read_datas(filename):
    if os.path.exists(filename):
        f = open(filename, "rb")
        res = pickle.load(f)
        f.close()
        return res
    return {}

def write_datas(filename,datas):
    f = open(filename, "wb")
    pickle.dump(datas, f)
    f.close()