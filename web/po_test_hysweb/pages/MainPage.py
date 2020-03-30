from web.po_test_hysweb.pages.BasePage import BasePage
from web.po_test_hysweb.pages.LoginPage import LoginPage


class MainPage(BasePage):
    def gotologin(self):
        self.driver.find_element_by_css_selector('.n-name').click()
        return LoginPage()