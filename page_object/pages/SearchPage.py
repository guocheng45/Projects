from selenium.webdriver.common.by import By

from page_object.driver.Client import AndroidClient
from page_object.pages.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator = (By.CLASS_NAME,"android.widget.EdiText")

    def search(self, key):
        self.find(self.__edit__locator).send_keys(key)      #找到元素并发送搜索关键字
        return self     # 返回self是为了链式调用，也就是说可以方法连着调方法  ：func1().func2().func3()

    def find(self,key):
        self.find(self._edit_locator).send_keys(key)
        return self

    def addToSelected(self,key):
        follow_button = (By.XPATH,"//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow_btn')]")

        self.find(follow_button).click()
        return self

    def removeFromSelected(self,key):
        followed_button = (By.XPATH,"//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'followed_btn')]")
        self.find(followed_button).click()
        return self

    def isInSelected(self,key):
        follow_button = (By.XPATH,"//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." %key +
                       "//*[contains(@resource-id, 'follow')]")
        id = self.find(follow_button).get_attribute("resourceId")  # 找到元素获取的它的某个东西
        print(id)
        return "followed_btn" in id

    def cancel(self):
        self.findByText("取消").click()
        return self

    def searchByUser(self):
        #todo:zuoyi1
        pass

    def idFollowed(self):
        #todo:zuoyi2
        pass

