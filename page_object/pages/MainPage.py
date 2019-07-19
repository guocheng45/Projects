from selenium.webdriver.common.by import By

from page_object.driver.Client import AndroidClient

from page_object.pages.BasePage import BasePage
from page_object.pages.ProfilePage import ProfilePage
from page_object.pages.SearchPage import SearchPage
from page_object.pages.SelectedPage import SelectedPage


class MainPage(BasePage):
    _profile_button=(By.ID,"user_profile_icon")
    _search_button=(By.ID,"home_search")

    def gotoSelected(self):

        #避免出错定位两次后进行点击
        # self.driver.find_element(By.xpath,"//*[@test='自选']")
        zixuan = "自选"
        self.findByText(zixuan)
        # self.driver.find_element_by_xpath("//*[@test='自选']")
        # self.driver.find_element_by_xpath("//*[@test='自选']").click()
        self.findByText(zixuan).click()
        return SelectedPage()

    def gotoSearch(self) ->SearchPage:
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        self.loadSteps("..page_object/data/MainPage.yaml","gotoProfile")

        return ProfilePage()
