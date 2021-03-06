import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from po_test_hysapp.driver.hysClient import HysClient
from datetime import datetime
import allure
import os
import logging
import time


class HysBase(object):
    """
        Page基类，它包括了所有定位元素的方法，所有的page都要继承该类
        初始化一个所有页面都要使用的driver，其他页面继承了就可以直接用self.driver用
        导出都是findelement，所以封装一下给所有页面用
    """
    black_element = [(By.XPATH, 'black-1'), (By.XPATH, 'black-2')]  # 这是弹窗黑名单按钮
    # wait_element = ("aa","tv_price_desc","cc")
    driver: WebDriver

    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):  # 此处是获取HysClient类的driver  但是不初始化APP生成driver
        cls.driver = HysClient.driver
        return cls.driver

    # 定义一个Client实例化供APP类调用
    @classmethod
    def getClient(cls):
        return HysClient

    # def find(self,kv)->WebElement:
    #     return self.find(*kv)

    def screenshots(self):
        time.sleep(1.5)
        name = datetime.now().strftime("%Y%m%d%H%M%S")
        # self.driver.get_screenshot_as_file(r'D:\Projects\page_object\ut\%s.png' % name)
        self.driver.get_screenshot_as_file(r'%s.png' % name)
        pic = name + '.png'
        file = open(pic, 'rb').read()  # 先把文件open 然后再read读取一下，然后即可把这个文件加到allure中
        allure.attach.file(pic, attachment_type=allure.attachment_type.PNG)  # attach图片上步已经可以读取，直接写上名字就可以了
        os.remove(pic)

    def send_mail(self, msg1, pic1, receiver1):
        # todo: 实现发邮件
        # SendMail.sendMail(msg1,pic1,receiver1)
        return 1

    def getToastMsg(self):
        # msg = self.findByXpath("@class='android.widget.Toast'").text
        toast = self.find(By.XPATH, "//*[@class='android.widget.Toast']")
        logging.info("打印是否获取到toast: %s" % toast)
        msg = toast.text
        logging.info("打印是否获取到msg: %s" % msg)
        return msg

    def swipe_ui(self, action):
        # Swipe（int start x, int start y, int end x, int y, duration)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        if action == "down":
            self.driver.swipe(int(x * 0.5), int(y * 0.2), int(x * 0.5), int(y * 0.5), 1000)
        elif action == "up":
            self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.5), 1000)
        elif action == "left":
            self.driver.swipe(int(x * 0.2), int(y * 0.5), int(x * 0.5), int(y * 0.5), 1000)
        else:  # 右滑或者返回
            self.driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.2), int(y * 0.5), 1000)
        time.sleep(2)

    def find(self, by, value):
        element: WebElement
        # 按钮是否等待
        # for e in HysBase.wait_element:
        #     if e == value:
        #         time.sleep(2)
        #         break
        # 加上重试机制，例如3次，目的是为了防止这个控件没有加载出来
        for i in range(2):
            try:
                element = self.driver.find_element(by, value)
                return element  # return 直接结束函数
            except:
                # self.driver.page_source     # 这是一个页面的XML，找到页面顶层元素进行点击
                # 动态变化位置的元素处理

                # 未找到元素可能是有弹窗，进行黑名单处理
                ##//*[@text='弹窗']/..//*[@text='确认']
                for e in HysBase.black_element:
                    elements = self.driver.find_elements(*e)  # *e 是一个（a,b） 挨个在界面上尝试找黑名单元素
                    if elements != []:  # 如果这个元素存在，则__sizeof__>0
                        elements[0].click()  # 则找到这个元素的第一个，点了它
                # 如果黑名单没有就报错

    def findByText(self, text) -> WebElement:
        return self.find(By.XPATH, "//*[@text='%s']" % text)

    def findByXpath(self, xpath) -> WebElement:
        return self.find(By.XPATH, "//*[%s]" % xpath)

    # 该方法将搞定一切操作流程，原理通过yaml文件直接进行每一步操作
    def loadSteps(self, yaml_path, key, **kwargs):  # 文件目录、key：Android IOS 字典参数
        file = open(yaml_path, 'r')
        data = yaml.load(file, Loader=yaml.FullLoader)
        po_method = data[key]
        po_element = dict()
        if data.keys().__contains__('elements'):  # 以防文件中没有elements
            po_element = data['elements']  # 里面是一个字典， 用element就说明是多平台
        # 如果elements存在于其他的yaml文件中，po_element = yaml.load('xxx.yaml')['elements']

        for step in po_method:  # step是一个集合
            step: dict
            element_step = dict()
            # 判断一下step中有没有element
            if step.keys().__contains__("element"):  # 此处是为了解决跨系统的问题控件不一样操作是一样的则可以合并（该控件安卓和IOS不一样）
                element_step = po_element[step['element']][
                    'android']  # step['element'] = element的值；[step['element']] 就是[account]
            else:
                element_step = {"by": step['by'], "locator": step['locator']}  # 取得step的by和locator
            # 注明一下类型以防报错
            element: WebElement = self.find(by=element_step['by'], value=element_step['locator'])
            if str(step['action']).lower() == 'click':  # .lower()转成小写，避免里面有大写
                element.click()
            elif str(step['action']).lower() == 'clear':
                element.clear()
            elif str(step['action']).lower() == 'send_keys':  # 涉及到传参替换的问题
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)  # 深入了解这里是一个循环替换符合条件的k,v
                element.send_keys(text)
            else:
                print("%s 步骤发生情况不知道如何操作" % step)
