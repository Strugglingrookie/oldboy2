import unittest
from page.thread_page import Page


class QQDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    def test_a_qq_login(self):
        self.page.reset_package()
        self.page.login()
        self.page.username()
        self.page.passwd()
        self.page.login()
        self.assertTrue(self.page.login_check(self.test_a_qq_login.__name__), 'msg')

if __name__ == '__main__':
    unittest.main()