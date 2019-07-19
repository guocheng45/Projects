# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"
caps["noreSet"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)

el1 = driver.find_element_by_id("tv_search")
el1.click()
el2 = driver.find_element_by_id("search_input_text")
el2.click()
el2.send_keys("alibaba")
el3 = driver.find_element_by_id("search_input_text")
el3.click()
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
el4.click()
el5 = driver.find_element_by_id("md_buttonDefaultNegative")
el5.click()


driver.quit()