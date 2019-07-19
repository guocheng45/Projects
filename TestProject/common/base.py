# -*- coding: utf-8 -*-
import requests
import json
import urllib.parse
from jsonpath import jsonpath
from requests_toolbelt.multipart.encoder import MultipartEncoder
from TestProject.common.fileReader import ExcelUtil
import logging


class RunMethod(object):

    def __init__(self):
        self.request = requests.Session()

    def post_main(self, url, data, timeout=15, headers=None):
        if headers is not None:
            res = self.request.post(url=url, params=data, headers=headers, timeout=timeout)
        else:
            res = self.request.post(url=url, params=data, timeout=timeout)
        return res

    def get_main(self, url, data=None, timeout=15, headers=None):
        if headers is not None:
            res = self.request.get(url, params=data, headers=headers, timeout=timeout)
        else:
            res = self.request.get(url=url, params=data, timeout=timeout)
        return res

    def run_main(self, method, url, data=None, timeout=15, headers=None):
        if method == 'Post':
            res = self.post_main(url, data, timeout, headers)
        else:
            res = self.get_main(url, data, timeout, headers)
        return res

    def get_json_and_status(self, method, url, data=None, headers=None):
        result = self.run_main(method, url, data, headers)
        return result.json(), result.status_code

    def get_headers(self, method, url, data=None, headers=None):
        result = self.run_main(method, url, data, headers)
        return result.headers

    def session_close(self):
        self.request.close()

    def post_multipart_form_data(self, url, input, opened_file):
        """
        处理Content-Type为 multipart/form-data的数据
        :param url:
        :param input:
        :param opened_file: 这里要传入的参数opened_file是指已用open()方法打开的文件
        :return:
        """

        # fields 加入要传入的文件信息
        fields = {
            'uploadFile0': ('filename', opened_file, 'multipart/form-data')
        }
        # fields 加入字典类型的数据
        fields.update(input)
        multipart_encoder = MultipartEncoder(fields=fields)

        # 将Content-Type设置为与multipart_encoder的Content-type一致
        headers = dict()
        headers['Content-Type'] = multipart_encoder.content_type
        # 发送请求
        result = self.request.post(url, data=multipart_encoder, headers=headers)
        return result.json(), result.status_code

    def post_data_in_url(self, url, input, headers=None):
        rs = self.request.post(url=url, params=input, headers=headers)
        return rs.json(), rs.status_code


if __name__ == "__main__":
    url = "http://sup.pre.yyjzt.com/mobile/salesman/mobileLogin.json"
    data = "loginName=wumeng&loginPwd=123456&appVersion=2.4.2&imei=dced90296131e146&model=DUK-AL20&systemVersion=dced90296131e146"

    data22 = "{loginName=wumeng&loginPwd=123456&appVersion=2.4.2&imei=dced90296131e146&model=DUK-AL20&systemVersion=dced90296131e146}"

    from common.common_methods import CommonMethod
    com = CommonMethod()
    data2233 = com.convert_input_to_json(data22)
    # print(data2233)

    url1 = 'http://sup.pre.yyjzt.com/mobile/salesman/searchSecondLevelCust.json'
    data2 = {"branchId": "FDG", "danwBh": "E420115104X001HA", "danwNm": "DWI35526279", "page": 1, "pageSize": 30}
    s = requests.Session()
    rs = s.post(url=url, params=data)
    print(rs.json())

    homepage = s.get(url1, params=data2)
    # print(rs.text)
    # print(homepage.text)


    data4 = {"blurCart":1,"branchId":"FDG","custId":"FDGDWI35491864","merArray":'{"editPrice":52.,"merchandiseNumber":1,"prodId":"SPH00049242","prodName":"阿莫西林胶囊","prodNo":"BAA003241D"}'}
    data44 = 'blurCart=1&branchId=FDG&custId=FDGDWI35491864&merArray={"editPrice":2.5,"merchandiseNumber":1,"prodId":"SPH00049242","prodName":"阿莫西林胶囊","prodNo":"BAA003241D"}'
    url4 = 'http://sup.pre.yyjzt.com/mobile/cart/checkNewCart.json'
    print(type(data4))
    page4 = s.get(url4, params=data4)
    print(page4.text)
    print(page4.headers)






