# coding=utf-8
"""购物车 共9个接口，已完成9个"""

import unittest
from TestProject.common.data_operation import DataOperation
from ddt import ddt, data
from TestProject.common.common_methods import  CommonMethod
from time import sleep
from TestProject.common.log import Log
from TestProject.common.fileReader import IniUtil


# add_to_cart = [False, False, False, False, False, False, False, False, False]
# cart_detail = [False,False,False]
# cart_submit = False
# order_generate = False

evn = IniUtil().get_value_of_option('Env','env')


@unittest.skipIf(evn == 'prod', '生产环境跳过加购物车下单的测试用例')
@ddt
class TestCart(unittest.TestCase):
    """测试购物车"""

    @classmethod
    def setUpClass(cls):
        Log().info("""
        ====================================执行模块【购物车】=============================================
        """)
        cls.com = DataOperation('sup')
        # 登录
        cls.com.get_response("login")

    @classmethod
    def tearDownClass(cls):
        cls.com.close_session()

    @data(*list(range(9)))
    def test_01_addToCart(self, index):
        """测试加购物车，3个客户同时加3个商品，此测试用例是后续测试用例的前提"""
        name = "checkNewCart"
        result = self.com.get_result(name, index)
        self.assertEqual(True, result[0], result[1])
        # global add_to_cart
        # add_to_cart[index] = True

    def test_02_salesManCartList(self):
        """测试获取购物车客户列表"""
        name = "salesManCartList"
        # global add_to_cart
        # print(add_to_cart)
        # if all(add_to_cart) is False:
        #     unittest.TestCase.skipTest(self, "加购物车的测试用例，即test_01_addToCart运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])

    @data(*list(range(3)))
    def test_03_custCartDetail(self, index):
        """测试获取购物车商品明细"""
        name = "custCartDetail"
        # global add_to_cart
        # if all(add_to_cart) is False:
        #     unittest.TestCase.skipTest(self, "加购物车的测试用例，即test_01_addToCart运行失败，故跳过此测试用例")
        result = self.com.get_result(name, index)
        self.assertEqual(True, result[0], result[1])
        # global cart_detail
        # cart_detail[index] = True



    def test_04_getCartStatus(self):
        """测试查询购物车状态"""
        name = "getCartStatus"
        # global cart_detail
        # if all(cart_detail) is False:
        #     unittest.TestCase.skipTest(self, "获取购物车商品明细的测试用例，即test_03_custCartDetail未运行或运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])


    def test_05_batchDeleteCart(self):
        """测试删除购物车列表中某个客户购物车，删除3个客户中第一个客户的购物车"""
        name = "batchDeleteCart"
        # global add_to_cart
        # if all(add_to_cart) is False:
        #     unittest.TestCase.skipTest(self, "加购物车的测试用例，即test_01_addToCart运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])
        # # =======检查购物车中该客户的商品数量应该为0===============
        # # 获取购物车该客户的商品数量
        rs = self.com.get_response('custCartDetail')
        # 检查返回结果中cartAmount是否为0
        cart_amount = CommonMethod().jsonpath_parse(rs[0], "$..cartAmount")
        self.assertEqual(0, cart_amount[0], '该客户购物车数量不为0')

    def test_06_MobileNextCart(self):
        """测试提交订单进入配送确认, 提交三个客户中第二个客户的所有商品"""
        name = "MobileNextCart"
        # global cart_detail
        # if all(cart_detail) is False:
        #     unittest.TestCase.skipTest(self, "获取购物车商品明细的测试用例，即test_03_custCartDetail未运行或运行失败，故跳过此测试用例")
        cm = CommonMethod()
        # 先检查该客户购物车的状态，是否全部校验通过
        rs = self.com.get_response('getCartStatus')
        status = cm.jsonpath_parse(rs[0], "$..erpCheckStatus")
        # status = [1,1,0]
        if all(status) is False:
            # 若不是全部通过，则等待15秒
            sleep(15)
            # 再次检查status
            rs = self.com.get_response('getCartStatus')
            status = cm.jsonpath_parse(rs[0], "$..erpCheckStatus")
            # status = [0,1,0]
            # print(status)
            if all(status):
                # 如果全部通过
                result = self.com.get_result(name)
                self.assertEqual(True, result[0], result[1])
            elif all(status) is False and any(status):
                # 如果有部分商品通过了校验
                # 获取response
                response = self.com.get_response(name)
                # 因只有部分商品通过校验，故不检查具体的数量
                # 1. 检查code
                code = cm.jsonpath_parse(response[0], "$.code")
                self.assertEqual(1, code[0], 'code的实际结果‘%s’不等于期望结果:‘1’' % code)
                # 2. 检查success
                success = cm.jsonpath_parse(response[0], "$.data.success")
                self.assertEqual(True, success[0], 'success的实际结果‘%s’不等于期望结果:‘True’' % success)
                # 3. 检查data.count的值大于0
                count = cm.jsonpath_parse(response[0], "$.data.count")
                self.assertGreater(count[0], 0, 'count的实际结果‘%s’不大于0’' % count)
            else:
                # 无任何商品通过校验，跳过此测试用例
                unittest.TestCase.skipTest(self, "三个测试商品均未通过购物车校验，故跳过此测试用例")
        else:
            result = self.com.get_result(name)
            self.assertEqual(True, result[0], result[1])
        # global cart_submit
        # cart_submit = True

    def test_07_mobileLastCart(self):
        """测试生成订单, 提交三个客户中第二个客户的所有商品"""
        name = "mobileLastCart"
        # global cart_submit
        # if cart_submit is False:
        #     unittest.TestCase.skipTest(self, "提交订单进入配送确认的测试用例，即test_06_MobileNextCart未运行或运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])
        global order_generate
        order_generate = True

    def test_08_getOrderStatus(self):
        """测试订单状态"""
        name = "getOrderStatus"
        # global order_generate
        # if order_generate is False:
        #     unittest.TestCase.skipTest(self, "生成订单的测试用例，即test_07_mobileLastCart未运行或运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])

    def test_09_buyAgain(self):
        """测试再次购买，第二个客户再次购买"""
        name = "buyAgain"
        # global order_generate
        # if order_generate is False:
        #     unittest.TestCase.skipTest(self, "生成订单的测试用例，即test_07_mobileLastCart未运行或运行失败，故跳过此测试用例")
        result = self.com.get_result(name)
        self.assertEqual(True, result[0], result[1])



















