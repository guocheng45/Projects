#-*-coding:GBK -*-
from appium import webdriver
import time

class TestHysApp(object):

    @classmethod
    def setup_class(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "GT_New123"
        caps["appPackage"] = "com.jzt.kingpharmacist"
        caps["appActivity"] = ".apploadpage.LoadingAc"
        caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "True"
        caps["unicodeKeyboard"]="True"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)

    def install_app(self):
        pass

    def login_app(self):
        # el1=driver.find_element_by_id("com.jzt.kingpharmacist:id/ll_skip").click()
        el2 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/fl_radio_profile").click()
        # el2_=driver.find_element_by_id("com.jzt.kingpharmacist:id/iv").click()
        el3 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_login").click()
        el4 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/clet_phone").send_keys("15001106951")
        el5 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/clet_password").send_keys('123456')
        el6 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_submit").click()

    def logout_app(self):
        time.sleep(2)
        el7 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/ll_setting").click()
        el8 = self.driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_logout").click()

    def search_goodsB2C(self):
        sel1=self.driver.find_element_by_id("radio_home").click()
        sel2=self.driver.find_element_by_id("qmy_main_search_ll").click()
        sel3=self.driver.find_element_by_id("et_search").send_keys('感冒')
        sel4=self.driver.find_element_by_id("bt_search").click()
        sel5=self.driver.find_element_by_id("tv_desc").click()
        sel6=self.driver.find_element_by_id("tv_desc_2").click()

    def search_goodsO2O(self):
        sel1=self.driver.find_element_by_id("function_img").click()
        sel2=self.driver.find_element_by_id("et_search").click()
        sel3=self.driver.find_element_by_id("et_search").send_keys('感冒')
        sel4=self.driver.find_element_by_id("bt_search").click()
        sel5=self.driver.find_element_by_id("tv_desc").click()
        sel6=self.driver.find_element_by_id("tv_desc_2").click()

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
        # 返回到首页
        cb3 = self.driver.find_element_by_id("iv_base_left").click()
        cb4 = self.driver.find_element_by_id("iv_back").click()
        cb5 = self.driver.find_element_by_id("iv_back").click()

    def place_order_B2CCart(self):
        self.search_goodsB2C()
        self.swipe_ui("上拉")
        pel1=self.driver.find_element_by_xpath("//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'iv_buy')]").click()
        pel2=self.driver.find_element_by_id("iv_cart").click()
        # pel3=self.driver.find_element_by_id("rb_pharmacy_check").click()
        # time.sleep(3)
        # pel4=self.driver.find_element_by_xpath("//*[@text='马应龙 对乙酰氨基酚栓 0.125g*6s']/../..//*[contains(@resource-id,'rb_check')]").click()
        time.sleep(3)
        pel5=self.driver.find_element_by_id("tv_next").click()
        pel6=self.driver.find_element_by_id("tv_submit_order").click()
        # 余额支付，不要支付了，不好退
        # pel7=self.driver.find_element_by_id("cb_use_balance").click()
        # pel8=self.driver.find_element_by_id("btn_add_addresss").click()
        # pel9=self.driver.find_element_by_id("tv_sure").click()
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


    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        cls.driver.quit()
    """
    # 例子Testcase
    def test_price(self):
        # main=MainPage()
        # 通过上一个page的方法返回的下一个page，直接调用下一page的方法，然后断言结果
        assert HysApp.main().gotoSelected().getPriceByName("科大讯飞")==28.83
    """

    def test_01_placeOrder1(self):
        self.place_order_B2CCart()
        self.cancel_order()

    def test_02_placeOrder2(self):
        self.place_order_B2CBuyNow()
        self.cancel_order()

    def test_03_placeOrder3(self):
        self.place_order_B2CSale()
        self.cancel_order()

    def test_04_placeOrder4(self):
        self.place_order_O2OCart()
        self.cancel_order()

    def test_05_placeOrder5(self):
        self.place_order_O2OBuyNow()
        self.cancel_order()

    # def test_hysapp(self):
    #     #self.install_app()
    #     # self.login_app()
    #     # self.logout_app()
    #     # self.search_goods()
    #     self.place_order()
    #     self.cancel_order()