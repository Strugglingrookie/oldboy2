import sys, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

from lib.appController import Controller, devices_name_queue
from appCase.test_thread_login import ThreadDemo
from conf.settings import logger,APP_REPORT
from lib.result import Result
from lib import HTMLTestAppRunner
import threading
import unittest
import time


local = threading.local()

class App():
    def __init__(self):
        self.c = Controller()

    def case(self):
        # 通过导入测试类来实现生成测试集
        local.suite = unittest.TestLoader().loadTestsFromTestCase(ThreadDemo)

        # 生成空的结果集，用来存执行结果
        local.result = Result()

        # 运行case，并更新结果集，如执行状态
        local.res = local.suite.run(local.result)

        # 将结果通过测试手机名称进行区分
        logger.debug('当前线程的的名字：%s' % threading.current_thread().getName())
        # 当前线程的名称就是当前手机的名字
        result = {threading.current_thread().getName():local.res}

        for deviceName,result in result.items():
            report_name = deviceName + '-' + time.strftime('%Y%m%d%H%M%S')
            html = HTMLTestAppRunner.HTMLTestRunner(
                stream=open(APP_REPORT.format('{}.html'.format(report_name)),'wb'),
                verbosity=2,title='Test'
            )
            # 这个方法就是生成报告的主要函数
            html.generateReport('',result)

    def run(self):
        threads = []
        self.c.server_start()
        if self.c.check_server():
            drivers = self.c.driver_start()
            logger.info('开始执行CASE！当前启动[%s]个DRIVER！' % drivers.qsize())
            # 根据driver的个数启动对应的case
            for driver in range((drivers.qsize())):
                # 根据driver启动多线程跑case，对每个线程通过手机名 命名
                t = threading.Thread(target=self.case,name=devices_name_queue.get())
                threads.append(t)
                t.start()
        for t in threads:
            t.join()

    def run_two(self):
        '''
        已经启动好 appium
        '''
        threads = []
        drivers = self.c.driver_start()
        logger.info('开始执行CASE！当前启动[%s]个DRIVER！' % drivers.qsize())
        # 根据driver的个数启动对应的case
        for driver in range((drivers.qsize())):
            # 根据driver启动多线程跑case，对每个线程通过手机名 命名
            t = threading.Thread(target=self.case,name=devices_name_queue.get())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()


if __name__ == '__main__':
    App().run()
    # App().run_two()