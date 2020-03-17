from selenium.webdriver.common.by import By
import time
from datetime import datetime
import logging
from page_object.pages.HysBase import HysBase
import allure
import os


class HysPage(HysBase):
    """
        # 该page的方法返回的结果是一个值类用于testcase断言使用
        self.driver.find_element_by_xpath("XXXX")
        对页面的每一步操作都用一个方法封装
        也可以对一个操作功能进行封装
        为了引用该类的时候调用到类里面的变量，可以给变量加_不会被看到
    """
    def getErrorMsg(self):
        msg = self.find("self._error_msg").text
        self.findByText("确定").click()
        return msg

    def login_app(self, var1, var2):
        self.loadSteps("data/hys.yaml", "login_app", phone=var1, pwd=var2)
        return self  # 返回self是为了链式调用，也就是说可以方法连着调方法  ：func1().func2().func3()

    def is_login_app(self):  # tv_nick_name 判断该控件是否存在即可
        element = self._driver.find_elements(By.ID, "tv_nick_name")  # 只有elements的找不到元素才是为[] 其他报错
        # if element.__sizeof__()>0:      # 判断昵称元素是否存在，大于0就是存在已登录，否则就是未登录
        if element != []:  # 判断昵称元素是否存在，大于0就是存在已登录，否则就是未登录
            return 1  # 已登录
        else:
            return 0  # 未登录

    def logout_app(self):
        time.sleep(2)
        self.loadSteps("data/hys.yaml", "logout_app")
        return self

    def search_goodsB2C(self, kw):

        # import os
        # print('当前所在位置：====================', os.getcwd())
        self.loadSteps("data/hys.yaml", "search_goodsB2C", keys=kw)
        return self

    def judge_Searchresult(self, jr):
        # judge_result = self._driver.find_elements(By.XPATH, jr)
        judge_result = self._driver.find_elements(By.ID, "iv_buy")
        logging.info("=================type(judge_result: %s", type(judge_result))
        pic = self.screenshots()
        file = open(pic,'rb').read()         # 先把文件open 然后再read读取一下，然后即可把这个文件加到allure中
        allure.attach.file(pic, attachment_type=allure.attachment_type.PNG)       # attach图片上步已经可以读取，直接写上名字就可以了
        os.remove(pic)
        return len(judge_result)

    def search_back(self):
        self.find(By.ID, "iv_back").click()
        return self

    def search_goodsO2O(self, kw):
        # sel1=self.driver.find_element_by_id("function_img").click()
        # sel2=self.driver.find_element_by_id("et_search").click()
        # sel3=self.driver.find_element_by_id("et_search").send_keys('感冒')
        # sel4=self.driver.find_element_by_id("bt_search").click()
        # sel5=self.driver.find_element_by_id("tv_desc").click()
        # sel6=self.driver.find_element_by_id("tv_desc_2").click()
        self.loadSteps("data/hys.yaml", "search_goodsO2O", keys=kw)
        return self

    def back_mainPage(self,curpage):
        # todo:完成从各个页面返回到mainpage
        return True

    def swipe_ui(self, act):
        time.sleep(3)
        # Swipe（int start x, int start y, int end x, int y, duration)
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        if act == "下拉":
            self._driver.swipe(int(x * 0.5), int(y * 0.2), int(x * 0.5), int(y * 0.5), 1000)
        elif act == "上拉":
            self._driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.5), 1000)
        elif act == "左滑":
            self._driver.swipe(int(x * 0.2), int(y * 0.5), int(x * 0.5), int(y * 0.5), 1000)
        else:  # 右滑或者返回
            self._driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.2), int(y * 0.5), 1000)
        time.sleep(3)

    def common_backtomainpage(self):
        # 下单不支付
        cb1 = self.find(By.ID, "iv_base_left").click()
        cb2 = self.find(By.ID, "tv_sure").click()
        # 返回到首页
        cb3 = self.find(By.ID, "iv_base_left").click()
        cb4 = self.find(By.ID, "iv_back").click()
        cb5 = self.find(By.ID, "iv_back").click()

    def cart_goods_isChecked(self,name):
        open_cart = self.find(By.ID, "radio_cart").click()
        open_cart = self.find(By.ID, "radio_cart").click()
        # "//*[contains(@text,'仁和可立克')]/../..//*[contains(@resource-id,'rb_check')]"
        pel1 = self.find(By.XPATH,
                         "//*[contains(@text,'%s')]" %name+"/../..//*[contains(@resource-id,'rb_check')]")
        is_checked = pel1.get_attribute("checked")
        logging.info("is_checked===========: %s", is_checked)
        # screenshot = self.driver.get_screenshot_as_png('D:\Projects\page_object\ut\%s.png' % (datetime.now().strftime("%Y%m%d%H%M%S")))
        # SendMail.sendMail(msg=0,pic=screenshot,receiver=1)
        return is_checked

    def addto_B2CCart(self):
        # 找到第一个商品加购
        eles = self._driver.find_elements(By.ID,"iv_buy")
        eles[0].click()
        # 返回首页
        self.find(By.ID,"iv_cart").click()
        # 需判断购物车该品是否选中
        return self

    def place_order_B2CCart(self):
         pel5 = self.find(By.ID, "tv_next").click()
         pel6 = self.find(By.ID, "tv_submit_order").click()

    def __place_order_B2CCart(self, kw):
        self.search_goodsB2C(kw)
        self.swipe_ui("上拉")
        pel1 = self.find(By.XPATH,
                         "//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        pel2 = self.find(By.ID, "iv_cart").click()
        # 此处需判断购物车中的这个商品是否是选中状态？？？？
        pel5 = self.find(By.ID, "tv_next").click()
        pel6 = self.find(By.ID, "tv_submit_order").click()
        # 余额支付，不要支付了，不好退
        # pel7=self.find(By.ID,"cb_use_balance").click()
        # pel8=self.find(By.ID,"btn_add_addresss").click()
        # self.driver.implicitly_wait(10)
        # pel9=self.find(By.ID,"tv_sure").click()
        # self.driver.implicitly_wait(10)
        # pel10=self.find(By.ID,"tv_order_detail").click()
        self.common_backtomainpage()

    def place_order_B2CBuyNow(self):
        self.search_goodsB2C()
        self.swipe_ui("上拉")
        po1 = self.find(By.XPATH, "//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]").click()
        time.sleep(3)
        po3 = self.find(By.ID, "tv_bottom_buy_now").click()
        po4 = self.find(By.ID, "tv_buy_now").click()
        po5 = self.find(By.ID, "tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.find(By.ID, "iv_back").click()

    def place_order_B2CSale(self):
        po1 = self.find(By.ID, "ac_title").click()
        # po1 = self.find(By.XPATH,"//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        # 多点两次页签2，怕点不中
        po2 = self.find(By.ID, "tv_flash_sale_status").click()
        po2_1 = self.find(By.ID, "tv_flash_sale_status").click()
        # 等待页面跳转
        time.sleep(3)
        po3 = self.find(By.ID, "tv_name").click()
        po4 = self.find(By.ID, "tv_bottom_buy_now").click()
        po5 = self.find(By.ID, "tv_buy_now").click()
        po6 = self.find(By.ID, "tv_submit_order").click()

        self.common_backtomainpage()
        po7 = self.find(By.ID, "iv_base_left").click()

    def place_order_O2OCart(self):
        self.search_goodsO2O()
        po1 = self.find(By.XPATH, "//*[contains(@text,'东信 对乙酰氨基酚栓')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        po2 = self.find(By.ID, "iv_cart").click()
        time.sleep(3)
        po3 = self.find(By.ID, "tv_next").click()
        po4 = self.find(By.ID, "tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.find(By.ID, "iv_back").click()

    def place_order_O2OBuyNow(self):
        self.search_goodsO2O()
        po1 = self.find(By.XPATH, "//*[contains(@text,'东信 对乙酰氨基酚栓')]").click()
        # po2 = self.find(By.ID,"iv_img").click()
        time.sleep(3)
        po3 = self.find(By.ID, "tv_bottom_buy_now").click()
        po4 = self.find(By.ID, "tv_buy_now").click()
        po5 = self.find(By.ID, "tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.find(By.ID, "iv_back").click()
        po7 = self.find(By.ID, "iv_back").click()

    def cancel_order(self):
        cel1 = self.find(By.ID, "radio_profile").click()
        cel2 = self.find(By.ID, "img_my_orders").click()
        cel3 = self.find(By.ID, "bt_cancel")[0].click()
        cel4 = self.find(By.ID, "iv_check").click()
        cel5 = self.find(By.ID, "bt_sure").click()
        time.sleep(3)
        cel6 = self.find(By.ID, "iv_base_left").click()
        cel7 = self.find(By.ID, "radio_home").click()
