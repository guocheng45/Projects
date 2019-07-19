import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAdds():
    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        cls.install_app()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = self.restart_app()

    @classmethod
    def restart_app(cls) ->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态,不重置APP
        caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    def install_app(cls) -> WebDriver:
        caps = {}
        # 如果有必要，进行第一次安装
        # caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"
        #此处要重置APP
        #caps["noreSet"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    def test_case1(self):
        el1 = self.driver.find_element_by_id("tv_search").click()
        el2 = self.driver.find_element_by_id("search_input_text").click()
        el2.send_keys("alibaba")
        el3 = self.driver.find_element_by_id("search_input_text").click()
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
        el4.click()
        el5 = self.driver.find_element_by_id("md_buttonDefaultNegative").click()

    def test_found(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@test='基金']")
        for i in range(5):
            self.driver.swipe(1000,1000,200,200)
            time.sleep(3)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000,y=1000).move_to(x=200,y=200).release().perform()
            time.sleep(3)

    def test_action_relat(self):
        rect = self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action\
                .press(x=rect['width']*0.8, y=rect['height']*0.8).move_to(x=rect['width']*0.2, y=rect['height']*0.2)\
                .release()\
                .perform()
            time.sleep(3)

    def test_windowsize(self):
        #获取设备的宽高
        print(self.driver.get_window_rect())

    def teardown_method(self):
        # 不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.quit()

    # 整个模块.py开始，调用
    def setup_app(self):
        print("setup app")
    #整个模块.py结束调用
    def teardown_module(self):
        print("py结束")
