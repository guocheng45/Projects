# from page_object.driver.hysClient import HysClient
from page_object.pages.HysBase import HysBase
from page_object.pages.HysMainPage import HysMainPage


class HysApp(HysBase):
    """
        # APP 负责初始化APP 返回一个HysMainPage 这样case里面就可以直接通过App来调用后续
        # 该类是为了衔接Client和MainPage的
    """
    @classmethod
    def main(cls):
        # HysClient.start_app()
        cls.driver = HysBase._driver
        if cls.driver is None:
            cls.getClient().start_app()     # 此处通过Base类调用，意义不大
        return HysMainPage()

