# coding=utf-8
from po_test_hysapp.pages.HysAPP import HysApp
import pytest
import allure

@allure.feature("测试好药师APP搜索")
class TestPlaceOrder(object):

    @classmethod
    def setup_class(cls):  # 类执行一下，如启动APP
        cls.mainPage = HysApp.main()  # 可能有问题-没问题
        # cls.hysPage = HysApp.main().gotoHyspage()   # 也可以如此写

    def setup_method(self):  # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.ProfilePage = self.mainPage.gotoProfile()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        self.cartspage = self.mainPage.gotoCartspage()

    def teardown_method(self):
        # 如返回至初始页可放置在此
        pass


    @classmethod
    def teardown_class(cls):
        # time.sleep(2)
        # cls.driver.quit()
        pass

    # 炒个栗子
    # def test_placeorder1(self):
    #     # 如要判断就加上断言
    #     assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
    #     assert "something" in self.mainPage.gotoProfile().getErrorMsg()
    # 下一步
    # 再一个assert

    @allure.story("测试车中有无商品")
    @allure.severity('normal')
    @allure.testcase("")
    @allure.issue("")
    def test_01_is_empty(self):
        with allure.step(""):
            result = self.cartspage.carts_is_empty()
            self.cartspage.screenshots()
        assert result is True

    @allure.story("测试选中商品")
    @allure.severity('normal')
    @allure.testcase("")
    @allure.issue("")
    def test_02_select_goods(self):
        with allure.step("选中下单商品"):
            self.cartspage.select_goods('一力')

    @allure.story("测试编辑商品数量")
    @allure.severity('blocker')
    @allure.testcase("")
    @allure.issue("")
    @pytest.mark.parametrize("str1,str2",[("一力",1),("好医生",1)])
    def test_03_change_quantity(self,str1,str2):
        with allure.step("修改商品的数量"):
            self.cartspage.change_quantity(name=str1,number=str2)
            self.cartspage.screenshots()

    @allure.story("测试移除商品")
    @allure.severity('blocker')
    @allure.testcase("")
    @allure.issue("")
    def test_04_remove_item(self):
        self.cartspage.screenshots()
        with allure.step("移除某个商品"):
            self.cartspage.remove_item('力生')
            self.cartspage.screenshots()

    @allure.story("测试商品下单")
    @allure.severity('blocker')
    @allure.testcase("")
    @allure.issue("")
    def test_05_place_order(self):
        with allure.step("选中商品下单"):
            result = self.cartspage.place_order()
            self.cartspage.screenshots()
        with allure.step("返回到购物车"):
            self.cartspage.back()
            self.cartspage.screenshots()
        assert result is True