import pytest
from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.remote.webdriver import WebDriver
from web.po_test_hysweb.pages.MainPage import MainPage
import allure
import logging


@allure.feature("测试web个人页")
class TestProfile(object):
    @classmethod
    def setup_class(cls):
        cls.profilepage = MainPage().goto_profile()

    @classmethod
    def teardown_class(cls):
        cls.profilepage.driver_quit()

    def setup_method(self):
        pass

    def teardown_method(self):
        # self.profilepage.driver_quit()
        pass

    @allure.story("核对个人页订单")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_01_profile_order(self):
        with allure.step("查看个人订单"):
            result = self.profilepage.profile_order()
        with allure.step("断言结果"):
            self.profilepage.screenshots()
            logging.info("核对个人页订单case")
            logging.info("测试result：%s" % result)
            assert result is True

    @allure.story("核对个人信息")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_02_profile_information(self):
        with allure.step("查看个人信息"):
            result = self.profilepage.profile_information()
        with allure.step("断言结果"):
            self.profilepage.screenshots()
            logging.info("核对个人信息case")
            logging.info("测试result：%s" % result)
            assert result is True

    @allure.story("核对地址信息")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_03_profile_address(self):
        with allure.step("查看地址信息"):
            result = self.profilepage.profile_address()
        with allure.step("断言结果"):
            self.profilepage.screenshots()
            logging.info("核对地址信息case")
            logging.info("测试result：%s" % result)
            assert result is True

    @allure.story("核对优惠券信息")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_04_profile_coupons(self):
        with allure.step("查看优惠券信息"):
            result = self.profilepage.profile_coupons()
        with allure.step("断言结果"):
            self.profilepage.screenshots()
            logging.info("核对优惠券信息case")
            logging.info("测试result：%s" % result)
            assert result is False

    @allure.story("核对充值信息")
    @allure.severity('normal')
    @allure.testcase('')
    @allure.issue('')
    def test_05_profile_recharge(self):
        with allure.step("查看充值信息"):
            result = self.profilepage.profile_recharge()
        with allure.step("断言结果"):
            self.profilepage.screenshots()
            logging.info("核对充值信息case")
            logging.info("测试result：%s" % result)
            assert result is True
