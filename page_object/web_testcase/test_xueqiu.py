import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class TestXueqiu(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'https://xueqiu.com/'
        #远程浏览器的调用
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)


    def test_xueqiusearch(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_xpath('//*[@placeholder="搜索"]').send_keys("alibaba")
        driver.find_element_by_xpath('//*[@class="icon iconfont"]').click()
        driver.find_element_by_css_selector('.follow__control .iconfont').click()
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector('[placeholder="请输入手机号或者邮箱"]').send_keys("18888888888")
        driver.find_element_by_css_selector('[placeholder="请输入登录密码"]').send_keys("abc123")
        driver.find_element_by_xpath('//*[@class="modal__login__btn"]').click()

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def test_execute_script(self):          #获取浏览器内部界面所有加载时间
        raw = self.driver.execute_script("JSON.stringify(window.performance.timing)")
        print(raw)
        # json解析一下
        print(json.dumps(json.loads(raw),indent=4))
        sleep(3)

    def test_execute(self):     #  execute 用于新的api的调用（底层支持，库不支持）
        self.driver.execute("getXXX", params={"x": 1, "y": 2})



    def teardown(self):
        sleep(5)
        self.driver.quit()