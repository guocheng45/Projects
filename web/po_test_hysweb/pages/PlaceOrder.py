# coding=utf-8
from selenium.webdriver.common.by import By

from web.po_test_hysweb.pages.BasePage import BasePage
from time import sleep


class PlaceOrder(BasePage):

    # 搜索商品
    def login_by_pwd(self):
        # self.find(By.NAME, 'loginName').send_keys('15001106951')
        # self.find(By.NAME, 'loginPwd').send_keys('123456')
        # self.find(By.ID, 'submitLogin2').click()
        self.find(By.ID,"top_search_input").send_keys('感冒')
        self.find(By.CSS_SELECTOR,'.btn').click()
        self._driver.find_elements(By.XPATH,'//*[@class="btn_car"]')[0].click()
        current_handle = self._driver.current_window_handle
        self.find(By.CSS_SELECTOR,'.go_pay').click()
        all_handle = self._driver.window_handles
        for handle in all_handle:
            if handle != current_handle:
                self._driver.switch_to.window(handle)

        self.find(By.CSS_SELECTOR,'.loginTip .btn').click()
        self.find(By.ID,'lgnByaccount').click()
        self.find(By.ID, 'loginName').send_keys('15001106951')
        self.find(By.ID, 'loginPwd').send_keys('123456')
        self.find(By.ID,'submitLogin2').click()



        return self

    # 加购物车
    def logout(self):
        self.find(By.CSS_SELECTOR, '.h-info').click()
        sleep(2)
        text = self.find(By.CSS_SELECTOR, '.on').text
        if text == "基本信息":
            return True
        else:
            return False

    # 购物车中选中商品
    def profile(self):
        pass

    # 然后下单，判断下单是否成功
    def xxx(self):
        pass

    # 取消订单
    def xxx(self):
        pass