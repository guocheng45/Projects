
from page_object.driver.hysClient import HysClient
from page_object.pages.HysMainPage import HysMainPage


class App(object):
    """
        # APP 负责初始化APP 返回一个HysMainPage 这样case里面就可以直接通过App来调用后续
    """
    @classmethod
    def main(self):
        HysClient.start_app()
        return HysMainPage()

