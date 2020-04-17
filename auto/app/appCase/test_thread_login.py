import unittest
from page.thread_page import Page
from conf.settings import logger


class ThreadDemo(unittest.TestCase):
    def __repr__(self):
        return 'appdemo'

    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    def test_a_login(self):
        self.page.login_btn()
        self.page.account()
        self.page.password()
        self.page.login()
        self.assertTrue(self.page.check(self.test_a_login.__name__),'msg')

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()


if __name__ == '__main__':
    from lib.appController import Controller

    c = Controller()
    c.server_start()
    c.check_server()
    c.driver_start()
    unittest.main()
