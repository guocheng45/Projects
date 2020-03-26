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

    # 选中商品
    def select_goods(self, name='一力'):
        general_check = self.find(By.ID, "rb_pharmacy_check")
        check_status = general_check.get_attribute("checked")
        if check_status == 'true':
            general_check.click()
        goods_checkbt = self.find(By.XPATH,
                                  "//*[contains(@text,'%s')]" % name + "/../..//*[contains(@resource-id,'rb_check')]").click()
        self.screenshots()
        return self

    # 修改商品数量为number
    def change_quantity(self, name='一力',number=1):
        goods_quantity = self.find(By.XPATH,
                                   "//*[contains(@text,'%s')]" % name + "/../..//*[contains(@resource-id,'tv_number')]").click()
        # clear_quantity = self.find(By.ID,'et_dialog_number').clear()
        # set_quantity = self.find(By.ID,'et_dialog_number').send_keys('1')
        # self.find(By.ID,'bt_dialog_sure').click()
        self.loadSteps('data/carts.yaml','change_quantity',quant=number)
        return self

    # 编辑移除商品
    def remove_item(self,name='力生'):
        self.find(By.ID,'tv_edit_all').click()
        self.find(By.XPATH,"//*[contains(@text,'%s')]" % name + "/../..//*[contains(@resource-id,'rb_check')]").click()
        # self.find(By.ID,"tv_delete").click()
        # self.find(By.ID,"tv_sure").click()
        self.loadSteps('data/carts.yaml','remove_item')
        return self

    def back(self):         # 收银台->购物车
        # self.find(By.ID, "iv_base_left").click()  # 收银台返回
        # self.find(By.ID, "tv_sure").click()  # 弹窗确定按钮
        # self.find(By.ID, "iv_base_left").click()  # 订单详情返回按钮——>回到购物车
        self.loadSteps('data/carts.yaml','back')
        return self

    # 下单结算，首先需要选中商品
    def place_order(self):
        self.find(By.ID, "tv_next").click()
        order_price1 = str(self.find(By.ID,"tv_total_to_pay").text)
        self.find(By.ID, "tv_submit_order").click()
        order_price2 = str(self.find(By.ID, "order_price").text)
        if order_price1 == order_price2:
            return True
        else:
            return False


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
