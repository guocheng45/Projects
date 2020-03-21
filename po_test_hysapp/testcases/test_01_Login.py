from po_test_hysapp.pages.HysAPP import HysApp
import pytest
import allure
import logging


@allure.feature("测试APP登录页")
class TestProfile(object):

    @classmethod
    def setup_class(cls):  # 类执行一下，如启动APP
        # cls.mainPage = HysApp.main()  # 可能有问题-没问题
        cls.profile = HysApp.main().gotoProfile()   # 也可以如此写

    def setup_method(self):
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.ProfilePage = self.mainPage.gotoProfile()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        # self.loginpage = self.profile.gotoLogin()
        pass

    def teardown_method(self):
        # 如返回至初始页可放置在此
        # self.loginpage.back_profile()
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


    @allure.story("测试登录功能")
    @allure.severity('normal')
    @allure.testcase("http://www.testlink.com/id=001")
    @allure.issue("http://www.jira.com/id=001")
    @pytest.mark.parametrize("phone,pwd,msg", [("15001106951", "123456", "logged"), ("15001106951", "abc123", "not logged")])
    def test_01_login(self, phone, pwd, msg):
        with allure.step("是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，直接进行登录"):
                self.profile.gotoLogin().login_app(phone, pwd)
        else:
            with allure.step("已登录，先退出登录"):
                self.profile.logout_app()
            with allure.step("进行登录"):
                self.profile.gotoLogin().login_app(phone, pwd)
        self.profile.screenshots()
        result = self.profile.is_login_app()
        logging.info("========result:  %s" % result)
        if result == "not logged":
            back = self.profile.back_profile()
        assert msg in result
