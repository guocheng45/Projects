from appium.webdriver.common.mobileby import MobileBy

from page_object.driver.Client import AndroidClient
from page_object.pages.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHuShen(self):
        self.findByText("沪深").click()
        return self

    def getPriceByName(self,name) ->float:

        priceLocation = (MobileBy.XPATH,"//*[contains(@resource-id,'stockName') and @test='"+name+"']/../../.."
                 "//*[contains(@resource-id,'currentPrice')]")
        price = self.find(priceLocation).text
        return float(price)