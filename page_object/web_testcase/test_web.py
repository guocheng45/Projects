# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.ehaoyao.com")
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[3]/span[1]").click()


handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        driver.close()
        driver.switch_to.window(handle)

driver.find_element_by_id("loginName").send_keys("13663397421")
driver.find_element_by_id("loginPwd").send_keys("abc123")
driver.find_element_by_id("submitLogin2").click()
time.sleep(2)

