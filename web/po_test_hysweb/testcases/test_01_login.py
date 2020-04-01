from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.remote.webdriver import WebDriver
from web.po_test_hysweb.pages.MainPage import MainPage


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        # cls.main = MainPage(cls.driver)         # 对主页面的初始化
        # cls.loginpage = Driver().startmain().gotologin()
        cls.loginpage = MainPage().gotologin()

    @classmethod
    def teardown_class(cls):
        cls.loginpage.driver_quit()


    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_01_login(self):
        self.loginpage.login_by_pwd()
        result = self.loginpage.login_result()
        self.loginpage.screenshots()
        assert "login" in result


    def test_02_logout(self):
        self.loginpage.login_by_pwd()
        self.loginpage.logout()
        self.loginpage.screenshots()
        result = self.loginpage.login_result()
        assert "not login" in result
