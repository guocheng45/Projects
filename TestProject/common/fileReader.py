# coding:utf-8
"""读取excel，ini配置文件"""
import configparser
import xlrd
import os
import json
import xml.etree.ElementTree as ET

"""各文件路径在这里维护"""
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'conf.ini')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_CASE_FOLDER = os.path.join(BASE_PATH, 'test')

TEST_DATA_FILE_PRE = os.path.join(BASE_PATH, r'test\resource', 'TestData_Pre.xlsx')

RESOURCE_FOLDER = os.path.join(BASE_PATH, r'test\resource')


class ExcelUtil(object):
    def __init__(self, sheet_name='supp', excel_path=TEST_DATA_FILE_PRE):
        if os.path.exists(excel_path):
            self.excel_path = excel_path
        else:
            raise FileNotFoundError(u'文件不存在！')
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    # 返回已第一行为key的字典列表
    def dict_data(self):
        """返回第一行为key的字典"""
        if self.rowNum <= 1:
            print(u"总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

    # 根据第一列，也就是Name的名称，找对应行的数据
    def get_values_by_name(self, name):
        all_values = self.dict_data()
        for dic in all_values:
            if dic['Name'] == name:
                return dic

    # 根据name，获取inputJson,返回字符串
    def get_inputs_by_name(self, name):
        dic = self.get_values_by_name(name)
        input_json = dic['InputJson']
        return input_json

    # 根据name，获取jsonpath，返回list
    def get_jsonpath_by_name(self, name):
        dic = self.get_values_by_name(name)
        json_path = dic['JsonPath']
        return json.loads(json_path)

    # 根据name, 获取expectedresult
    def get_expected_result_by_name(self, name):
        dic = self.get_values_by_name(name)
        expected = dic['ExpectedResult']
        return json.loads(expected)

    # 根据name,获取Method的值
    def get_method_by_name(self, name):
        dic = self.get_values_by_name(name)
        method = dic['Method']
        return method

    # 根据name, 获取包含sql编号和sql的字典
    def get_sqls_by_name(self, name):
        dic = self.get_values_by_name(name)
        sqls = dic['SQL']
        if sqls is "":
            result = {}
        else:
            result = json.loads(sqls)
        return result


class IniUtil(object):
    def __init__(self, ini_path=CONFIG_FILE):
        self.ini_path = ini_path
        # 生成config对象
        self.conf = configparser.ConfigParser()
        # 用config对象读取配置文件
        self.conf.read(self.ini_path, encoding="utf-8-sig")

    # def get_sections(self):
    #     # 以列表形式返回所有的section的名称 ['45', '46']
    #     return self.conf.sections()
    #
    # def get_options_of_section(self, section_name):
    #     # 得到指定section的所有option的名称 ['host', 'user', 'password', 'port', 'database']
    #     return self.conf.options(section_name)
    #
    # def get_kvaules_of_section(self, section_name):
    #     # 得到指定section的所有键值对
    #     return self.conf.items(section_name)

    def get_value_of_option(self, section_name, option):
        # 得到指定section，option的值
        return self.conf.get(section_name, option)

    def update_value_of_opetion(self, section_name, option, value):
        # 修改指定section，option的值
        self.conf.set(section_name, option, value)
        self.conf.write(open(self.ini_path, "w", encoding="utf-8-sig"))


class JsonUtil(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, key1,key2):
        return self.data[key1][key2]

    # 写json
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))


class XMLUtil(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = self.get_tree()
        self.root = self.tree.getroot()

    # 获取根目录
    def get_tree(self):
        tree = ET.parse(self.file_path)
        return tree

    # 根据name获取method
    def get_method(self, name):
        xpath = './/resource[@name="' + name + '"]'
        resource = self.root.find(xpath)
        method = resource.get('method')
        return method

    # 根据name获取resource.test的数据
    def get_test_element(self, name):
        """
        :param name: resource name
        :return: list[Element,Element]
        """
        xpath = './/resource[@name="' + name + '"]/test'
        print("xpath====================:",xpath)
        test = self.root.findall(xpath)
        return test

    # 获取test.input的数据
    def get_input_field(self, name, index=0):
        """
        :param name: resource name
        :param index: index in test element list
        :return:
        """
        test = self.get_test_element(name)[index]
        input_data = test.find(".input")
        return input_data.text

    # 获取test.compare(type=c1)的数据
    def get_compare_c1(self, name, index=0):
        """
        :param name:
        :param index:
        :return: value of json_path and expected
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c1']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        return json.loads(json_path.text), json.loads(expected.text)

    # 获取test.compare(type=c2)的数据
    def get_compare_c2(self, name, index=0):
        """

        :param name:
        :param index:
        :return: jsonpath, expected, sql
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c2']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        sqls = compare.findall("./sql")
        sql = {}
        for s in sqls:
            key = s.get('seq')
            sql[key] = s.text
        return json.loads(json_path.text), json.loads(expected.text), sql

    # 获取test.compare(type=c3)的数据
    def get_compare_c3(self, name, index=0):
        """

        :param name:
        :param index:
        :return: jsonpath, expected, sql
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c3']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        sqls = compare.findall("./sql")
        sql = dict()
        for s in sqls:
            key = s.get('seq')
            sql[key] = s.text
        return json.loads(json_path.text), json.loads(expected.text), sql

    # 获取test.compare(type=c4)的数据
    def get_compare_c4(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return: jsonpath, expected, sql
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c4']")
        field_name = compare.find("./fieldname")
        expected = compare.find("./expected")
        sqls = compare.findall("./sql")
        sql = dict()
        for s in sqls:
            key = s.get('seq')
            sql[key] = s.text
        return json.loads(field_name.text), json.loads(expected.text), sql

    # 获取test.compare(type=5)的数据
    def get_compare_c5(self, name, index=0):
        """

        :param name:
        :param index:
        :return: jsonpath, expected, sql
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c5']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        sqls = compare.findall("./sql")
        sql = dict()
        for s in sqls:
            key = s.get('seq')
            sql[key] = s.text
        return json.loads(json_path.text), json.loads(expected.text), sql

    # 获取test.compare(type=c6)的数据
    def get_compare_c6(self, name, index=0):
        """
        :param name:
        :param index:
        :return: value of json_path and expected
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c6']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        return json.loads(json_path.text), json.loads(expected.text)

    # 获取test.compare(type=c7)的数据
    def get_compare_c7(self, name, index=0):
        """
        :param name:
        :param index:
        :return: value of json_path and expected
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c7']")
        json_path = compare.find("./jsonPath")
        return json.loads(json_path.text)

    # 获取test.compare(type=c8)的数据
    def get_compare_c8(self, name, index=0):
        """
        :param name:
        :param index:
        :return: value of json_path and expected
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c8']")
        json_path = compare.find("./jsonPath")
        expected = compare.find("./expected")
        return json.loads(json_path.text), json.loads(expected.text)

    # 获取test.write-back的数据
    def get_write_back(self, name, index=0):
        """

        :param name: resourece name
        :param index:
        :return:
        """
        print("get_write_back========name====",name)
        test = self.get_test_element(name)[index]
        fields = test.findall(".write_back/field")
        result = []
        i = 1
        for f in fields:
            field_name = f.get('field_name')
            json_path = f.get('json_path')
            value = f.text
            value_xpath = './/resource[@name="' + name + '"]/test['+str((index+1))+']/write_back/field['+str(i)+']'
            i = i + 1
            result.append((field_name, json_path, value, value_xpath))
            print("result==============", field_name, json_path, value, value_xpath)     #没走到这一步。。。找到原因json_path写错了
        return result


    # 获取test.dependence的数据
    def get_dependence(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        dependence = test.find('./dependence')
        resource_name = dependence.get('resource_name')
        test_index = dependence.get('test_index')
        if test_index is None:
            test_index = '0'
        value = dependence.text
        return resource_name, test_index, eval(value)

    # 修改xml节点的值
    def modify_write_back(self, node_xpath, new_value):
        field = self.root.find(node_xpath)
        field.text = new_value
        self.tree.write(self.file_path, encoding='utf-8')

    # 判断test.compare(type=c1)节点是否存在
    def is_compare_c1_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c1']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c2)节点是否存在
    def is_compare_c2_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c2']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c3)节点是否存在
    def is_compare_c3_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c3']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c4)节点是否存在
    def is_compare_c4_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c4']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c5)节点是否存在
    def is_compare_c5_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c5']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c6)节点是否存在
    def is_compare_c6_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c6']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c7)节点是否存在
    def is_compare_c7_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c7']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.compare(type=c8)节点是否存在
    def is_compare_c8_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".compare[@type='c8']")
        if compare is None:
            return False
        else:
            return True

    # 判断test.write-back节点是否存在
    def is_write_back_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".write_back")
        if compare is None:
            return False
        else:
            return True

    # 判断test.dependence节点是否存在
    def is_dependence_exist(self, name, index=0):
        """

        :param name: resource name
        :param index:
        :return:
        """
        test = self.get_test_element(name)[index]
        compare = test.find(".dependence")
        if compare is None:
            return False
        else:
            return True


if __name__ == "__main__":
    xmlf = XMLUtil(r'D:\Projects\TestProject\test\resource\pre\sup.xml')
    jsonx = JsonUtil(r'D:\Projects\TestProject\test\resource\pre\sup.json')
    r = jsonx.get_data('getConfirmCodeByPhone')
    print(r)

    # print(y)
















