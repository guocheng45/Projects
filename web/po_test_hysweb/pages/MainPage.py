from selenium.webdriver.common.by import By
from web.po_test_hysweb.pages.BasePage import BasePage
from web.po_test_hysweb.pages.LoginPage import LoginPage
from web.po_test_hysweb.pages.PlaceOrder import PlaceOrder
from web.po_test_hysweb.pages.ProfilePage import ProfilePage


class MainPage(BasePage):
    def goto_login(self):
        current_handle = self._driver.current_window_handle  # current ：当前
        self.find(By.CSS_SELECTOR, '.n-name').click()
        all_handle = self._driver.window_handles  # 获取所有的句柄
        for handle in all_handle:
            if handle != current_handle:
                self._driver.switch_to.window(handle)
        return LoginPage(self._driver)

    def goto_profile(self):
        current_handle = self._driver.current_window_handle  # current ：当前
        self.find(By.CSS_SELECTOR,'.pCenter').click()
        all_handle = self._driver.window_handles  # 获取所有的句柄
        for handle in all_handle:
            if handle != current_handle:
                self._driver.switch_to.window(handle)
        return ProfilePage(self._driver)

    def goto_place_order(self):
        return PlaceOrder(self._driver)
