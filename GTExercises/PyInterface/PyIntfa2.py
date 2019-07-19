# 将python对象test转换json对象
    #test = [{"username":"测试","age":16},(2,3),1]
    #print type(test)
    #python_to_json = json.dumps(test,ensure_ascii=False)
    #print python_to_json
    #print type(python_to_json)

    # 将json对象转换成python对象
    #json_to_python = json.loads(python_to_json)
    #print json_to_python
    #print type(json_to_python)

# -*- coding: UTF-8 -*-
import json

class Print(object):
    @classmethod
    def json_dumps(cls,dict_obj):
        #将python对象test转换json对象
        return json.dumps(dict_obj,ensure_ascii=False,indent=2).encode("utf-8")

    @classmethod
    def check_rsp(cls,rsp_obj):
        if rsp_obj.ok or rsp_obj.status_code ==200:
            return True
        raise ValueError(rsp_obj)

    @classmethod
    def print_process(cls,rsp_obj):
        if cls.check_rsp(rsp_obj):
            json_data = cls.json_dumps(rsp_obj.json())
            print cls.join_content(json_data)

    @classmethod
    def join_content(cls,json_data):
        content = "{}测试过程{}\测试地址：{}\n1、请求方法：{}\n2、请求参数：{}\n3、返回值:\n{}\n{}"
        return content.format("-"*20,"-"*20,cls.api,cls.method,cls.json_dumps(cls.data),json_data)


