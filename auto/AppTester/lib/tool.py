import json
import os
from lib.path import APPPATH
from lib.path import APPPICTUREPATH,APPERROR
import threading
import yaml


class Tool(object):
    @property
    def app_data(self):
        with open(APPPATH, 'rb') as f:
            data = yaml.load(f)
        return data

    def app_error_picture(self):
        # 根据当前线程名也就是设备名，拼接错误图片路径
        name = threading.current_thread().getName()
        app = APPPICTUREPATH.format(name)
        app_list = os.listdir(app)
        app_picture = []
        for item in app_list:
            if item.endswith('.jpg'):
                app_picture.append((APPERROR.format(name) + item,))
        return app_picture

    @staticmethod
    def app_clear(app):
        app_list = os.listdir(app)
        list(map(os.remove, map(lambda file: app + file, app_list)))