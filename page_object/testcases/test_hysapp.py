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
        cls.driver.implicitly_wait(10)

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

    def search_goods(self):
        sel1=self.driver.find_element_by_id("radio_home").click()
        sel2=self.driver.find_element_by_id("qmy_main_search_ll").click()
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


    def place_order(self):
        self.search_goods()
        self.swipe_ui("上拉")
        pel1=self.driver.find_element_by_xpath("//*[contains(@text,'马应龙 对乙酰氨基酚栓 0.125g*6s')]/../..//*[contains(@resource-id,'com.jzt.kingpharmacist:id/iv_buy')]").click()
        # time.sleep(4)
        pel2=self.driver.find_element_by_id("iv_cart").click()
        # self.driver.implicitly_wait(10)
        # pel3=self.driver.find_element_by_id("rb_pharmacy_check").click()
        # time.sleep(3)
        # pel4=self.driver.find_element_by_xpath("//*[@text='马应龙 对乙酰氨基酚栓 0.125g*6s']/../..//*[contains(@resource-id,'rb_check')]").click()
        time.sleep(3)
        pel5=self.driver.find_element_by_id("tv_next").click()
        # self.driver.implicitly_wait(10)
        pel6=self.driver.find_element_by_id("tv_submit_order").click()
        # self.driver.implicitly_wait(10)
        # 余额支付，不要支付了，不好退
        # pel7=self.driver.find_element_by_id("cb_use_balance").click()
        # pel8=self.driver.find_element_by_id("btn_add_addresss").click()
        # self.driver.implicitly_wait(10)
        # pel9=self.driver.find_element_by_id("tv_sure").click()
        # self.driver.implicitly_wait(10)
        # pel10=self.driver.find_element_by_id("tv_order_detail").click()
        # 下单不支付
        pel_1=self.driver.find_element_by_id("iv_base_left").click()
        pel_2 = self.driver.find_element_by_id("tv_sure").click()
        self.driver.implicitly_wait(10)
        # 返回到首页
        cel_3 = self.driver.find_element_by_id("iv_base_left").click()
        cel_4 = self.driver.find_element_by_id("iv_back").click()
        cel_5 = self.driver.find_element_by_id("iv_back").click()



    def cancel_order(self):
        cel1 = self.driver.find_element_by_id("radio_profile").click()
        cel2 = self.driver.find_element_by_id("img_my_orders").click()
        cel3 = self.driver.find_elements_by_id("bt_cancel")[0].click()

        cel4 = self.driver.find_element_by_id("iv_check").click()
        cel5 = self.driver.find_element_by_id("bt_sure").click()
        cel6 = self.driver.find_element_by_id("iv_base_left").click()
        cel7 = self.driver.find_element_by_id("radio_home").click()



    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        cls.driver.quit()

    def test_hysapp(self):
        #self.install_app()
        # self.login_app()
        # self.logout_app()
        # self.search_goods()
        self.place_order()
        self.cancel_order()