from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class HysClient(object):

    driver:WebDriver

    @classmethod
    def start_app(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "GT_New123"
        caps["appPackage"] = "com.jzt.kingpharmacist"
        caps["appActivity"] = ".apploadpage.LoadingAc"
        caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "True"
        caps["unicodeKeyboard"] = "True"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
