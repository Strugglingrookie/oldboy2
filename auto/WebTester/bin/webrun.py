from lib.logger import logger
from lib.path import WEBCASEPATH,REPORTPATH
from lib.HTMLTestRunner import HTMLTestRunner
import unittest


class Main(object):
    def run(self):
        suite = unittest.TestSuite()
        cases = unittest.defaultTestLoader.discover(WEBCASEPATH)
        for case in cases:
            suite.addTest(case)
        f = open(REPORTPATH,'wb')
        runner = HTMLTestRunner(f,verbosity=1,title=u'测试报告', description=u'用例执行情况：')
        runner.run(suite)
        f.flush()
        f.close()
if __name__ == '__main__':
    Main().run()