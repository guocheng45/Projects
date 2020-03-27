from selenium.webdriver.common.by import By
import time
from po_test_hysapp.pages.HysBase import HysBase
from po_test_hysapp.pages.LoginPage import LoginPage


class ProfilePage(HysBase):
    """
        # 该page的方法返回的结果是一个值类用于testcase断言使用
        self.driver.find_element_by_xpath("XXXX")
        对页面的每一步操作都用一个方法封装
        也可以对一个操作功能进行封装
        为了引用该类的时候调用到类里面的变量，可以给变量加_不会被看到
    """

    # 注意要跳登录页，首先判断是否登录
    def gotoLogin(self) -> LoginPage:
        self.find(By.ID,"btn_login").click()
        return LoginPage()

    # ================首先判断个人页是否已登录
    def is_login_app(self):  # tv_nick_name 判断该控件是否存在即可
        element = self.driver.find_elements(By.ID, "tv_nick_name")  # 只有elements的找不到元素才是为[] 其他报错
        # self.screenshots()  # 操作页面进行截图
        # if element.__sizeof__()>0:      # 判断昵称元素是否存在，大于0就是存在已登录，否则就是未登录
        if element != []:  # 判断昵称元素是否存在，大于0就是存在已登录，否则就是未登录
            return "logged"  # 已登录
        else:
            return "not logged"  # 未登录

    def back_profile(self):
        self.find(By.ID, "iv_base_left").click()
        return self

    # ================登录的，可退出登录测试
    def logout_app(self):
        time.sleep(2)
        self.loadSteps("data/hys.yaml", "logout_app")
        self.screenshots()  # 操作页面进行截图
        return self

    # ================登录后的================点击各项跳转测试
    # 1.点头像
    def click_avatar(self):
        self.find(By.ID,"iv_mine_head").click()
        text = self.find(By.ID,"tv_username").text
        self.screenshots()          # 操作页面进行截图
        self.find(By.ID,"iv_base_left").click()
        return text

    # 2.点充值
    def click_recharge(self):
        balance1 = str(self.find(By.ID, "tv_balance").text) + '元'
        self.find(By.ID, "tv_recharge").click()
        balance2 = self.find(By.ID, "tv_blance").text
        self.screenshots()          # 操作页面进行截图
        self.find(By.ID, "iv_base_left").click()
        if balance2 == balance1:
            return True
        else:
            return False

    # 3.点我的订单
    def click_myorder(self):
        self.find(By.ID,"ll_my_orders").click()
        length = len(self.driver.find_elements(By.ID,"tv_pharmacy_name"))
        self.screenshots()          # 操作页面进行截图
        self.find(By.ID,"iv_base_left").click()
        if length>0:
            return True
        else:
            return False

    # 4.点待付款
    def click_payment(self):
        self.find(By.ID,"ll_my_pending_pay").click()
        length = len(self.driver.find_elements(By.ID, "tv_pharmacy_name"))
        self.screenshots()          # 操作页面进行截图
        if length>0:
            self.cancel_order()
        self.find(By.ID,"iv_base_left").click()
        if length>0:
            return False
        else:
            return True

    def cancel_order(self):
        self.loadSteps('data/profile.yaml','cancel_order')
        # self.find(By.ID,'bt_cancel').click()
        # self.find(By.ID, 'iv_check').click()
        # self.find(By.ID, 'bt_sure').click()

        # cel3 = self.driver.find_elements(By.ID,"bt_cancel")[0].click()

        self.screenshots()
        return self

    # 5.点我的需求
    def click_needs(self):
        self.find(By.ID,"myRequireView").click()
        length = len(self.driver.find_elements(By.ID,"ll_item_goods"))
        self.screenshots()  # 操作页面进行截图
        self.find(By.ID, "iv_base_left").click()
        if length > 0:
            return True
        else:
            return False

    # 6.点我的优惠券
    def click_mycoupon(self):
        self.find(By.ID,"ll_coupon").click()
        length = len(self.driver.find_elements(By.ID, "fl_get_coupon"))
        self.screenshots()  # 操作页面进行截图
        self.find(By.ID, "iv_back").click()
        if length > 0:
            return True
        else:
            return False

    # 7.点地址管理
    def click_manager_address(self):
        self.find(By.ID, "ll_address").click()
        length = len(self.driver.find_elements(By.ID, "ll_item_above"))
        self.screenshots()  # 操作页面进行截图
        self.find(By.ID, "iv_base_left").click()
        if length > 0:
            return True
        else:
            return False

    # 8.点我的收藏
    def click_mycollection(self):
        self.find(By.ID, "ll_collection").click()
        length = len(self.driver.find_elements(By.ID, "ll_item_foreground"))
        self.screenshots()  # 操作页面进行截图
        self.find(By.ID, "iv_base_left").click()
        if length > 0:
            return True
        else:
            return False

    # 9.点会员中心
    def click_members(self):
        tv_point = self.find(By.ID,"tv_point").text
        self.find(By.ID, "ll_member").click()
        points = self.find(By.ID,"myPoints2").text
        self.screenshots()  # 操作页面进行截图
        self.find(By.ID, "iv_web_back").click()
        if points == tv_point:
            return True
        else:
            return False