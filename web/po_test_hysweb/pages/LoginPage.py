from selenium.webdriver.common.by import By

from web.po_test_hysweb.pages.BasePage import BasePage
from time import sleep

class LoginPage(BasePage):

    def login_by_pwd(self):
        # self.driver.find_element_by_name('loginName').send_keys('15001106951')
        # self.driver.find_element_by_name('loginPwd').send_keys('123456')
        # self.driver.find_element_by_id('submitLogin2').click()
        self.driver.find_element(By.NAME,'loginName').send_keys('15001106951')
        self.driver.find_element(By.NAME,'loginPwd').send_keys('123456')
        self.driver.find_element(By.ID,'submitLogin2').click()
        return self

    def logout(self):
        self.driver.find_element_by_id('exit_top_btn').click()
        sleep(3)
        return self