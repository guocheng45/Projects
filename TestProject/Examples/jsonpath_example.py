# -*- coding: utf-8-*-
"""
使用jsonpath解析json数据，从json文档中抽取指定的信息

安装：pip install jsonpath
"""
from jsonpath import jsonpath

resonpse = {'code':1,'data':{'flowAccount':None,'contactData':[],'branchList':[{'branchId':'FDG','isCustTypePrice':1,'supUserId':67951,'shortName':'湖北','userBranchId':141515},{'branchId':'FC5','isCustTypePrice':1,'supUserId':67951,'shortName':'十堰','userBranchId':141516},{'branchId':'FWE','isCustTypePrice':1,'supUserId':67951,'shortName':'器械','userBranchId':141517},{'branchId':'FDC','isCustTypePrice':1,'supUserId':67951,'shortName':'宜昌','userBranchId':141518}],'supplierId':'6768','supUserId':'67951','isResponsiblePerson':0,'message':'登录成功','coreSupplierName':'','deviceUnauthorized':False,'success':True,'loginName':'wumeng','innerAccountFlag':3,'isEidtOrderPrice':1,'innerErpBranchName':'湖北','reportScope':'','innerErpBranchId':'FDG'},'msg':'登录成功'}

# 获取根节点下code的值
json_path = "$.code"
code = jsonpath(resonpse, json_path)
print(code)

# 获取根节点下任意branchdid的值
json_path = "$..branchId"
# json_path = "$.data.branchList[*].branchId"
# json_path = "$..branchList[*].branchId"
branchId = jsonpath(resonpse, json_path)
print(branchId)

# 获取第一个branchList的数据
json_path = "$..branchList[0]"
branchList_1 = jsonpath(resonpse, json_path)
print(branchList_1)

# 获取branchlist的第1条数据的branchid的值
json_path = "$..branchList[0].branchId"
branchId_1 = jsonpath(resonpse, json_path)
print(branchId_1)

# 获取branclist的第2，3条数据的userBranchId
json_path = "$..branchList[1,2].userBranchId"
userBranchId_23 = jsonpath(resonpse, json_path)
print(userBranchId_23)

# 获取branchList中branchID为FDG的shortName
json_path = "$..branchList[?(@.branchId=='FDG')].shortName"
short_name = jsonpath(resonpse, json_path)
print(short_name)

