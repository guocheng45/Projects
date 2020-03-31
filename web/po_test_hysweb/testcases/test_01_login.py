from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.remote.webdriver import WebDriver
from web.po_test_hysweb.pages.MainPage import MainPage


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        # cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.ehaoyao.com")
        cls.driver.maximize_window()
        cls.main = MainPage(cls.driver)         # 对主页面的初始化

    @classmethod
    def teardown_class(cls):
        cls.main.driver_quit()


    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_01_login(self):
        self.main.gotologin().login_by_pwd()
        # assert 1==1

    def test_02_logout(self):
        pass