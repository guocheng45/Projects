from selenium.webdriver.common.by import By
from web.po_test_hysweb.pages.BasePage import BasePage
from time import sleep

class LoginPage(BasePage):

    def login_by_pwd(self):
        self.find(By.ID,'lgnByaccount').click()
        self.find(By.NAME,'loginName').send_keys('15001106951')
        self.find(By.NAME,'loginPwd').send_keys('123456')
        self.find(By.ID,'submitLogin2').click()
        return self

    def logout(self):
        sleep(3)
        self.find(By.ID,'exit_top_btn').click()
        return self

    def login_result(self):     # 前提需跳转至首页
        # print(self.driver.get_cookies())
        sleep(4)
        text = self.find(By.XPATH, '//*[@class="login_name_top"]/i').text
        # print("===========text:",text,"=================")
        # print("===========len(text):", len(text), "=================")
        if len(text) >0:
            return "login"
        else:
            return "not login"