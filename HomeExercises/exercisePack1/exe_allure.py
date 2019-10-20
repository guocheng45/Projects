
import os

def create_allure():
    # 生成测试报告
    allure_generate =  r'allure generate D:\A测开文件\online_proj\Projects\HomeExercises\exercisePack1\allure_result -o  ./allure --clean'
    os.system(allure_generate)


def generate_xml():
    # 生成XML文件
    generate_filepath='report/xml'     # ./  返回到上级目录
    test_filepath='D:/Projects/HomeExercises/exercisePack1/test_allure.py'
    # pytest 测试文件所在路径 --alluredir 生成的测试结果数据保存的目录
    # pytest --alluredir=report/xml/ D:/Projects/HomeExercises/exercisePack1/test_allure.py
    generate_command = 'pytest --alluredir='+generate_filepath+' '+test_filepath
    os.system(generate_command)


def generate_html():
    # 生成html文件
    xml_path='report/xml'
    html_path='report/html'
    # allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean
    # allure generate D:/Projects/report/xml -o D:/Projects/report/html --clean
    generate_command = 'allure generate '+xml_path+' -o '+html_path+' --clean'
    os.system(generate_command)

if __name__ == '__main__':
    generate_xml()
    generate_html()