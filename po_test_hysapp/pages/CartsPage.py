from selenium.webdriver.common.by import By
import time
import logging
from po_test_hysapp.pages.HysBase import HysBase
import allure
import os


class CartsPage(HysBase):
    """
        # 该page的方法返回的结果是一个值类用于testcase断言使用
        self.driver.find_element_by_xpath("XXXX")
        对页面的每一步操作都用一个方法封装
        也可以对一个操作功能进行封装
        为了引用该类的时候调用到类里面的变量，可以给变量加_不会被看到
    """

    # 判断车中是否有商品
    def carts_is_empty(self):
        goods = self.driver.find_elements(By.ID, "iv_goods_img")
        if goods != []:
            return True
        else:
            return False

    # 选中车中某品
    def select_goods(self, name='一力'):
        general_check = self.find(By.ID, "rb_pharmacy_check")
        check_status = general_check.get_attribute("checked")
        if check_status == 'true':
            general_check.click()
        # "//*[contains(@text,'仁和可立克')]/../..//*[contains(@resource-id,'rb_check')]"
        goods_checkbt = self.find(By.XPATH,
                                  "//*[contains(@text,'%s')]" % name + "/../..//*[contains(@resource-id,'rb_check')]")
        checked = goods_checkbt.click()
        self.screenshots()
        return self

    # 加减某品的数量为多少
    def change_quantity(self, name='一力'):
        goods_quantity = self.find(By.XPATH,
                                   "//*[contains(@text,'%s')]" % name + "/../..//*[contains(@resource-id,'tv_number')]").click()
        clear_quantity = self.find(By.ID,'et_dialog_number').clear()
        set_quantity = self.find(By.ID,'et_dialog_number').send_keys('1')
        self.find(By.ID,'bt_dialog_sure').click()
        return self

    # 编辑移除商品
    def remove_item(self):
        self.find(By.ID,'tv_edit_all').click()


    def back(self):
        self.find(By.ID, "iv_back").click()
        return self

    # 下单结算
    def place_order(self):
        pel5 = self.find(By.ID, "tv_next").click()
        pel6 = self.find(By.ID, "tv_submit_order").click()
        return self

    # def __place_order_B2CCart(self, kw):        # B2C搜索商品加到购物车下单
    #     self.search_goodsB2C(kw)
    #     self.swipe_ui("上拉")
    #     pel1 = self.find(By.XPATH,
    #                      "//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
    #     pel2 = self.find(By.ID, "iv_cart").click()
    #     # 此处需判断购物车中的这个商品是否是选中状态？？？？
    #     pel5 = self.find(By.ID, "tv_next").click()
    #     pel6 = self.find(By.ID, "tv_submit_order").click()

    # def place_order_B2CSale(self):            # O2O搜索商品加到购物车下单
    #     po1 = self.find(By.ID, "ac_title").click()
    #     # po1 = self.find(By.XPATH,"//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
    #     # 多点两次页签2，怕点不中
    #     po2 = self.find(By.ID, "tv_flash_sale_status").click()
    #     po2_1 = self.find(By.ID, "tv_flash_sale_status").click()
    #     # 等待页面跳转
    #     time.sleep(3)
    #     po3 = self.find(By.ID, "tv_name").click()
    #     po4 = self.find(By.ID, "tv_bottom_buy_now").click()
    #     po5 = self.find(By.ID, "tv_buy_now").click()
    #     po6 = self.find(By.ID, "tv_submit_order").click()
    #     po7 = self.find(By.ID, "iv_base_left").click()

    # def place_order_O2OCart(self):
    #     self.search_goodsO2O()
    #     po1 = self.find(By.XPATH, "//*[contains(@text,'东信 对乙酰氨基酚栓')]/../..//*[contains(@resource-id,'iv_buy')]").click()
    #     po2 = self.find(By.ID, "iv_cart").click()
    #     time.sleep(3)
    #     po3 = self.find(By.ID, "tv_next").click()
    #     po4 = self.find(By.ID, "tv_submit_order").click()
    #     po6 = self.find(By.ID, "iv_back").click()
