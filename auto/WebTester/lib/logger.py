from logging import handlers
import logging
from lib.path import WEBLOGPATH


class Logger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Logger.__instance:
            Logger.__instance = object.__new__(cls, *args)
        return Logger.__instance

    def __init__(self):
        # 格式化log的模板
        self.formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')

        # 声明一个log对象
        self.logger = logging.getLogger('log')
        # 设置全局log级别
        self.logger.setLevel(logging.DEBUG)

        # 文件log
        self.filelogger = handlers.RotatingFileHandler(WEBLOGPATH,
                                                       maxBytes=5242880,
                                                       backupCount=3
                                                       )
        # 屏幕log
        self.console = logging.StreamHandler()
        # 对屏幕设置级别
        self.console.setLevel(logging.DEBUG)

        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

    def log(self):
        return self.logger


logger = Logger().log()