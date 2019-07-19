from page_object.driver.Client import AndroidClient
from page_object.pages.BasePage import BasePage
from page_object.pages.MainPage import MainPage


#这个类是用来重启APP的？
class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()   #通过类方法调用上个类中的方法
        return MainPage()