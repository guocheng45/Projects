# from page_object.driver.hysClient import HysClient
from po_test_hysapp.pages.HysBase import HysBase
from po_test_hysapp.pages.HysMainPage import HysMainPage


class HysApp(HysBase):
    """
        # APP 负责初始化APP 返回一个HysMainPage 这样case里面就可以直接通过App来调用后续
        # 该类是为了衔接Client和MainPage的
    """
    @classmethod
    def main(cls):
        # HysClient.start_app()
        cls.getClient().start_app()     # 此处通过Base基类调用
        return HysMainPage()

