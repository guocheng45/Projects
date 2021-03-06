from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class HysClient(object):
    """
        # 是一个driver类，用于启动APP，重装APP
        # 用于basePage或者Mainpage来调用初始化driver
    """

    driver:WebDriver    # driver设置成WebDriver格式对象

    @classmethod
    def start_app(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "GT_New"
        caps["appPackage"] = "com.jzt.kingpharmacist"
        caps["appActivity"] = ".apploadpage.LoadingAc"
        caps["autoGrantPermissions"] = True
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(3)       # 隐式等待是对全局元素设置的隐式等待时间，影响全局速度
        return cls.driver
