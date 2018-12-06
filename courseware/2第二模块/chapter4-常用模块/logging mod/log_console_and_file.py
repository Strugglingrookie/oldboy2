# _*_coding:utf-8_*_
# created by Alex Li on 10/19/17


import logging
from logging import handlers


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return  "db backup" in record.getMessage()


#1.生成 logger 对象
logger =logging.getLogger("web")
logger.setLevel(logging.DEBUG)

#1.1 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

#2. 生成 handler对象
ch = logging.StreamHandler()
#ch.setLevel(logging.INFO)

#fh = logging.FileHandler("web.log")
#fh = handlers.RotatingFileHandler( "web.log",maxBytes=10,backupCount=3)
fh = handlers.TimedRotatingFileHandler( "web.log",when="S",interval=5,backupCount=3)
#fh.setLevel(logging.WARNING)

#2.1 把 handler对象 绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

#3.生成formatter 对象
#3.1 把formatter 对象 绑定handler对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



logger.warning("test log ")
logger.info("test log 2")
logger.debug("test log 3")
logger.debug("test log db backup 3")

#console : INFO
#global : DEBUG  default level : warning
#file :Warning

#全局设置为DEBUG后， console handler 设置为INFO, 如果输出的日志级别是debug, 那就不会在屏幕上打印