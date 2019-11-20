from page_object.pages.HysAPP import App
from page_object.pages.HysMainPage import HysMainPage


class TestPlaceOrder(object):

    @classmethod
    def setup_class(cls):       # 类执行一下，如启动APP
        cls.mainPage=App.main()

    def setup_mothod(self):     # 设置等于自己的mainPage，可以直接调用？
        self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP

    @classmethod
    def teardown_class(cls):
        pass
    # 炒个栗子
    def test_placeorder1(self):
        # 如要判断就加上断言
        assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()