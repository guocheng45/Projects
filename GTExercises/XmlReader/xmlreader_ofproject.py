import xml.etree.ElementTree as ET
import json
#XML用法大全
class XMLUtil(object):

    def __init__(self, file_path):
        self.file_path = file_path   #声明一个路径等于调用init的方法的文件路径
        self.tree = self.get_tree()  #声明一个树等于自己的get_tree方法
        self.root = self.tree.getroot()  #声明一个root等于根节点

    # 获取根目录
    def get_tree(self):
        tree = ET.parse(self.file_path)   #通过文件获取其根节点
        return tree

    # 根据name获取method接口的方法（get/post）—可用
    def get_method(self, name):
        xpath = './/resource[@name="' + name + '"]'
        resource = self.root.find(xpath)
        method = resource.get('method')
        return method

    # 根据name获取resource.test的数据     [<Element 'test' at 0x00000000023168B8>]
    def get_test_element(self, name):
        """
        :param name: resource name
        :return: list[Element,Element]
        """
        xpath = './/resource[@name="' + name + '"]/test'
        test = self.root.findall(xpath)
        return test

    # 获取test.input中的数据
    def get_input_field(self, name, index=0):
        """
        :param name: resource name
        :param index: index in test element list
        :return:
        """
        test = self.get_test_element(name)[index]   # getToken    test[0]
        input_data = test.find(".input")      #   在test[0]中找到.input节点
        return input_data.text     #   获取 input的text

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
            print("result==============", field_name, json_path, value, value_xpath)     #没走到这一步。。。
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
