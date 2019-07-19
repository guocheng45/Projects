#coding:utf-8
import json
from jsonpath import jsonpath
from TestProject.common.database import DBOperation
from TestProject.common.fileReader import IniUtil


class CommonMethod(object):

    def __init__(self):
        pass

    # 获取测试环境的host
    def get_host(self, host_name):
        """

        :param host_name: option name under [host_test], [host_pre], [host_prod], eg: sup
        :return:
        """
        ini = IniUtil()
        test_env = ini.get_value_of_option("Env", "Env")
        section = "host_" + test_env
        host = ini.get_value_of_option(section, host_name)
        return host

    # 获取完整endpoint
    def get_endpoints(self, host_name, sys_name, resource_name):
        """

        :param host_name: option name under [host_test], [host_pre], [host_prod], eg: sup
        :param sys_name: system name, eg: sup, b2b, b2c
        :param resource_name: option name under [resource_b2b],[resource_sup], eg: login
        :return:
        """
        host = self.get_host(host_name)
        resource_section = "resource_" + sys_name
        resource = IniUtil().get_value_of_option(resource_section, resource_name)
        endpoint = host + resource
        return endpoint

    # 获取数据库连接
    def get_db_connections(self, connection_name):
        """
        connection_name也以system的名称命名，所以此参数也是sys_name
        :param connection_name: option name under [db_test], [db_pre],[db_prod], eg: sup, b2b, b2c.
        :return:
        """
        ini = IniUtil()
        test_env = ini.get_value_of_option("Env", "Env")
        section = "db_" + test_env
        con = ini.get_value_of_option(section, connection_name)
        connection = json.loads(con)
        return connection

    # 查询数据库，返回一条数据
    def search_one_from_db(self, sql, connection_name):
        """

        :param sql:
        :param connection_name: ption name under [db_test], [db_pre],[db_prod], eg: sup, b2b, b2c
        :return: dict, eg: {'sup_user_id': 48229, 'login_name': 'wumeng', 'login_pwd': '123456'}
        """
        # # 获取数据库连接
        connections = self.get_db_connections(connection_name)
        # 连接数据库
        db = DBOperation(connections)
        # 执行sql 返回结果
        rs = db.search_one(sql)
        # 关闭数据库连接
        db.close_db()
        return rs

    # 查询数据库， 返回多条数据
    def search_all_from_db(self, sql, connection_name):
        """

        :param sql:
        :param connection_name: ption name under [db_test], [db_pre],[db_prod], eg: supp_connection
        :return: dict eg:
        { "Field1" : [value1, value1,value3, value4, value5],
        "Field2" : [value1, value1,value3, value4, value5]
        }
        """
        # # 获取数据库连接
        connections = self.get_db_connections(connection_name)
        # 连接数据库
        db = DBOperation(connections)
        # 执行sql 返回结果
        rs = db.search_all(sql)
        # 转换结果
        result = self.search_all_result_to_dict(rs)
        # 关闭数据库连接
        db.close_db()
        return result

    # 更新数据（删除数据）
    def update_data(self, sql, connection_name):
        """
        用sql做更新和删除操作
        :param sql:
        :param connection_name:
        :return:
        """
        # 获取数据库连接
        connections = self.get_db_connections(connection_name)
        # 连接数据库
        db = DBOperation(connections)
        # 执行更新或delete的sql
        db.update(sql)
        db.close_db()

    # 将从数据库返回的多条数据，转化成字典格式
    def search_all_result_to_dict(self, result):
        """
        result: search_all_from_db的返回结果(或这种类型的数据)
        eg: [{'dictcode': 'CustType', 'dictitemcode': '6', 'branchid': 'STD'}, {'dictcode': 'CustType', 'dictitemcode': '8', 'branchid': 'STD'}, {'dictcode': 'CustType', 'dictitemcode': '11', 'branchid': 'STD'}, {'dictcode': 'CustType', 'dictitemcode': '24', 'branchid': 'FZ1'}, {'dictcode': 'CustType', 'dictitemcode': '25', 'branchid': 'FZ1'}, {'dictcode': 'CustType', 'dictitemcode': '30', 'branchid': 'FB8'}, {'dictcode': 'CustType', 'dictitemcode': '31', 'branchid': 'FB8'}, {'dictcode': 'CustType', 'dictitemcode': '32', 'branchid': 'FB8'}]

        将其转化成下面格式的字典：
        eg: {'dictcode': ['CustType', 'CustType', 'CustType', 'CustType', 'CustType', 'CustType', 'CustType', 'CustType'], 'dictitemcode': ['6', '8', '11', '24', '25', '30', '31', '32'], 'branchid': ['STD', 'STD', 'STD', 'FZ1', 'FZ1', 'FB8', 'FB8', 'FB8']}
        """
        r = {}
        keys = list(result[0])
        for k in keys:
            value = []
            for m in result:
                value.append(m[k])
            r[k] = value
        return r

    # 解析jsonpath,返回list
    def jsonpath_parse(self, rs, json_path):
        result = jsonpath(rs, json_path)
        return result

    # 对比列表
    def compare_list(self, list1, list2):
        """
        :param list1:
        :param list2:
        :return: 两个列表一致，返回True，否则返回False
        """
        # 将list里面的元素全部转换成字符串
        l1 = [str(i) for i in list1]
        l2 = [str(i) for i in list2]
        # 将list排序
        sorted_l1 = sorted(l1)
        sorted_l2 = sorted(l2)
        if sorted_l1 == sorted_l2:
            result = True
        else:
            result = False
        return result

    # 修改json对象的字段
    def modify_json_value(self, input_json, json_path, new_value):
        # 字段名称
        field_name = json_path.split('.')[-1]
        # 解析json path获取value
        field_value = self.jsonpath_parse(input_json, json_path)[0]
        # 字段名称和value的组合
        if isinstance(field_value, str):
            value_tobe_replace = '"' + field_name + '": ' + '"'+str(field_value) + '"'
            replace_value = '"' + field_name + '": ' + '"'+ str(new_value) + '"'
        elif isinstance(field_value, bool):
            value_tobe_replace = '"' + field_name + '": ' +str(field_value).lower()
            replace_value = '"' + field_name + '": ' + str(new_value).lower()
        else:
            value_tobe_replace = '"' + field_name + '": ' + str(field_value)
            replace_value = '"' + field_name + '": ' + str(new_value)
        # 将input_json转化成字符串
        input_str = json.dumps(input_json)
        # 将对应的值替换掉
        input_str = input_str.replace(value_tobe_replace, replace_value)
        # 将input_str转化成json
        result = json.loads(input_str)
        return result

    # 将非json格式的input转化成json
    def convert_input_to_json(self, string):
        """
        data = "{loginName=wumeng&loginPwd=123456&appVersion=2.4.2&imei=dced90296131e146&model=DUK-AL20&systemVersion=dced90296131e146}"
        将上面这种非标准的输入字符串，转化成json格式
        """
        new_str = string.replace("&", '","').replace("=", '":"').replace('{', '{"').replace('}', '"}')
        return new_str


if __name__ == "__main__":
    cm = CommonMethod()
    # sql = 'delete from tb_sup_multi_account_bind where login_name="wumeng" and imei = "b4d26f719c6883c0"'
    # cm.update_data(sql, 'sup')
    string ='{pageSize=30&startTime=2018-08-22&endTime=2018-08-28&page=1&orderState=1&appVersion=3.0.1&imei=dced90296131e146&model=DUK-AL20&systemVersion=dced90296131e146}'
    print(cm.convert_input_to_json(string))



