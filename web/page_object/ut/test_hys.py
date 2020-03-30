from selenium import webdriver
import time

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
                # driver.find_element_by_id('lgnByaccount').click()
                driver.find_element_by_id('loginName').send_keys('15001106951')
                driver.find_element_by_id('loginPwd').send_keys('123456')
                driver.find_element_by_id('submitLogin2').click()
                time.sleep(2)
                result = driver.find_element_by_id('exit_top_btn').text
                print("=============self.result:",result)
                assert result == '退出'
                #self.assertEqual(self.result,'退出', msg='登录不成功！')


    def test_login2(self):
        """弹窗登录测试"""

        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(1)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@class='fr font_mid']/li[3]").click()  # 点击个人中心
        time.sleep(1)
        driver.find_element_by_id('loginName').send_keys('15001106951')
        driver.find_element_by_id('loginPwd').send_keys('123456')
        driver.find_element_by_id('submitLogin2').click()
        time.sleep(2)
        result = driver.find_element_by_id('exit_top_btn').text         # 一些控件的操作需要等待时间
        print("==============result: ",result)
        #self.assertEqual(result, '退出', msg='登录不成功！')

    def teardown(self):
        time.sleep(4)
        self.driver.quit()

