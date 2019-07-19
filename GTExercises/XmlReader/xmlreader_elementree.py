# coding=utf-8
import xml.etree.ElementTree as ET
import json

'''
# 简单遍历
tree = ET.parse("b2c.xml")
root = tree.getroot()   # 把root作为一个解析树，root作为根节点

test = root.findall('.//resource[@name="getToken"]/test')
print("test:",test)

test = root('getToken')[0]
input_data = test.find(".input")
print("input_data.text",input_data.text)'''
'''
#print(root.tag, ":" , root.attrib)     # 打印根元素的tag和属性值   data : {}

# 遍历xml文档的第二层
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag, ":" ,child.attrib)     # country : {'name': 'Liechtenstein'}
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, ":" ,children.attrib)   # rank : {'updated': 'yes'}

#访问根节点下第一个country的第二个节点year,获取对应的文本
year = root[0][1].text    # 2008

def get_test_element(self, name):
    """
    :param name: resource name
    :return: list[Element,Element]
    """
    xpath = './/resource[@name="' + name + '"]/test'
    test = self.root.findall(xpath)
    print("test==================", test)
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

 def __init__(self, file_path):
        self.file_path = file_path
        self.tree = self.get_tree()
        self.root = self.tree.getroot()

    # 获取根目录
    def get_tree(self):
        tree = ET.parse(self.file_path)
        return tree
'''
#读取B2C文件的数据
xpath = './/resource[@name="getToken"]/test'
xpath2 = './/resource[@name="testPass"]/test'
file_path = "D:/Projects/GTExercises/XmlReader/b2c.xml"
def get_tree():

    tree = ET.parse(file_path)
    return tree
def get_root():
    tree = get_tree()
    root = tree.getroot()  # 把root作为一个解析树，root作为根节点
    return root


#设置B2C文件的数据————从原文档中摘出修改B2C文件的语句，进行验证
# 根据name获取method接口的方法（get/post）—可用
def get_method(xpath1):
    xpath1 = './/resource[@name="getToken"]'
    root = get_root()
    resource = root.find(xpath1)
    method = resource.get('method')
    print('xmethod:', method)
    return method




# 获取test.input中的数据
def get_input(xpath,index=0):
    root = get_root()
    findalltest = root.findall(xpath)
    print('findalltest:', findalltest)
    test_index = findalltest[0]  # 定位至第一个test节点
    input_data = test_index.find(".input")  # 找到test节点下的input
    input_text = input_data.text  # 获取input节点的文本信息
    print('input_text:', input_text)
    return input_text



#！！！！需要尝试
# 获取test.compare(type=c1)的数据             ******用这种方式读取下一节点   上级节点.find(".下级节点[@节点名称='c1']")
def get_compare(xpath):
    xpath = './/resource[@name="getToken"]/test/compare[@type="c1"]'
    root = get_root()
    compare = root.find(xpath)   # ".compare[@type='c1']"
    json_path = compare.find("./jsonpath")
    expected = compare.find("./expected")
    return json_path,expected
    print('json.loads(json_path.text), json.loads(expected.text):',json.loads(json_path.text), json.loads(expected.text))
    # ['$.code', '$.smg'] ['1', 'success']




# 获取test.dependence的数据
def get_dependence(xpath2):
    root = get_root()
    findalltest3 = root.findall(xpath2)
    test_index3 = findalltest3[0]
    dependence = test_index3.find('./dependence')
    resource_name = dependence.get('resource_name')
    test_indexs = dependence.get('test_index')
    if test_indexs is None:
        test_indexs = '0'
    dependence_value = dependence.text
    return resource_name,test_indexs,eval(dependence_value)
    print('resource_name:=====', resource_name, ' test_indexs:=====', test_indexs, 'eval(value):=====',
          eval(dependence_value))
    from_dependence_value = dependence.text
    print('from_dependence_value:====', from_dependence_value)
    # resource_name:===== getToken  test_indexs:===== 0 eval(value):===== {'access_token': '$.access_token'}


#修改xml节点的值
def write_xml(node_path,new_value):
    #node_path = './/resource[@name="getToken"]/test/write_back/filed'  # 声明要修改节点的路径          此为一步到位找法
    #new_value = "352c31cf60c7497caf75a04d0136f3b6"  # 声明要修改的新值
    root = get_root()
    update_field = root.find(node_path)
    update_field.text = new_value  # 给其文本部分赋值
    #file_path = "b2c.xml"
    tree = get_tree()
    tree.write(file_path, encoding='utf-8')  # 猜测应该是给tree文件写数据需要用到，以何种编码格式写入文件
    new_field_value = update_field.text
    print('new_field_value:====', new_field_value)

def quckget_dependence():
    xpath = './/resource[@name="testPass"]/test/dependence'
    root = get_root()
    quckget_dependence = root.find(xpath)
    quckget_dependence_value = quckget_dependence.text
    return quckget_dependence_value
    print('quckget_dependence_value:====', quckget_dependence_value)

# 获取test.write-back的数据              此为一节一节的找法！！！
def get_write_back():
    root = get_root()
    findalltest = root.findall(xpath)
    print('findalltest:', findalltest)
    test_index = findalltest[0]  # 定位至第一个test节点
    write_back_field = test_index.findall(".write_back/filed")
    result = []
    values = 0
    i = 1
    for field in write_back_field:
        field_name = field.get("filed_name")
        json_path1 = field.get("json_path")
        values = field.text
        value_xpath = './/resource[@name="getToken"]/test[' + str((0 + 1)) + ']/write_back/field[' + str(i) + ']'
        i = i + 1
        result.append((field_name, json_path1, values, value_xpath))
        print("result==============", field_name, json_path1, values, value_xpath)
    return values
        # access_token $.access_token ['352c31cf60c7497caf75a04d0136f3b6'] .//resource[@name="getToken"]/test[1]/write_back/field[1]
#!!!  尝试怎么使用return  2个值的
# write_back_values = get_write_back()
# print('write_back_values=========:',write_back_values)
# get_dependence1 = get_dependence(xpath2)    #这是一个元组，
# print('get_dependence1========',get_dependence1,'get_dependence1[0]:',get_dependence1[0],'get_dependence1[2]:',get_dependence1[2])
