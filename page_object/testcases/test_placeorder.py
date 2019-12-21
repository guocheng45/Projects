from page_object.pages.HysAPP import HysApp
from page_object.pages.HysBase import HysBase
from page_object.pages.HysMainPage import HysMainPage
import pytest

from page_object.pages.HysPage import HysPage


class TestPlaceOrder(object):


    @classmethod
    def setup_class(cls):       # 类执行一下，如启动APP
        cls.mainPage = HysApp.main()                # 可能有问题-没问题
        # cls.hysPage = HysApp.main().gotoHyspage()   # 也可以如此写

    def setup_method(self):     # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.searchPage = self.mainPage.gotoHyspage()     # 如果是搜索页的话就可用这个
        # self.ProfilePage = self.mainPage.gotoProfile()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        # self.SearchPage = self.mainPage.gotoSearchpage()
        self.Hyspage = self.mainPage.gotoHyspage()

    def teardown_method(self):
        # 如返回至初始页可放置在此
        # self.SearchPage.search_back()
        return 1

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

    @pytest.mark.parametrize("phone,pwd,msg",[("15001106951","123456","成功"),("15001106951","abc123","错误")])
    def test_01_login(self,phone,pwd,msg):
        if self.ProfilePage.is_login_app()==0:
            assert str(self.ProfilePage.login_app(phone,pwd).getToastMsg()).__contains__(msg)
        else:
            assert str(self.ProfilePage.logout_app().login_app(phone,pwd).getToastMsg()).__contains__(msg)

    @pytest.mark.parametrize("kw,jr",[("感冒","//*[contains(@text,'感')]"),("发烧","//*[contains(@text,'发')]")])
    def test_02_search(self,kw,jr):
        result = self.SearchPage.search_goodsB2C(kw)
        assert result.judge_Searchresult(jr)>1

    def test_03_placeOrder(self):
        self.Hyspage.cart_goods_isChecked()