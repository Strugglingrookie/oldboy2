import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPPATH = os.path.join(BASEPATH, 'conf', 'appController.yml')

LOGPATH = os.path.join(BASEPATH, 'log')

SYSTEMPATH = os.path.join(LOGPATH, 'server.log')

APPREPORT = os.path.join(BASEPATH, 'report', '{}')

APPPICTUREPATH = BASEPATH + os.path.sep + 'report' + os.path.sep + 'app_picture' + os.path.sep + '{}' + os.path.sep

# 生成报告时的地址
APPERROR = '../report/app_picture/{}/'