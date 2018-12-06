#_*_coding:utf-8_*_

import logging

# logging.basicConfig(filename='example.log',
#                     level=logging.INFO,
#                     format='%(asctime)s-%(module)s- %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()




#console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#file handler
fh = logging.FileHandler('mysql.log')
#fh.setLevel(logging.WARNING)


#formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#bind formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger = logging.getLogger("Mysql")
logger.setLevel(logging.DEBUG) #logger 优先级高于其它输出途径的


#add handler   to logger instance
logger.addHandler(ch)
logger.addHandler(fh)



#add filter
logger.addFilter(IgnoreBackupLogFilter())

logger.debug("test ....")
logger.info("test info ....")
logger.warning("start to run db backup job ....")
logger.error("test error ....")


