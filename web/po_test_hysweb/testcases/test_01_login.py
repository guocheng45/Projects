import pytest
from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.remote.webdriver import WebDriver
from web.po_test_hysweb.pages.MainPage import MainPage
import allure
import logging


@allure.feature("测试web登录")
class TestLogin(object):
    @classmethod
    def setup_class(cls):
        # cls.loginpage = MainPage().goto_login()         # 对页面的初始化
        pass

    @classmethod
    def teardown_class(cls):
        # cls.loginpage.driver_quit()
        pass


    def setup_method(self):
        self.loginpage = MainPage().goto_login()

    def teardown_method(self):
        self.loginpage.driver_quit()

    @allure.story("测试登录功能")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    @pytest.mark.parametrize("name,pwd",[("15001106951","123456"),("13663397421","abc123")])
    def test_01_login(self,name,pwd):
        with allure.step("进行登录"):
            self.loginpage.login_by_pwd(name,pwd)
        with allure.step("获取登录结果"):
            result = self.loginpage.login_result()
        self.loginpage.screenshots()
        logging.info("测试登录功能")
        logging.info("测试result：%s" % result)
        assert "login" in result

    @allure.story("测试登录登出功能")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_02_logout(self):
        with allure.step("进行登录"):
            self.loginpage.login_by_pwd("15001106951","123456")
        with allure.step("然后登出"):
            self.loginpage.logout()
        with allure.step("获取登录结果"):
            result = self.loginpage.login_result()
            self.loginpage.screenshots()
            logging.info("测试登录登出功能")
            logging.info("测试result：%s" % result)
        assert "not login" in result
