from selenium.webdriver.common.by import By
from po_test_hysapp.pages.HysBase import HysBase


class LoginPage(HysBase):

    def login_app(self, var1, var2):
        self.loadSteps("data/hys.yaml", "login_app", phone=var1, pwd=var2)
        return self  # 返回self是为了链式调用，也就是说可以方法连着调方法  ：func1().func2().func3()

    def login_success_byuser(self, var1, var2):
        self.loadSteps("data/hys.yaml", "login_app", phone=var1, pwd=var2)
        return self