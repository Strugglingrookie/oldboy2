import unittest
from BeautifulReport import BeautifulReport

suite = unittest.defaultTestLoader.discover('case','*.py')

bf = BeautifulReport(suite)

bf.report(description='查找测试用例的',filename='discover.html')



