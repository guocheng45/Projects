from datetime import datetime
from PIL import ImageGrab
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from time import sleep
import allure
import os

class BasePage(object):
    _driver = None

    def __init__(self,driver:WebDriver = None):
        if driver is None:
            # self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(10)
            self._driver.get("https://www.ehaoyao.com")
            self._driver.maximize_window()
        else:
            self._driver=driver

    def screenshots(self):
        name = datetime.now().strftime("%Y%m%d%H%M%S")+'.png'
        pic = ImageGrab.grab()  # webʵ�ֽ�������
        im = pic.convert('RGB')
        im.save(name)
        # file = open(name, 'rb').read()  # �Ȱ��ļ�open Ȼ����read��ȡһ�£�Ȼ�󼴿ɰ�����ļ��ӵ�allure��
        # allure.attach.file(name, attachment_type=allure.attachment_type.PNG)  # attachͼƬ�ϲ��Ѿ����Զ�ȡ��ֱ��д�����־Ϳ�����
        # os.remove(name)

    def find(self,by,locator):
        if isinstance(by,tuple):        # isinstance(by,tuple) �ж�by�ǲ���Ԫ��  ���ص���True��False
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by,locator)

    def driver_quit(self):
        sleep(5)
        self._driver.quit()
        return self