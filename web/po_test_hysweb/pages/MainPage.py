from selenium.webdriver.common.by import By

from web.po_test_hysweb.pages.BasePage import BasePage
from web.po_test_hysweb.pages.LoginPage import LoginPage


class MainPage(BasePage):
    def gotologin(self):
        current_handle = self._driver.current_window_handle  # current ：当前
        self.find(By.CSS_SELECTOR,'.n-name').click()
        all_handle = self._driver.window_handles     # 获取所有的句柄
        for handle in all_handle:
            if handle != current_handle:
                self._driver.switch_to.window(handle)
        return LoginPage(self._driver)

    def gotoProfile(self):
        pass

    def gotoPlaceorder(self):
        pass