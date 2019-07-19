# coding:utf-8
import json
from TestProject.common.fileReader import IniUtil,RESOURCE_FOLDER
from TestProject.common.fileReader import JsonUtil, XMLUtil
from decimal import Decimal
from TestProject.common.common_methods import CommonMethod
import os
from TestProject.common.base import RunMethod
from TestProject.common.log import Log


class DataOperation(object):

    def __init__(self, sys_name):
        """
        :param sys_name: sup, b2b, b2c...resource文件夹中xml，json文件均以此系统名称命名

        """
        self.name = sys_name
        self.xml_file_path = self.get_xml_path()
        self.json_file_path = self.get_json_path()
        self.json = JsonUtil(self.json_file_path)
        self.xml = XMLUtil(self.xml_file_path)
        self.run = RunMethod()

    # 获取xml文件的地址
    def get_xml_path(self):
        """
        获取xml文件的路径
        """
        ini = IniUtil()
        # 从ini文件获取当前要测试的环境
        test_env = ini.get_value_of_option("Env", "Env")
        # xml文件的名称
        file_name = self.name + ".xml"
        file_path = os.path.join(RESOURCE_FOLDER, test_env, file_name)
        return file_path

    # 获取json文件的地址
    def get_json_path(self):
        """
        获取json文件的路径
        """
        ini = IniUtil()
        # 从ini文件获取当前要测试的环境
        test_env = ini.get_value_of_option("Env", "Env")
        # json文件的名称
        file_name = self.name + ".json"
        file_path = os.path.join(RESOURCE_FOLDER, test_env, file_name)
        return file_path

    # *****************************========input========************************************* #

    # 获取input json的内容
    def get_input(self, resource_name, index=0):
        """根据input的值，去json文件获取对应的输入数据"""
        # xml文件中input节点的值
        input_field = self.xml.get_input_field(resource_name, index)   #在XML文件找到需要的参数input_field resource_name ==getToken
        # 根据input节点的值，在json文件找到对应的json
        input_json = self.json.get_data(resource_name, input_field)  #input_field==client_id  需要补 key1 gettoken
        return input_json

    # *****************************========c1========**************************************** #

    # 解析c1的json path，获取实际结果，返回数据类型为字典
    def get_actual_list_c1(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: {'code': [1], 'msg': ['Testing'], 'branchId':['FDG','FDG,'FDG']}
        """
        # 从xml文件拿到实际结果的json path 列表
        json_path_list = self.xml.get_compare_c1(resource_name, index)[0]
        # 定义一个空字典，用来存实际结果，key为字段名，value为该字段在返回的response中的值
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名
            field_name = path.split('.')[-1]
            # 值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名和值加入result字典中
            result[field_name] = value
        return result

    # 获取c1的期望结果列表，返回数据类型为列表
    def get_expected_list_c1(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: [1, 'Testing', true]
        """
        # 从xml文件拿到的期望结果列表
        expected_list = self.xml.get_compare_c1(resource_name, index)[1]
        return expected_list

    # 比较c1的实际结果和期望结果，返回元祖（True/False,msg），True代表对比数据一致。
    def get_compare_result_c1(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
            Pass --> (True, '')
            Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'； 字段：'branchId'在返回的Response中不存在； ")
        """
        # 实际结果
        actual_list = self.get_actual_list_c1(resource_name, json_response, index)
        # 期望结果
        expected_list = self.get_expected_list_c1(resource_name, index)
        length = len(actual_list)
        # 先将result设置为true，一旦有一个字段比较结果不一致，则将其设置为False
        result = True
        msg = ''
        # 循环对比每一个字段的值
        for i in range(length):
            # 用来存储该字段的实际值列表中与期望值不一致的值（实际值是个列表，可能包含一个或多个元素）
            fields = ''
            # 实际结果的字段名（list）和对应的值（list）
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                # 循环实际结果列表，跟对应的期望结果对比，若不等，设置result为False，并添加msg
                for item in actual_result:
                    if expected_list[i] != item:
                        result = False
                        fields = fields + '；' + str(item)
                # 如果fields字符串的长度大于0，代表该字段的实际值列表中，有值与期望结果不一致
                if len(fields) > 0:
                    fields = fields.lstrip("；")
                    msg = msg + u"字段：'%s'的实际结果：'%s'不等于期望结果：'%s'； " % (field_name, fields, expected_list[i])
        return result, msg

    # *****************************========c2========**************************************** #

    # 解析c2的json path，获取实际结果列表，返回数据类型为字典
    def get_actual_list_c2(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: {'code': [1], 'msg': ['Testing'], 'branchId':['FDG','FDG,'FDG']}
        """
        # 从xml文件拿到实际结果的json path 列表
        json_path_list = self.xml.get_compare_c2(resource_name, index)[0]
        # 定义一个空字典，用来存实际结果，key为字段名，value为该字段在返回的response中的值
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名
            field_name = path.split('.')[-1]
            # 值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名和值加入字典result
            result[field_name] = value
        return result

    # 获取c2的期望结果
    def get_expected_list_c2(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: [1, 'Testing', false]
        """
        # 获取XML中的expected列表
        expected_list = self.xml.get_compare_c2(resource_name, index)[1]
        # 获取XML中的SQL列表
        sql_list = self.xml.get_compare_c2(resource_name, index)[2]
        com = CommonMethod()
        sql_result = {}
        # 执行sql,得到结果集，结果集类型为列表，每个元素为字典
        for e in sql_list.items():
            key = e[0]
            sql = e[1]
            result = com.search_one_from_db(sql, self.name)
            sql_result[key] = result
        # 获取最终各期望结果的值，类型为列表，每个元素为每个字段对应的值
        result = []
        for item in expected_list:
            k = item.split(':')[0]
            field_name = item.split(':')[1]
            value = sql_result[k][field_name]
            # 如果是浮点型，需要做数据处理,去掉小数点后面多余的0
            if isinstance(value, (Decimal, float,int)):
                value = [str(value), int(value)][int(value) == value]
            result.append(value)
        return result

    # 比较c2的实际结果和期望结果
    def get_compare_result_c2(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
                Pass --> (True, '')
                Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'； 字段：'branchId'在返回的Response中不存在;")
        """

        # 实际结果
        actual_list = self.get_actual_list_c2(resource_name, json_response, index)
        # 期望结果
        expected_list = self.get_expected_list_c2(resource_name, index)
        length = len(actual_list)
        # 先将result设置为true，一旦有一个字段比较结果不一致，则将其设置为False
        result = True
        msg = ''
        # 循环对比每一个字段的值
        for i in range(length):
            # 用来存储该字段的实际值列表中与期望值不一致的值（实际值是个列表，可能包含一个或多个元素）
            fields = ''
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                # 循环实际结果列表，跟对应的期望结果对比，若不等，设置result为False，并添加msg
                for item in actual_result:
                    # 由于数据库和返回结果的数据类型可能不一致，需要将实际结果和期望结果都转换成字符串，再做比较
                    if str(expected_list[i]) != str(item):
                        result = False
                        fields = fields + '；' + str(item)
                # 如果fields字符串的长度大于0，代表该字段的实际值列表中，有值与期望结果不一致
                if len(fields) > 0:
                    fields = fields.lstrip("；")
                    msg = msg + u"字段：'%s'的实际结果：'%s'不等于期望结果：'%s'； " % (field_name, fields, expected_list[i])
        return result, msg

    # *****************************========c3========**************************************** #

    # 解析c3的json path，获取实际结果列表
    def get_actual_list_c3(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: [['a','b','c'],[1,2,3,],[true,false,true]]
        """
        # 从xml文件拿到实际结果的json path 列表
        json_path_list = self.xml.get_compare_c3(resource_name, index)[0]
        # 定义一个空字典，用来存实际结果，key为字段名，value为该字段在返回的response中的值
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名
            field_name = path.split('.')[-1]
            # 值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名和值加入字典result
            result[field_name] = value
        return result

    # 获取c3的期望结果
    def get_expected_list_c3(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: {'result': [true, false, true], 'amount': [315, 317, 2802], 'branchId': ['STD', 'FDG', 'FZ1']}
        """
        # 获取XML中的expected列表
        expected_list = self.xml.get_compare_c3(resource_name, index)[1]
        # 获取XML中的SQL列表
        sql_list = self.xml.get_compare_c3(resource_name, index)[2]
        com = CommonMethod()
        sql_result = {}
        # 执行sql,得到结果集
        for e in sql_list.items():
            key = e[0]
            sql = e[1]
            result = com.search_all_from_db(sql, self.name)
            sql_result[key] = result
        # 获取最终各期望结果的值，类型为列表，元素也是列表，每个列表是对应的字段的值
        result = []
        for item in expected_list:
            k = item.split(':')[0]
            field_name = item.split(':')[1]
            value = sql_result[k][field_name]
            result.append(value)
        return result

    # 比较c3的实际结果和期望结果
    def get_compare_result_c3(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
                Pass --> (True, '')
                Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'； 字段：'branchId'在返回的Response中不存在;")
        """
        # 实际结果
        actual_list = self.get_actual_list_c3(resource_name, json_response, index)
        # 期望结果
        expected_list = self.get_expected_list_c3(resource_name, index)
        com = CommonMethod()
        result = True
        msg = ''
        # 循环对比每一个字段的值
        for i in range(len(actual_list)):
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                # 循环对比每个字段的值
                if com.compare_list(actual_result, expected_list[i]) is False:
                    result = False
                    msg = msg + "字段：'%s'的实际结果列表：%s与期望列表：%s不一致；" % (field_name, actual_result, expected_list[i])
        return result, msg

    # *****************************========c4========**************************************** #

    # 执行c4的sql，获取实际结果列表
    def get_actual_list_c4(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: {'sup_user_id': 67951, 'login_name': 'wumeng', 'user_status': 1}
        """
        # 获取XML中的field name列表
        actual_list = self.xml.get_compare_c4(resource_name, index)[0]
        # xml中sql列表
        sql_list = self.xml.get_compare_c4(resource_name, index)[2]
        com = CommonMethod()
        sql_result = {}
        # 执行sql,得到结果集
        for e in sql_list.items():
            key = e[0]
            sql = e[1]
            result = com.search_one_from_db(sql, self.name)
            sql_result[key] = result
        # 存储字典格式的实际结果
        result = dict()
        # 将查询到的结果转化成字典
        for item in actual_list:
            k = item.split(':')[0]
            # 字段名称
            field_name = item.split(':')[1]
            # 字段值
            value = sql_result[k][field_name]
            result[field_name] = value
        return result

    # 获取c4的期望结果
    def get_expected_list_c4(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: [48229, 'testing', true]
        """
        expected_list = self.xml.get_compare_c4(resource_name, index)[1]
        # result = []
        # for value in expected_list:
        #     result.append(value)
        return expected_list

    # 比较c4的实际结果和期望结果
    def get_compare_result_c4(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return:
                Pass --> (True, '')
                Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'；")
        """
        actual_list = self.get_actual_list_c4(resource_name, index)
        expected_list = self.get_expected_list_c4(resource_name, index)
        length = len(actual_list)
        result = True
        msg = ''
        for i in range(length):
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            if expected_list[i] != actual_result:
                result = False
                msg = msg + u"字段：'%s'的实际结果：'%s' 不等于期望结果：'%s'； " % (field_name,actual_result, expected_list[i] )
        return result, msg
    # *****************************========c5========**************************************** #

    # 解析c5的json path，获取实际结果列表
    def get_actual_list_c5(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:{'code': [67951], 'branchId': ['a', 'b', 'c'], 'custId': ['aa', 'bb', 'cc']}
        """
        # 从xml文件拿到实际结果的json path 列表
        json_path_list = self.xml.get_compare_c5(resource_name, index)[0]
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名称
            field_name = path.split('.')[-1]
            # 字段值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名称和值加入result
            result[field_name] = value
        return result

    # 获取c5的期望结果
    def get_expected_list_c5(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: [1, 3, 33]
        """
        # 期望结果列表
        expected_list = self.xml.get_compare_c5(resource_name, index)[1]
        # sql列表
        sql_list = self.xml.get_compare_c5(resource_name, index)[2]
        com = CommonMethod()
        sql_result = {}
        # 执行sql,得到结果集(字典)
        for e in sql_list.items():
            key = e[0]
            sql = e[1]
            result = com.search_one_from_db(sql, self.name)
            sql_result[key] = result
        # 获取最终各期望结果的值（列表）
        result = []
        for item in expected_list:
            k = item.split(':')[0]
            field_name = item.split(':')[1]
            value = sql_result[k][field_name]
            result.append(value)
        return result

    # 比较c5的实际结果和期望结果
    def get_compare_result_c5(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
                Pass --> (True, '')
                Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'； 字段：'branchId'在返回的Response中不存在;")
        """
        # 实际结果
        actual_list = self.get_actual_list_c5(resource_name, json_response, index)
        # 期望结果
        expected_list = self.get_expected_list_c5(resource_name, index)
        length = len(actual_list)
        result = True
        msg = ''
        # 循环对比每一个字段的值
        for i in range(length):
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            expected_result = expected_list[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                if expected_result != len(actual_result):
                    result = False
                    msg = msg + u"字段：'%s'的实际总数：'%s'不等于期望结果：'%s'； " % (field_name, len(actual_result), expected_result)
        return result, msg

    # *****************************========c6========**************************************** #

    # 解析c6的json path，获取实际结果列表
    def get_actual_list_c6(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: {'code': ["abc"], 'branchId': ['aa', 'ba, 'ca'], 'custId': ['aav', 'bbv', 'ccv']}
        """
        # 从xml文件拿到实际结果的json path 列表
        json_path_list = self.xml.get_compare_c6(resource_name, index)[0]
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名称
            field_name = path.split('.')[-1]
            # 字段值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名称和值加入result
            result[field_name] = value
        return result

    # 获取c6的期望结果列表
    def get_expected_list_c6(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: ["234","武汉", "wj"]
        """
        expected_list = self.xml.get_compare_c6(resource_name, index)[1]
        # result = []
        # for value in expected_list:
        #     result.append(value)
        return expected_list

    # 比较c6的实际结果和期望结果
    def get_compare_result_c6(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
            Pass --> (True, "")
            Failed --> (False, "字段：'supplierName'的实际结果：'wj供应商'不包含期望字符串：'wj1'； 字段：'code'在返回的Response中不存在； ")
        """
        # 实际结果
        actual_list = self.get_actual_list_c6(resource_name, json_response, index)
        # 期望结果
        expected_list = self.get_expected_list_c6(resource_name, index)
        length = len(actual_list)
        result = True
        msg = ''
        for i in range(length):
            fields = ''
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                # 对比实际结果列表中每个值是否都包含期望字符串
                for item in actual_result:
                    if expected_list[i] not in item:
                        result = False
                        fields = fields + '；' + str(item)
                if len(fields) > 0:
                    fields = fields.lstrip("；")
                    msg = msg + u"字段：'%s'的实际结果：'%s'不包含期望字符串：'%s'； " % (field_name, fields, expected_list[i])
        return result, msg

    # *****************************========c7========**************************************** #

    # 解析c7的json path，获取期望列表
    def get_expected_list_c7(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: {'code': [67951], 'consigneeAdd': [ 'a','b'], 'custFlag': [true]}

        """
        # 获取json path 列表
        json_path_list = self.xml.get_compare_c7(resource_name, index)
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名
            field_name = path.split('.')[-1]
            # 字段值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名称和值加入result
            result[field_name] = value
        return result

    # 判断c7的期望列表是否在返回的response中存在
    def get_compare_result_c7(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
            Pass --> (True, "")
            Failed --> (False, "返回结果中不包含字段或节点：'consigneeAdd1','custFlag1'")
        """
        # 期望结果列表
        expected_list = self.get_expected_list_c7(resource_name, json_response, index)
        result = True
        msg = ''
        fields_name = ''
        # 循环判断每个节点是否存在
        for item in expected_list.items():
            # 判断返回结果是否为False
            if isinstance(item[1], bool):
                result = False
                fields_name = fields_name + "'" + item[0] + "',"
        if len(fields_name) > 0:
            msg = msg + "返回结果中不包含字段或节点：%s" % fields_name.rstrip(',')
        return result, msg

    # *****************************========c8========**************************************** #
    # 解析c8的json path，获取实际结果列表
    def get_actual_list_c8(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return: {'code': [67951], 'consigneeAdd': [ 'a','b'], 'custFlag': [true]}
        """
        # json path 列表
        json_path_list = self.xml.get_compare_c8(resource_name, index)[0]
        result = dict()
        # 循环获取各字段的名称和值，并保存到字典result中
        for path in json_path_list:
            # 字段名
            field_name = path.split('.')[-1]
            # 字段值
            value = CommonMethod().jsonpath_parse(json_response, path)
            # 将字段名称和值加入result
            result[field_name] = value
        return result

    # 获取c8的期望结果列表
    def get_expected_list_c8(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: [1, 'Testing', true]
        """
        # 从xml文件拿到的期望结果列表
        expected_list = self.xml.get_compare_c8(resource_name, index)[1]
        # result = []
        # for value in expected_list:
        #     result.append(value)
        return expected_list

    # 比较c8的实际结果和期望结果
    def get_compare_result_c8(self, resource_name, json_response, index=0):
        """
        :param resource_name:
        :param json_response:
        :param index:
        :return:
                Pass --> (True, '')
                Failed --> (False, "字段：'code'的实际结果：'1'不等于期望结果：'11'； 字段：'branchId'在返回的Response中不存在;")
        """
        # 实际结果列表
        actual_list = self.get_actual_list_c8(resource_name, json_response, index)
        # 期望结果列表
        expected_list = self.get_expected_list_c8(resource_name, index)
        length = len(actual_list)
        result = True
        msg = ''
        for i in range(length):
            actual_result = list(actual_list.values())[i]
            field_name = list(actual_list.keys())[i]
            expected_result = expected_list[i]
            # 先判断该节点是否存在,若不存在，设置result为False，并添加msg
            if actual_result is False:
                result = False
                msg = msg + u"字段：'%s'在返回的Response中不存在； " % field_name
            else:
                if expected_result != len(actual_result):
                    result = False
                    msg = msg + u"字段：'%s'的实际总数：'%s'不等于期望结果：'%s'； " % (field_name, len(actual_result), expected_result)
        return result, msg

    # *****************************========write_back========********************************** #

    # 写入write_back各节点的值
    def write_back_values(self, resource_name, json_response, index=0):
        write_back_list = self.xml.get_write_back(resource_name, index)
        com = CommonMethod()
        for item in write_back_list:
            json_path = item[1]
            node_path = item[3]
            # 解析json path，获取response中对应的值
            value = com.jsonpath_parse(json_response, json_path)
            # print(value)
            # 将获取的值写入对应节点
            self.xml.modify_write_back(node_path, str(value))

    # 获取回写的值
    def get_write_back_values(self, resource_name, index=0):
        """
        :param resource_name:
        :param index:
        :return: {'code': '"test333"', 'consigneeAdd': '武汉市武昌区武珞路', 'custFlag': '5567'}
        """
        # 获取write back列表
        write_back_list = self.xml.get_write_back(resource_name, index)
        # 将结果以字段名- 值的方式存入字典result
        result = dict()
        for item in write_back_list:
            field_name = item[0]
            field_value = item[2]
            result[field_name] = field_value.lstrip('[').rstrip(']').lstrip("'").rstrip("'")
        return result

    # *****************************========dependence========********************************** #

    # 替换input json中的值
    def replace_input_values(self, resource_name, index=0):
        com = CommonMethod()
        dependence_list = self.xml.get_dependence(resource_name, index)
        dependence_resource = dependence_list[0]
        dependence_test_index = int(dependence_list[1])
        # 获取dependence的数据
        dependence = self.get_write_back_values(dependence_resource, dependence_test_index)
        # 获取input json
        input_json = self.get_input(resource_name, index)
        # 替换各json path对应的字段值
        for item in dependence_list[2].items():
            replace_field_name = item[0]
            json_path = item[1]
            new_value = dependence[replace_field_name]
            # 替换input json对应的值
            input_json = com.modify_json_value(input_json, json_path, new_value)
        return input_json

    # 获取response
    def get_response(self, resource_name, index=0, input_json=None, opened_file=None):
        method = self.xml.get_method(resource_name)
        com = CommonMethod()
        url = com.get_endpoints(self.name, self.name, resource_name)  #参数：sup b2c login
        Log().info("=================================%s==============================" % resource_name)
        Log().info("Url: %s" % url)
        if input_json is None:
            if self.xml.is_dependence_exist(resource_name, index):
                input_json = self.replace_input_values(resource_name, index)
            else:
                input_json = self.get_input(resource_name, index)
        Log().info("输入: %s" % input_json)
        # 获取结果
        if method == "Mul":
            response = self.run.post_multipart_form_data(url, input_json, opened_file)
        else:
            response = self.run.get_json_and_status(method, url, input_json)
            print('response====================:',response)
        return response

    # 获取最终的result
    def get_result(self, resource_name, index=0, input_json=None, opened_file=None):
        response = self.get_response(resource_name, index, input_json, opened_file)
        Log().info("输出: %s" % response[0])
        status_code = response[1]
        json_response = response[0]
        msg = ''
        result = True

        # 重新获取各种比较结果，第一个值代表该节点是否存在，第二个值代表比较结果，第二个值是msg
        # c1
        if self.xml.is_compare_c1_exist(resource_name, index):
            compare_result = self.get_compare_result_c1(resource_name, json_response, index)
            c1 = (True,) + compare_result
        else:
            c1 = (False,)

        # c2
        if self.xml.is_compare_c2_exist(resource_name, index):
            compare_result = self.get_compare_result_c2(resource_name, json_response, index)
            c2 = (True,) + compare_result
        else:
            c2 = (False,)

        # c3
        if self.xml.is_compare_c3_exist(resource_name, index):
            compare_result = self.get_compare_result_c3(resource_name, json_response, index)
            c3 = (True,) + compare_result
        else:
            c3 = (False,)

        # c4
        if self.xml.is_compare_c4_exist(resource_name, index):
            compare_result = self.get_compare_result_c4(resource_name, index)
            c4 = (True,) + compare_result
        else:
            c4 = (False,)

        # c5
        if self.xml.is_compare_c5_exist(resource_name, index):
            compare_result = self.get_compare_result_c5(resource_name, json_response, index)
            c5 = (True,) + compare_result
        else:
            c5 = (False,)

        # c6
        if self.xml.is_compare_c6_exist(resource_name, index):
            compare_result = self.get_compare_result_c6(resource_name, json_response, index)
            c6 = (True,) + compare_result
        else:
            c6 = (False,)

        # c7
        if self.xml.is_compare_c7_exist(resource_name, index):
            compare_result = self.get_compare_result_c7(resource_name, json_response, index)
            c7 = (True,) + compare_result
        else:
            c7 = (False,)

        # c8
        if self.xml.is_compare_c8_exist(resource_name, index):
            compare_result = self.get_compare_result_c8(resource_name, json_response, index)
            c8 = (True,) + compare_result
        else:
            c8 = (False,)

        # 先判断status_code，若status_code不为200，则response不需要继续检查
        if status_code != 200:
            result = False
            msg = msg + "返回Response的Status Code为%s；" % status_code
        # 检查c1的结果,若c1检查不通过，则不再继续检查
        elif c1[0] and c1[1] is False:
                result = False
                msg = msg + c1[2]
        else:
            # 检查c2的结果
            if c2[0] and c2[1] is False:
                result = False
                msg = msg + c2[2]
            # 检查c3的结果
            if c3[0] and c3[1] is False:
                result = False
                msg = msg + c3[2]
            # 检查c4的结果
            if c4[0] and c4[1] is False:
                result = False
                msg = msg + c4[2]
            # 检查c5的结果
            if c5[0] and c5[1] is False:
                result = False
                msg = msg + c5[2]
            # 检查c6的结果
            if c6[0] and c6[1] is False:
                result = False
                msg = msg + c6[2]
            # 检查c7的结果
            if c7[0] and c7[1] is False:
                result = False
                msg = msg + c7[2]
            # 检查c8的结果
            if c8[0] and c8[1] is False:
                result = False
                msg = msg + c8[2]

        # 若检查都通过，则检查是否有数据回写
        if result:
            if self.xml.is_write_back_exist(resource_name, index):
                # 回写数据
                self.write_back_values(resource_name, json_response, index)
        return result, msg

    # 关闭session，若不执行此步骤，会造成资源浪费
    def close_session(self):
        self.run.session_close()



if __name__ == "__main__":
    x = DataOperation("sup")
    # rsxx = {'code':67951,'data':{'msg':'Testing','supplierName':'wj供应商','sumIntegral':0,'linkPhone':'13116000998','cartIds':'132839,132840,132841,','totalPrice':13.2,'success':True,'count':3,'msgFlag':0,'cust':[{'branchId':'FDG','consigneeAdd':'1武汉','custId':'DWI31432092','danwNm':'1DWI31432092','custFlag':1},{'branchId':'FDG','consigneeAdd':'2武汉','custId':'DWI31432093','danwNm':'2DWI31432092','custFlag':1},{'branchId':'FDG','consigneeAdd':'3武汉','custId':'DWI31432094','danwNm':'3DWI31432092','custFlag':1}]}}
    # rs = {'code':1,'data':{'supUserId':'67951','success':True,'loginName':'wumeng',},'msg':'登录成功','userStatus':[{'status':1,'note':'a'},{'status':1,'note':'b'},{'status':1,'note':'c'}]}
    # rs1 = {'code':1,'data':{'msgFlag':0,'cust':[{'branchId':315, 				'danwNm': 'CustType', 				'custFlag': 'STD' 			}, { 				'branchId': 317, 				'danwNm': 'CustType', 				'custFlag': 'STD' 			}, { 				'branchId': 2802, 				'danwNm': 'CustType', 				'custFlag': 'STD' 			}, 			{ 				'branchId': 75370001, 				'danwNm': 'CustType', 				'custFlag': 'FB8' 			}, 			{ 				'branchId': 75380001, 				'danwNm': 'CustType', 				'custFlag': 'FB8' 			}, 			{ 				'branchId': 117590001, 				'danwNm': 'CustType', 				'custFlag': 'FB8' 			}, 			{ 				'branchId': 117600001, 				'danwNm': 'CustType', 				'custFlag': 'FZ1' 			}, 			{ 				'branchId': 117610001, 				'danwNm': 'CustType', 				'custFlag': 'FZ1' 			} 		] 	} }
    #
    # # a = x.get_actual_list_c1('testresoure1',rs)
    # # print(a)
    #
    # b = x.get_expected_list_c2('testresoure1')
    # c = x.get_actual_list_c2('testresoure1',rs)
    # print(b)
    # print(c)

    print(x.get_json_path())