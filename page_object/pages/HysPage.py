from selenium.webdriver.common.by import By
import time

from page_object.pages.HysBase import HysBase


class HysPage(HysBase):
    """
        # 该page的方法返回的结果是一个值类用于testcase断言使用
        self.driver.find_element_by_xpath("XXXX")
        对页面的每一步操作都用一个方法封装
        也可以对一个操作功能进行封装
        为了引用该类的时候调用到类里面的变量，可以给变量加_不会被看到
    """

    def getErrorMsg(self):
        msg=self.find("self._error_msg").text
        self.findByText("确定").click()
        return msg

    def getToastMsg(self):
        msg = self.findByXpath("@class='android.widget.Toast'").text
        return msg

    def login_app(self,var1=15001106951,var2=123456):
        self.loadSteps("../data/hys.yaml","login_app",phone=var1,pwd=var2)
        # self.find(By.ID,"fl_radio_profile").click()
        # self.find(By.ID, "btn_login").click()
        # self.find(By.ID, "clet_phone").send_keys("15001106951")
        # self.find(By.ID, "clet_password").send_keys('123456')
        # self.find(By.ID, "btn_submit").click()
        return self         # 返回self是为了链式调用，也就是说可以方法连着调方法  ：func1().func2().func3()

    def login_app(self):
        # el1=driver.find_element_by_id("ll_skip").click()
        el2 = self.driver.find_element_by_id("fl_radio_profile").click()
        # el2_=driver.find_element_by_id("iv").click()
        el3 = self.driver.find_element_by_id("btn_login").click()
        el4 = self.driver.find_element_by_id("clet_phone").send_keys("15001106951")
        el5 = self.driver.find_element_by_id("clet_password").send_keys('123456')
        el6 = self.driver.find_element_by_id("btn_submit").click()

    def logout_app(self):
        time.sleep(2)
        el7 = self.driver.find_element_by_id("ll_setting").click()
        el8 = self.driver.find_element_by_id("btn_logout").click()

    def search_goodsB2C(self):
        sel1=self.driver.find_element_by_id("radio_home").click()
        sel2=self.driver.find_element_by_id("qmy_main_search_ll").click()
        self.driver.implicitly_wait(10)
        sel3=self.driver.find_element_by_id("et_search").send_keys('感冒')
        sel4=self.driver.find_element_by_id("bt_search").click()
        self.driver.implicitly_wait(5)
        sel5=self.driver.find_element_by_id("tv_desc").click()
        sel6=self.driver.find_element_by_id("tv_desc_2").click()
        self.driver.implicitly_wait(10)

    def search_goodsO2O(self):
        sel1=self.driver.find_element_by_id("function_img").click()
        sel2=self.driver.find_element_by_id("et_search").click()
        self.driver.implicitly_wait(10)
        sel3=self.driver.find_element_by_id("et_search").send_keys('感冒')
        sel4=self.driver.find_element_by_id("bt_search").click()
        self.driver.implicitly_wait(5)
        sel5=self.driver.find_element_by_id("tv_desc").click()
        sel6=self.driver.find_element_by_id("tv_desc_2").click()
        self.driver.implicitly_wait(10)

    def swipe_ui(self,act):
        time.sleep(4)
        # Swipe（int start x, int start y, int end x, int y, duration)
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        if act=="下拉":
            self.driver.swipe(int(x * 0.5), int(y * 0.2), int(x * 0.5), int(y * 0.5), 1000)
        elif act=="上拉":
            self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.5), 1000)
        elif act=="左滑":
            self.driver.swipe(int(x * 0.2), int(y * 0.5), int(x * 0.5), int(y * 0.5), 1000)
        else:   # 右滑或者返回
            self.driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.2), int(y * 0.5), 1000)
        time.sleep(4)


    def common_backtomainpage(self):
        # 下单不支付
        cb1 = self.driver.find_element_by_id("iv_base_left").click()
        cb2 = self.driver.find_element_by_id("tv_sure").click()
        self.driver.implicitly_wait(10)
        # 返回到首页
        cb3 = self.driver.find_element_by_id("iv_base_left").click()
        cb4 = self.driver.find_element_by_id("iv_back").click()
        cb5 = self.driver.find_element_by_id("iv_back").click()

    def place_order_B2CCart(self):
        self.search_goodsB2C()
        self.swipe_ui("上拉")
        pel1=self.driver.find_element_by_xpath("//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        pel2=self.driver.find_element_by_id("iv_cart").click()
        # self.driver.implicitly_wait(10)
        # pel3=self.driver.find_element_by_id("rb_pharmacy_check").click()
        # time.sleep(3)
        # pel4=self.driver.find_element_by_xpath("//*[@text='马应龙 对乙酰氨基酚栓 0.125g*6s']/../..//*[contains(@resource-id,'rb_check')]").click()
        time.sleep(3)
        pel5=self.driver.find_element_by_id("tv_next").click()
        pel6=self.driver.find_element_by_id("tv_submit_order").click()
        # 余额支付，不要支付了，不好退
        # pel7=self.driver.find_element_by_id("cb_use_balance").click()
        # pel8=self.driver.find_element_by_id("btn_add_addresss").click()
        # self.driver.implicitly_wait(10)
        # pel9=self.driver.find_element_by_id("tv_sure").click()
        # self.driver.implicitly_wait(10)
        # pel10=self.driver.find_element_by_id("tv_order_detail").click()
        self.common_backtomainpage()

    def place_order_B2CBuyNow(self):
        self.search_goodsB2C()
        self.swipe_ui("上拉")
        po1 = self.driver.find_element_by_xpath("//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]").click()
        # po2 = self.driver.find_element_by_id("iv_img").click()
        time.sleep(3)
        po3 = self.driver.find_element_by_id("tv_bottom_buy_now").click()
        po4 = self.driver.find_element_by_id("tv_buy_now").click()
        po5 = self.driver.find_element_by_id("tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.driver.find_element_by_id("iv_back").click()

    def place_order_B2CSale(self):
        po1 = self.driver.find_element_by_id("ac_title").click()
        # po1 = self.driver.find_element_by_xpath("//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        # 多点两次页签2，怕点不中
        po2 = self.driver.find_element_by_id("tv_flash_sale_status").click()
        po2_1 = self.driver.find_element_by_id("tv_flash_sale_status").click()
        # 等待页面跳转
        time.sleep(3)
        po3 = self.driver.find_element_by_id("tv_name").click()
        po4 = self.driver.find_element_by_id("tv_bottom_buy_now").click()
        po5 = self.driver.find_element_by_id("tv_buy_now").click()
        po6 = self.driver.find_element_by_id("tv_submit_order").click()

        self.common_backtomainpage()
        po7 = self.driver.find_element_by_id("iv_base_left").click()

    def place_order_O2OCart(self):
        self.search_goodsO2O()
        po1 = self.driver.find_element_by_xpath("//*[contains(@text,'东信 对乙酰氨基酚栓')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        po2 = self.driver.find_element_by_id("iv_cart").click()
        time.sleep(3)
        po3 = self.driver.find_element_by_id("tv_next").click()
        po4 = self.driver.find_element_by_id("tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.driver.find_element_by_id("iv_back").click()

    def place_order_O2OBuyNow(self):
        self.search_goodsO2O()
        po1 = self.driver.find_element_by_xpath("//*[contains(@text,'东信 对乙酰氨基酚栓')]").click()
        # po2 = self.driver.find_element_by_id("iv_img").click()
        time.sleep(3)
        po3 = self.driver.find_element_by_id("tv_bottom_buy_now").click()
        po4 = self.driver.find_element_by_id("tv_buy_now").click()
        po5 = self.driver.find_element_by_id("tv_submit_order").click()

        self.common_backtomainpage()
        po6 = self.driver.find_element_by_id("iv_back").click()
        po7 = self.driver.find_element_by_id("iv_back").click()

    def cancel_order(self):
        cel1 = self.driver.find_element_by_id("radio_profile").click()
        cel2 = self.driver.find_element_by_id("img_my_orders").click()
        cel3 = self.driver.find_elements_by_id("bt_cancel")[0].click()
        cel4 = self.driver.find_element_by_id("iv_check").click()
        cel5 = self.driver.find_element_by_id("bt_sure").click()
        time.sleep(3)
        cel6 = self.driver.find_element_by_id("iv_base_left").click()
        cel7 = self.driver.find_element_by_id("radio_home").click()