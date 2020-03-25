from selenium.webdriver.common.by import By
import time
import logging
from po_test_hysapp.pages.HysBase import HysBase
import allure
import os


class SearchPage(HysBase):
    """
        # 该page的方法返回的结果是一个值类用于testcase断言使用
        self.driver.find_element_by_xpath("XXXX")
        对页面的每一步操作都用一个方法封装
        也可以对一个操作功能进行封装
        为了引用该类的时候调用到类里面的变量，可以给变量加_不会被看到
    """

    def search_goodsB2C(self, kw):
        self.loadSteps("data/hys.yaml", "search_goodsB2C", keys=kw)
        return self

    def search_goodsO2O(self, kw):
        self.loadSteps("data/hys.yaml", "search_goodsO2O", keys=kw)
        return self

    def search_by_record(self):
        eles = self.driver.find_elements(By.ID,"tv_tag")
        eles[0].click()
        return self

    def judge_Searchresult(self):
        # judge_result = self.driver.find_elements(By.XPATH, jr)
        judge_result = self.driver.find_elements(By.ID, "iv_buy")
        logging.info("=================type(judge_result: %s", type(judge_result))
        logging.info("=================judge_result: %s", judge_result)
        self.screenshots()
        if judge_result != []:
            return True
        else:
            return False

    def search_back(self):
        self.find(By.ID, "iv_back").click()
        return self

    def addto_Carts(self):
        amount1 = self.find(By.XPATH,"//*[contains(@resource-id,'iv_cart')]/../android.widget.TextView").text
        # 找到第一个商品加购
        eles = self.driver.find_elements(By.ID,"iv_buy")
        eles[0].click()
        amount2 = self.find(By.XPATH, "//*[contains(@resource-id,'iv_cart')]/../android.widget.TextView").text
        # 目前判断不了是否加到购物车
        self.screenshots()
        if amount2 >=amount1:
            return True
        else:
            return False