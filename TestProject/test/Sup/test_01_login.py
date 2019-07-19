# coding=utf-8
"""登录 共1个接口 已完成1个"""
import unittest
from TestProject.common.data_operation import DataOperation
from ddt import ddt, data
from TestProject.common.log import Log


@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""

    @classmethod
    def setUpClass(cls):
        Log().info("""
        ====================================执行模块【登录】=============================================
        """)
        cls.com = DataOperation('sup')

    @classmethod
    def tearDownClass(cls):
        cls.com.close_session()

    @data(0, 1)
    def test_01_login(self, index):
        """测试登录"""
        name = "login"
        result = self.com.get_result(name, index)
        self.assertEqual(True, result[0], result[1])





