from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class BasePage(object):

    def __init__(self,driver):
        self.driver:WebDriver = driver

    def driver_quit(self):
        sleep(4)
        self.driver.quit()
        return self