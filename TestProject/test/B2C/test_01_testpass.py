# coding=utf-8
"""kong接口通过性，1个接口，已完成1个"""

import unittest
from TestProject.common.log import Log
from TestProject.common.data_operation import DataOperation
from TestProject.common.fileReader import IniUtil

evn = IniUtil().get_value_of_option('host_test','b2c')

class testkongpass(unittest.TestCase):
    """获取access_token"""
    @classmethod
    def setUpClass(cls):
        Log().info("""======================获取access_token===================""")
        cls.com = DataOperation('b2c')     #定义cls.com
        #XXX
        cls.com.get_response("getToken")
    @classmethod
    def tearDownClass(cls):
        cls.com.close_session()

    def test_01_testKongPass(self):
        """测试kong通过性"""
        name = "testPass"    #接口名称
        result = self.com.get_result(name)
        self.assertEqual(True,result[0],result[1])

    """    @unittest.skipIf(evn == 'prod','生产环境跳过位置矫正的测试用例')    # 此条用于跳过当前测试用例，有的测试用例在测试环境可以执行，生产环境不能执行，比如下单操作
    #所以这里判断执行环境是prod，那就跳过这个测试用例
    def test_02_testKongPass2(self):
        #测试kong通过性1111
        name = "updateCustLocation"
        result = self.com.get_result(name)
        self.assertEqual(True,result[0],result[1])

    def test_03_testKongPass3(self):    # 测试用例的名称，必须有“test”，要不然不会被识别为测试用例；后面接“_01”,"_02","_03"用来确定测试用例的顺序，如不需顺序可省略；后接"_"后再接接口名称，最好是接口名称
        #测试kong通过性2222
        name = "noLocationCustList"
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])
"""