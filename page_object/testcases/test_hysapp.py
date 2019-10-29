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
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def install_app(self):
        pass


    def start_app(self):
        pass

    def login_app(self):
        self.driver.implicitly_wait(10)
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
        pass

    def place_order(self):
        pass

    def cancel_order(self):
        pass

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.quit()

    def test_hysapp(self):
        #self.install_app()
        self.login_app()
        self.logout_app()