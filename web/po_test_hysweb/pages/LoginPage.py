from web.po_test_hysweb.pages.BasePage import BasePage


class LoginPage(BasePage):

    def login_by_pwd(self):
        self.driver.find_element_by_name('loginName').send_keys('15001106951')
        self.driver.find_element_by_name('loginPwd').send_keys('123456')
        self.driver.find_element_by_id('submitLogin2').click()
        return self