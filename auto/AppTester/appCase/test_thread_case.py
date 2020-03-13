import unittest
from page.thread_page import Page
import time


class threadDemo(unittest.TestCase):
    def __repr__(self):
        return 'appdemo'

    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    def test_a_thread(self):
        self.page.url()
        time.sleep(2)
        self.page.enter()
        self.assertTrue(self.page.check(self.test_a_thread.__name__), 'msg')
    @classmethod
    def tearDownClass(cls):
        cls.page.quit()
