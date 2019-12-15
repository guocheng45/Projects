from selenium.webdriver.common.by import By

from page_object.driver.hysClient import HysClient
from page_object.pages.HysPage import HysPage
from page_object.pages.HysBase import HysBase


class HysMainPage(HysBase):

    """
        # 首页首先初始化driver  这个初始化就放置到App类里面去
        # 方法是goto其他page，这样在case中就可以直接通过goto方法访问下一页面的方法
    """

    _search_button=(By.ID,"radio_home")

    def gotoProfile(self)->HysPage:     # 如果返回不指定返回类型，使用时就不嫩玩链式调用    这个只是告诉看你代码的人，返回类型是啥。python 没有强制检测???试试吧
        #调用全局的driver对象使用webdriver 定位元素
        # self.driver.find_element_by_xpath()    # 有时find可能会报错，find两次比较保险
        # page_button=(By.ID,"fl_radio_profile")
        self.find(By.ID,"fl_radio_profile").click()
        return HysPage()

    def gotoSearchpage(self):
        self.find(By.ID,"radio_home").click()
        return HysPage()