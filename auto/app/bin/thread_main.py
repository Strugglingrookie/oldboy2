from lib.appController import Controller, devices_name_queue
from appCase.test_thread_login import ThreadDemo
from conf.settings import logger,APP_REPORT
from lib.result import Result
from lib import HTMLTestAppRunner
import threading
import unittest


local = threading.local()

class App():
