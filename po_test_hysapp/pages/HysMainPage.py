from selenium.webdriver.common.by import By
from po_test_hysapp.pages.HysBase import HysBase
from po_test_hysapp.pages.ProfilePage import ProfilePage
from po_test_hysapp.pages.SearchPage import SearchPage
from po_test_hysapp.pages.CartsPage import CartsPage
from po_test_hysapp.pages.OrderPage import OrderPage


class HysMainPage(HysBase):
    """
        # 首页首先初始化driver  这个初始化就放置到App类里面去
        # 方法是goto其他page，这样在case中就可以直接通过goto方法访问下一页面的方法
    """



    def gotoProfile(self) -> ProfilePage:  # 如果返回不指定返回类型，使用时就不嫩玩链式调用    这个只是告诉看你代码的人，返回类型是啥。python 没有强制检测???试试吧
        # 调用全局的driver对象使用webdriver 定位元素
        self.find(By.ID, "fl_radio_profile").click()
        return ProfilePage()

    def gotoSearchpage(self):
        self.find(By.ID, "qmy_main_search_ll").click()
        return SearchPage()

    def gotoCartspage(self):
        self.find(By.ID,"radio_cart").click()
        return CartsPage()

    # # 首页不能直接到订单页从购物车可以
    # def gotoOrderpage(self):
    #     self.find(By.ID,"").click()
    #     return OrderPage()
