from appium.webdriver.webdriver import WebDriver


class Aaa(object):

    driver: WebDriver
    def __init__(self):
        self.driver=self.getDriver()

    # driver: WebDriver
    # def __init__(self, driver: WebDriver=None):
    #     self.driver= driver

    def fun1(self):
        a=1
        print("==============",a)
        return a

    @classmethod
    def getDriver(cls):
        cls.driver="getDriver"
        return cls.driver

    @classmethod
    def fun2(cls):
        b=2
        print("===========",cls.driver)
        print("==========",b)
        return b
