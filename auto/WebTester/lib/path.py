import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告地址
REPORTPATH = BASEPATH + os.path.sep + 'report' + os.path.sep + 'report.html'

LOGPATH = BASEPATH + os.path.sep + 'log' + os.path.sep

WEBLOGPATH = LOGPATH + 'server.log'

# webcase path
WEBCASEPATH = BASEPATH + os.path.sep + 'test_case'

WEBPICTUREPATH = BASEPATH + os.path.sep + 'report' + os.path.sep + 'picture' + os.path.sep
