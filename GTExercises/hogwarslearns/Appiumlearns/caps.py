import time

from appium import webdriver

import pytest
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAndroid(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("XXDDSD")

    def setup_method(self):
        print("SDSDSD")



    def test_swipe(self):
        for i in range(5):
            #滑动界面
            self.driver.swipe(1000,1000,200,200)
            time.sleep(2)
            # 截图
            self.driver.get_screenshot_as_file(i + ".png")

    def test_login(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "192.168.211.102:5555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)

        el1 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        driver.implicitly_wait(20)
        el1.send_keys("alibaba")
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
        el2.click()
        el3 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative")
        el3.click()

        #driver.quit()

    def test_jijin(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "192.168.211.102:5555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)
        el2 = driver.find_element_by_xpath("//[contains(@resource-id, 'buttons_container')]//[@text='基金']")
        driver.quit()
