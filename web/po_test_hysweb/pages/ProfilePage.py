# coding=utf-8
from selenium.webdriver.common.by import By
import logging
from web.po_test_hysweb.pages.BasePage import BasePage
from time import sleep


class ProfilePage(BasePage):        # 该页面测试主要看登录后

    # 核对个人页订单
    def profile_order(self):
        self.find(By.ID, 'lgnByaccount').click()
        sleep(2)
        self.find(By.NAME, 'loginName').send_keys('15001106951')
        self.find(By.NAME, 'loginPwd').send_keys('123456')
        self.find(By.ID, 'submitLogin2').click()
        sleep(2)
        number = self._driver.find_elements(By.XPATH,"//*[@class='list-img']")
        logging.info("核对个人页订单—number：%s" % number)
        if number != []:
            return True
        else:
            return False

    # 核对个人信息
    def profile_information(self):
        self.find(By.CSS_SELECTOR, '.h-info').click()
        sleep(2)
        text = self.find(By.CSS_SELECTOR, '.on').text
        if text == "基本信息":
            return True
        else:
            return False

    # 核对地址信息
    def profile_address(self):
        self.find(By.CSS_SELECTOR, '.h-address').click()
        sleep(2)
        number = self._driver.find_elements(By.XPATH,'//*[@class="addressOpt "]')
        logging.info("核对地址信息的number信息打印：")
        logging.info("===========number:%s=================" % number)
        logging.info("===========type(number):%s=================" % type(number))
        logging.info("===========len(number):%s=================" % len(number))
        if number != []:
            return True
        else:
            return False

    # 核对优惠券信息
    def profile_coupons(self):  # 可用优惠券当前为空
        self.find(By.CSS_SELECTOR, '.h-coupon').click()
        sleep(2)
        number = self._driver.find_elements(By.XPATH, '//*[@id="type_1"]/li')
        if number != []:
            return True
        else:
            return False

    # 核对充值信息
    def profile_recharge(self):
        self.find(By.CSS_SELECTOR, '.h-recharge').click()
        sleep(2)
        text = self.find(By.CSS_SELECTOR, '.btn_recharge').text
        if text == "确认充值":
            return True
        else:
            return False