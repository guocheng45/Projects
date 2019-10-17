
import os

def create_allure():
    # 生成测试报告
    allure_generate =  r'allure generate D:\A测开文件\online_proj\Projects\HomeExercises\exercisePack1\allure_result -o  ./allure --clean'
    os.system(allure_generate)


def generate_xml():
    # 生成XML文件
    # pytest 测试文件所在路径 --alluredir 生成的测试结果数据保存的目录
    generate_command = 'pytest --alluredir=resport/xml/ D:/PyTest/tests/allure/test_allure_demo.py'
    os.system(generate_command)


def generate_html():
    # 生成html文件
    # allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean
    generate_command = 'allure generate D:/PyTest/tests/allure/report/xml -o D:/PyTest/tests/allure/report/html --clean'
    os.system(generate_command)

if __name__ == '__main__':
    create_allure()