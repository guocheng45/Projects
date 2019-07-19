import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.page_object.page.MainPage import MainPage


class TestXueqiu(object):

    def setup(self):
        #远程浏览器的调用,（）不写内容默认的就是本地浏览器
        #self.driver = webdriver.Remote()   # webdriver.Remote(desire_capabilities=DesiredCapabilities.CHROME)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main = MainPage(self.driver)

    def test_xueqiusearch(self):
        # driver = self.driver
        # driver.get(self.url)
        # driver.find_element_by_xpath('//*[@placeholder="搜索"]').send_keys("alibaba")
        # driver.find_element_by_xpath('//*[@class="icon iconfont"]').click()
        # driver.find_element_by_css_selector('.follow__control .iconfont').click()
        # driver.implicitly_wait(5)
        # driver.find_element_by_css_selector('[placeholder="请输入手机号或者邮箱"]').send_keys("18888888888")
        # driver.find_element_by_css_selector('[placeholder="请输入登录密码"]').send_keys("abc123")
        # driver.find_element_by_xpath('//*[@class="modal__login__btn"]').click()

        # 牛逼的传值法，跨类传值，啧啧啧啧啧。。。  自己的理解是调用了主page ，searchpage是辅的，用主的里面去调辅的
        self.main.search("alibaba").follow("1688")
        #断言  todo: do assert



    def teardown(self):
        sleep(5)
        self.driver.quit()