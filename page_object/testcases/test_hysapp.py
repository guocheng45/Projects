from appium import webdriver
import time

def install_app():
    caps={}
    caps["platformName"] = "android"
    caps["deviceName"] = "GT_New"
    caps["appPackage"] = "com.jzt.kingpharmacist"
    caps["appActivity"] = ".apploadpage.LoadingAc"
    caps["autoGrantPermissions"] = "true"
    caps["noSet"] = "true"

    driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)

    driver.implicitly_wait(10)
    el1=driver.find_element_by_id("com.jzt.kingpharmacist:id/ll_skip").click()
    el2=driver.find_element_by_id("com.jzt.kingpharmacist:id/fl_radio_profile").click()
    el2_=driver.find_element_by_id("com.jzt.kingpharmacist:id/iv").click()
    el3=driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_login").click()
    el4=driver.find_element_by_id("com.jzt.kingpharmacist:id/clet_phone").send_keys("15001106951")
    el5=driver.find_element_by_id("com.jzt.kingpharmacist:id/clet_password").send_keys('123456')
    el6=driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_submit").click()
    time.sleep(2)
    el7=driver.find_element_by_id("com.jzt.kingpharmacist:id/ll_setting").click()
    el8=driver.find_element_by_id("com.jzt.kingpharmacist:id/btn_logout").click()
    time.sleep(2)
    driver.quit()

def start_app():
    pass

def login_app():
    pass

def search_goods():
    pass

def place_order():
    pass

def cancel_order():
    pass

def test_hysapp():
    install_app()