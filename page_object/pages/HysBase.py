import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.hysClient import HysClient


class HysBase(object):
    """
        Page基类，它包括了所有定位元素的方法，所有的page都要继承该类
        初始化一个所有页面都要使用的driver，其他页面继承了就可以直接用self.driver用
        导出都是findelement，所以封装一下给所有页面用
    """

    def __init__(self):
        # self.driver=HysClient.driver
        # 使用什么driver
        self.driver:WebDriver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=HysClient.driver
        return cls.driver

    # 定义一个Client实例化供APP类调用
    @classmethod
    def getClient(cls):
        return HysClient

    def find(self,kv)->WebElement:
        return self.driver.find_element(*kv)
    # def find(self,by ,value)->WebElement:
    #     element:WebElement
    #     #重试
    #     for i in range(3):
    #         try:
    #             element=self.driver.find_element(by,value)
    #             return element
    #         except:
    #             print("未找到元素")

    def findByText(self,text)->WebElement:
        return self.find(By.XPATH,"//*[@text='%s']" %text)

    # 该方法将搞定一切操作流程，原理通过yaml文件直接进行每一步操作
    def loadSteps(self,yaml_path,key,**kwargs):     # 文件目录、key：Android IOS 字典参数
        file=open(yaml_path,'r')
        data=yaml.load(file)
        po_method=data(key)
        for step in po_method:
            # 注明一下类型以防报错
            element:WebElement=self.driver.find_element(by=step['by'],value=step['locator'])
            # 此处加上try catch 避免一下弹窗阻碍
            if str(step['action']).lower()=='click':    # .lower()转成小写，避免里面有大写
                element.click()
            elif str(step['action']).lower()=='send_keys':  # 涉及到传参替换的问题
                text=str(step['text'])
                for k,v in kwargs.items():
                    text=text.replace("$%s" %k,v)     # 深入了解这里是一个循环替换符合条件的k,v
                element.send_keys(step['text'])
            else:
                print("%s 步骤发生情况不知道如何操作" %step)