#-*- coding: UTF-8 -*-
from appium import webdriver
desired_caps={
              'platformName':'Android',
              'platformVersion':'5.1.1',
              'deviceName':'emulator-5554',
              'appPackage':'com.android.gallery',
              'appActivity':'com.android.camera.GalleryPicker'
              }
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#其第一个参数是appium server监听的端口
driver.find_element_by_name('Phone').click()
driver.find_element_by_name('1').click()
driver.find_element_by_name('3').click()
driver.find_element_by_name('*').click()
driver.find_element_by_name('1').click()
driver.find_element_by_name('5').click()
driver.find_element_by_name('9').click()
driver.find_element_by_name('delete').click()
driver.find_element_by_name('=').click()
driver.quit()
driver.install_app('path/to/my.app')#安装包到设备
driver.removeApp('com.example.android.apis')#删除一个设备中的应用
driver.close_app()#关闭应用
driver.launch_app()#启动应用
driver.is_app_installed('com.example.android.apis')#应用是否安装
driver.reset()#应用重置
driver.background_app(seconds)#应用置于后台运行,时长