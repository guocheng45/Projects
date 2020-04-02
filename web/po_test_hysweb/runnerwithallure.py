# coding=utf-8
import pytest
import shutil
import allure
import logging
import subprocess

fileHander = logging.FileHandler(filename="log/uiautotest.log", encoding="utf-8")
logging.basicConfig(level=logging.INFO)         # log的输出级别
logging.getLogger().setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHander.setFormatter(formatter)
logging.getLogger().addHandler(fileHander)


if __name__ == '__main__':
    shutil.rmtree('log/report/', ignore_errors=True)  # 表示递归删除文件夹下的所有文件夹和子文件,删除包括report文件夹本身

    # pytest.main(['--alluredir', '../log/report/xml', 'testcases/alluredemo/login/test_hys.py::TestLogin::test_2474609'])
    # pytest.main(['--alluredir', '../log/report/xml','--allure-severities=blocker', 'testcases/alluredemo/'])

    pytest.main(['--alluredir', 'log/report/xml', 'testcases/'])
    # 通过subprocess.getstatusoutput 获得shell返回结果
    print(subprocess.getstatusoutput('allure generate --clean log/report/xml -o log/report/html'))
