from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.po_test_hysweb.pages.MainPage import MainPage


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.ehaoyao.com")
        cls.main = MainPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_01_login(self):
        self.main.gotologin().login_by_pwd()
        assert 1==1

    def test_02_logout(self):
        pass