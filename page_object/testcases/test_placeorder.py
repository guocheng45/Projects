from page_object.pages.HysAPP import HysApp
from page_object.pages.HysMainPage import HysMainPage
import pytest
import logging


class TestPlaceOrder(object):


    @classmethod
    def setup_class(cls):       # 类执行一下，如启动APP
        cls.mainPage=HysApp.main()


    def setup_mothod(self):     # 设置等于自己的mainPage，可以直接调用？
        self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP
        # self.searchPage = self.mainPage.gotoHyspage()     # 如果是搜索页的话就可用这个

    def teardown_mothod(self):
        # 如返回至首页可放置在此
        # self.searchPage.cancel()
        pass

    @classmethod
    def teardown_class(cls):
        pass
    # 炒个栗子
    def test_placeorder1(self):
        # 如要判断就加上断言
        assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
        assert "something" in self.mainPage.gotoProfile().getErrorMsg()
        #下一步
        # 再一个assert

    # @pytest.mark.parametrize("phone,pwd",[("15001106951","123456"),("15001106951","abc123")])
    def test_login(self):
        self.mainPage.gotoHyspage().login_app(15001106951,123456)
        assert "成功" in self.mainPage.gotoHyspage().getToastMsg()