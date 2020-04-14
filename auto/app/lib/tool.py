import json
import os
from conf.settings import APP_PATH
from conf.settings import APP_PICTUREPATH,APP_ERROR
import threading
import yaml


class Tool(object):
    @property
    def app_data(self):
        with open(APP_PATH, 'rb') as f:
            data = yaml.load(f)
        return data

    def app_error_picture(self):
        # 根据当前线程名也就是设备名，拼接错误图片路径
        name = threading.current_thread().getName()
        app = APP_PICTUREPATH.format(name)
        app_list = os.listdir(app)
        app_picture = []
        for item in app_list:
            if item.endswith('.png'):
                app_picture.append((APP_ERROR.format(name) + item,))
        return app_picture

    @staticmethod
    def app_clear(app):
        '''
        每次运行之前都需要清除报错截图，不然每次都会加载到测试报告
        :param app: 错误图片路径
        '''
        app_list = os.listdir(app)
        list(map(os.remove, map(lambda file: os.path.join(app,file), app_list)))