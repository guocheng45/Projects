from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import AndroidClient
import yaml

class BasePage(object):
    element_black=[(By.XPATH,"adad")]

    def __init__(self):     #初始化AndroidClient的driver
        self.driver: WebDriver=self.getDriver()

    @classmethod     #这个方法是获取到AndroidClient中的driver
    def getDriver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver

    @classmethod   #这个方法是用来干啥的？返回AndroidClient类
    def getClient(cls):
         return AndroidClient

    def find(self,kv) ->WebElement:     #根据findByText提供的关键字找控件          指定方法的返回类型
        #todo:处理各类弹窗
        return self.find(*kv)

    def find(self, by, value):
        element: WebElement
        #加上重试机制，重试3次
        for i in range(3):
            try:
                element=self.driver.find_element(by, value)
                return element
            except:
                # 找到页面的最顶层元素，进行点击
                # self.driver.page_source
                # get_maxdepth_element.click()

                # 黑名单
                ##//*[@text='弹窗']/..//*[@text='确认']
                for e in BasePage.element_black:
                    elements = self.driver.find_element(*e)     #在黑名单中找到元素
                    # 判断元素的大小
                    if (elements.__sizeof__()>0):
                        elements[0].click()


    def findByText(self,text)-> WebElement:     #此处设置关键字文本      指定方法的返回类型
        return self.find((By.XPATH,"//*[@txt='%s']" %text))


    def loadSteps(self,po_path,key,**kwargs):          #解析
        file = open(po_path,'r')
        po_data = yaml.load(file)       #把文件中的数据都读取到po_data中
        po_method = po_data[key]        #读出具体的key值
        po_elements=dict()
        if po_data.keys().__contains__("elements"):
            po_elements=po_data['elements']     #获取elements中的值赋给po_elements

        for step in po_method:
            step: dict
            element_platform=dict()
            if step.keys().__contains__("element"):
                element_platform=po_elements[step['element']][AndroidClient.platform]    #读取其中具体的节点值
            else:
                element_platform={"by":step['by'],'locator':step['locator']}
            element:WebElement = self.driver.find_element(by=step['by'],value=step['locator'])
            action = str(step['action']).lower()        #lower()强转为string小写
            #todo:  处理失败，多数是弹窗，造成，try catch 后进入弹窗处理 元素的智能等待
            if action=='click':      #转小写.lower()
                element.click()
            elif action=="sendKeys":
                text=str(step['text'])
                for k,v in kwargs.items():
                    text=text.replace("$%s" %k,v)
                    print("update text:%s" % (text))
                element.send_keys(text)
            else:
                 print("UNKNOW COMMAND %s" % step)