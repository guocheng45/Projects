from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.hysClient import HysClient


class HysBase(object):
    """
        Page基类，它包括了所有定位元素的方法，所有的page都要继承该类
    """

    def __init__(self):
        self.driver:WebDriver=self.getDriver()


    @classmethod
    def getDriver(cls):
        cls.driver=HysClient.driver
        return cls.driver

    def find(self,by ,value):
        element:WebElement
        #重试
        for i in range(3):
            try:
                element=self.driver.find_element(by,value)
                return element
            except:
                print("未找到元素")


    def findByText(self,text)->WebElement:
        return self.find(By.XPATH,"//*[@text='%s']" %text)