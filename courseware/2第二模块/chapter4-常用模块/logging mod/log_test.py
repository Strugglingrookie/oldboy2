# _*_coding:utf-8_*_
# created by Alex Li on 10/19/17


import logging

#
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")


logging.basicConfig(filename='log_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(process)d %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S %p')


def sayhi():
    logging.error("from sayhi....")

sayhi()
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')