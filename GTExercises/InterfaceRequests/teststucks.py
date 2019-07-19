import json

import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from GTExercises.XmlReader import xmlreader_elementree

#测试官网商品的库存
#post
#https://uat-kong.ehaoyao.com/auth/v1/oauth2/token?grant_type=client_credentials&client_id=29f666537d7f4b7188529ee57fcfd7f9&client_secret=3fc5e170716d4dea95e7bdf43b726039&scope=hys

#get
#https://uat-kong.ehaoyao.com/stock/v1.1/stocks/16612,123276,230,3150?access_token={{access_token1}}

def requests_post(url,params):
    try:
        req = requests.post(url, params)
        json_response = json.loads(req.text)
        if req.status_code == 200:
            return json_response
        else:
            return False
    except ReadTimeout:
        print('Timeout!')
    except ConnectionError:
        print('Connection error!')
    except RequestException:
        print('RequestException Error!')

def requests_get(url,params):
    try:
        req = requests.get(url, params)
        json_response = json.loads(req.text)
        if req.status_code == 200:
            return json_response
        else:
            return False
    except ReadTimeout:
        print('Timeout!')
    except ConnectionError:
        print('Connection error!')
    except RequestException:
        print('RequestException Error!')

url_1 = 'https://uat-kong.ehaoyao.com/auth/v1/oauth2/token'
params = {'grant_type':'client_credentials','client_id':'29f666537d7f4b7188529ee57fcfd7f9','client_secret':'3fc5e170716d4dea95e7bdf43b726039','scope':'hys'}
json_response = requests_post(url_1,params)
node_path = './/resource[@name="getToken"]/test/write_back/filed'
if json_response is not False:
    access_token = json_response['access_token']
    print('access_token==========:', access_token)
    xmlreader_elementree.write_xml(node_path,access_token)
    url1 = 'https://uat-kong.ehaoyao.com/stock/v1.1/stocks/16612,123276,230,3150'
    params1 = {'access_token': access_token}
    json_response1 = requests_get(url1, params1)
    print('json_response1====:', json_response1)
else:
    print('json_response====:',json_response)





#print('reponses:',reponses,'\n',type(reponses))
#print(json_response) #response.json()方法同json.loads(response.text)print(type(response.json()))
#print(type(json_response))
#print('access_token==========:',access_token)


'''
import pytest
@pytest.fixture()
def login():
    print("\n 输入用户名和密码！")

def test_soso(login):
    print('denglu hou zhixing')

def test_cakan():
    print("case2 buyong denglu")

def test_cart(login):
    print('case3 denglu jiagouwuche')
'''
