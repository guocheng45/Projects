from page_object.driver.hysClient import HysClient
from page_object.pages import HysPage


class HysMainPage(object):

    """
        # 首页首先初始化driver
        # 方法是goto其他page，这样在case中就可以直接通过goto方法访问下一页面的方法
    """

    def __init__(self):
        HysClient.start_app()

    def gotoSearch(self):
        #调用全局的driver对象使用webdriver 定位元素
        HysClient.driver.find_element_by_xpath()    # 有时find可能会报错，find两次比较保险

        return HysPage()
