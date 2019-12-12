from page_object.pages.HysAPP import HysApp
from page_object.pages.HysMainPage import HysMainPage
import pytest
import logging

from page_object.pages.HysPage import HysPage


class TestPlaceOrder(object):


    @classmethod
    def setup_class(cls):       # 类执行一下，如启动APP
        cls.mainPage = HysApp.main()                # 可能有问题-没问题
        # cls.hysPage = HysApp.main().gotoHyspage()   # 也可以如此写

    def setup_method(self):     # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.searchPage = self.mainPage.gotoHyspage()     # 如果是搜索页的话就可用这个
        self.hysPage = self.mainPage.gotoHyspage()

    def teardown_method(self):
        # 如返回至初始页可放置在此
        # self.searchPage.cancel()
        pass

    @classmethod
    def teardown_class(cls):
        pass
    # 炒个栗子
    # def test_placeorder1(self):
    #     # 如要判断就加上断言
    #     assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
    #     assert "something" in self.mainPage.gotoProfile().getErrorMsg()
        #下一步
        # 再一个assert

    # @pytest.mark.parametrize("phone,pwd",[("15001106951","123456"),("15001106951","abc123")])
    def test_login(self):
        # self.mainPage.gotoHyspage().login_app('15001106951','123456')
        # assert "成功" in self.Hys.getToastMsg()
        assert str(self.hysPage.login_app('15001106951','123456').getToastMsg()).__contains__("成功")