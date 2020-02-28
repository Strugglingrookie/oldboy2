# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/27 10:45
# @File   : log_write.py


import logging
import traceback
from logging import handlers


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父方法object来生成一个实例
            cls._instance = super().__new__(cls)
        # 如果已经存在实例就返回这个实例
        return cls._instance


class Mylog(Singleton):
    def __init__(self, log_path='./test.log', log_level=''):
        # 判断是否存在 logger 实例，不存在才初始化
        # 避免每次实例化的时候都执行一遍，会导致增加多个handler到logger
        if "logger" not in self.__dict__:
            self.log_path = log_path
            self.log_level = log_level.lower()
            self.logger = logging.getLogger("ATP")
            self.logger.setLevel(logging.DEBUG)

            # 日志输出到控制台的 handler
            self.ch = logging.StreamHandler()

            # 日志输出到文件的 handler 日志大小达到5m的时候备份
            self.fh = handlers.RotatingFileHandler(self.log_path, maxBytes=1024 * 1024 * 5, backupCount=3)
            # self.handler = handlers.TimedRotatingFileHandler(self.log_path,when="D",interval=1,backupCount=3)

            self.set_level()
            self.set_format()
            self.add_handler()

    def set_level(self):
        if self.log_level == 'error':
            self.ch.setLevel(logging.ERROR)
            self.fh.setLevel(logging.ERROR)
        elif self.log_level == 'warning':
            self.ch.setLevel(logging.WARNING)
            self.fh.setLevel(logging.WARNING)
        elif self.log_level == 'info':
            self.ch.setLevel(logging.INFO)
            self.fh.setLevel(logging.INFO)
        else:
            self.ch.setLevel(logging.DEBUG)
            self.fh.setLevel(logging.DEBUG)

    def set_format(self):
        self.formatter = logging.Formatter('%(asctime)s - %(threadName)s_%(thread)d '
                                           '%(levelname)s %(module)s.%(funcName)s:%(lineno)s - %(message)s')
        self.ch.setFormatter(self.formatter)
        self.fh.setFormatter(self.formatter)

    def add_handler(self):
        # 将两个输出方式都加载到 logger里
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    log = Mylog().get_logger()
    log2 = Mylog().get_logger()

    # 下面所有的日志写到 atp.log,而不是 atp2.log
    try:
        print(int('1.1asd'))
    except:
        log.error(traceback.format_exc())
        log2.error("test shit error")
    log.debug("test debug")
    log.info("test info")
    log2.warning("test warning")
    log2.error("test error")

    print(id(log), id(log2))
    # 可以看到两个实例的内存地址是一样的
