from web.page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def follow(self,keyword):       #follow  关键字  1688
        self.driver.find_element_by_xpath('//*[contains(text(),"%s")]'%keyword).click()
        return self