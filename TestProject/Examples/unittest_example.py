import unittest


class TestUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """所有test运行前运行一次"""
        pass

    @classmethod
    def tearDownClass(cls):
        """所有test运行完后运行一次"""
        pass

    def setUp(self):
        """每个测试用例运行之前执行一次"""
        pass

    def tearDown(self):
        """每个测试用例运行完之后执行一次"""
        pass

    def test_add(self):
        pass

    def test_plus(self):
        pass

