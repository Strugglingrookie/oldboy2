import unittest


class TestPay(unittest.TestCase):
    def test_buy(self):
        self.assertEqual(1, 1, msg='成功')

    def test_buy2(self):
        self.assertEqual(1, 2, '失败')