# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:44
# @File   : tools.py


import os
from config.settings import WEB_PICTURE_PATH


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEB_PICTURE_PATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg') or item.endswith('png'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: os.path.join(WEB_PICTURE_PATH,file), self.filelist)))

