import unittest

def calc(a,b):
    return a+b

class CalcTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('这里是setUp')
    def tearDown(self):
        print('这里是tearDown')

    def test_zhengchang(self):
        print('test_zhengchang')

    def test_buzhengchang(self):
        print('test_buzhengchang')
        # result = calc(0,0)
        # self.assertEqual(1,result,'预期结果应该是1')
    def test_calc(self):
        print('test_calc')
    def test_a(self):
        print('aaa')

unittest.main()