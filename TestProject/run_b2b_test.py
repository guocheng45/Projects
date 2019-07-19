from HTMLTestRunner import HTMLTestRunner
import unittest
import time
from common.mail import send_report, new_report
from common.fileReader import IniUtil
from common.fileReader import REPORT_PATH, TEST_CASE_FOLDER
import os
from common.log import Log

TEST_CASE_PATH = os.path.join(TEST_CASE_FOLDER, 'B2B')


# 用makeSuite()方法，一次性加载一个文件夹下所有测试用例到suite中
def suite():
    discover = unittest.defaultTestLoader.discover(TEST_CASE_PATH, pattern="test_01*.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    # 修改测试环境为预生产
    f = IniUtil()
    f.update_value_of_opetion("Env", "env", "test")
    env = f.get_value_of_option('Env', 'env')

    # 获取当前时间
    now_time = time.strftime('%Y%m%d%H%M')

    Log().info(u"""

        ****************************************************************************************************************
        ***********************************B2B接口自动化测试用例执行开始*********************************************
        ***********************************运行环境：%s  ***************************************************************
        ****************************************************************************************************************
        """ % env)

    # 报告名称
    filename = REPORT_PATH + '\\' + now_time + '_' + 'result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title=u'B2B接口自动化测试报告--测试', description=u'自动化测试结果如下：', verbosity=2)
    runner.run(suite())
    fp.close()

    # 报告地址
    report = new_report(REPORT_PATH)

    # 收件人列表
    to_list = f.get_value_of_option('to_list', 'to_list_sup')

    # 第三个参数可填可不填
    send_report(report, to_addr=to_list, subject=u'供应商接口自动化测试报告')
