from selenium import webdriver
import unittest
import time
import pytest

class TestLogin(object):
    """官网PC端登录功能测试"""

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'http://www.ehaoyao.com'

    def test_login1(self):
        """页面登录测试"""
        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(1)
        time.sleep(1)
        current_handle = driver.current_window_handle
        driver.find_element_by_xpath('//div[1]/div/ul[1]/li[3]/span[1]').click()
        all_handle = driver.window_handles
        driver.close()
        for handle in all_handle:
            if handle != current_handle:
                driver.switch_to.window(handle)
                time.sleep(2)
                driver.find_element_by_id('lgnByaccount').click()
                driver.find_element_by_id('loginName').send_keys('13663397421')
                driver.find_element_by_id('loginPwd').send_keys('abc123')
                driver.find_element_by_id('submitLogin2').click()
                time.sleep(2)
                self.result = driver.find_element_by_id('exit_top_btn').text
                time.sleep(3)
                assert self.result == '退出'
                #self.assertEqual(self.result,'退出', msg='登录不成功！')


    def test_login2(self):
        """弹窗登录测试"""

        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(1)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@class='fr font_mid']/li[3]").click()  # 点击个人中心
        time.sleep(1)
        driver.find_element_by_id('lgnByaccount').click()
        driver.find_element_by_id('loginName').send_keys('13663397421')
        driver.find_element_by_id('loginPwd').send_keys('abc123')
        driver.find_element_by_id('submitLogin2').click()
        driver.implicitly_wait(8)
        result = driver.find_element_by_id('exit_top_btn').text
        print(result)
        #self.assertEqual(result, '退出', msg='登录不成功！')

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
