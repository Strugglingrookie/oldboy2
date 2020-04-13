from page.thread_page import Page
import unittest


class Zbox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_a_login(self):
        self.page.url()
        self.page.username()
        self.page.password()
        self.page.keep_login()
        self.page.login_button()
        self.assertTrue(self.page.login_check(self.test_a_login.__name__), 'msg')

    def test_b_create_bug(self):
        self.page.tag_bug()
        self.page.create_bug()
        self.page.module()
        self.page.system()
        self.page.browser()
        self.page.build()
        self.page.assign()
        self.page.end_date()
        self.page.bug_title()
        self.page.steps()
        self.page.save()
        self.assertTrue(self.page.create_bug_check(self.test_b_create_bug.__name__), 'msg')


if __name__ == '__main__':
    unittest.main()
