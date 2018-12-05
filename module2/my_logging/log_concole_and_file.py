# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/30


import logging
from logging import  handlers

#1.生成loger 对象
logger = logging.getLogger("web")
#日志级别过滤顺序：全局-->haddler  全局默认是warning,那么不设置的情况下控制台和文件只能在warning级别的基础上进行设置，不能输出info和debug
# logger.setLevel(logging.INFO)

#1.1 filter加进logger
class IgnoreShit(logging.Filter):
    def filter(self,record):
        return "shit" not in record.msg  #过滤掉含有shit的日志
logger.addFilter(IgnoreShit())

#2.生成haddler 对象
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# fh = logging.FileHandler("ch_fg_test.log")
#当日志文件达到10bytes的时候，之前的日志重命名，最多存在3个，超过3个删除
fh = handlers.RotatingFileHandler("web.log",maxBytes=10,backupCount=3)
#每5秒生成一个新的日志文件，之前的日志重命名，最多存在3个，超过3个删除
fh = handlers.TimedRotatingFileHandler("web.log",when="S",interval=5,backupCount=3)
fh.setLevel(logging.DEBUG)

#2.1.生成handler绑定loger 对象
logger.addHandler(ch)
logger.addHandler(fh)

#3.生成formatter 对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

#3.1.生成formatter绑定filter 对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.debug("test debug")
logger.info("test info")
logger.warning("test warning")
logger.error("test error")
logger.error("test shit error")


