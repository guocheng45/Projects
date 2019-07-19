from page_object.pages.BasePage import BasePage
from page_object.pages.LoginPage import LoginPage


class ProfilePage(BasePage):


    def gotoProfile(self):
        self.loadSteps("../data/LoginPage.yaml","gotoLogin")
        #self.findByText("个人页").click()
        return LoginPage()