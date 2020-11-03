#!/usr/bin/env python
# coding=utf-8
'''
# @Author       : Wenqing Nie
# @Date         : 2020-11-02 21:13:55
# @LastEditTime : 2020-11-03 09:56:08
# @Description  : file content
# @FilePath     : /Learn_softwareAutomatedTesting/delivery_system_teacher/cookieTest.py
'''

#1- 登录接口
import requests
def login(inData):
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'#路径
    payload = inData
    resp = requests.post(url,data=payload)#
    print(resp.text)
    #方案一：原生态cookie----如果后续的接口直接使用这个cookie,不增加其他参数--直接使用
    print(resp.cookies)
    # 方案二：如果后续的接口使用这个cookie,再增加其他参数认证，重新封装cookies
    print(resp.cookies['sessionid'])
    # print(resp.headers)#响应头

    return resp.cookies,resp.cookies['sessionid']
#方案一：
#原生态cookie
cookie1 = login({'username':'auto','password':'sdfsdfsdf'})[0]
#其他接口请求
resp = requests.post('路径',cookies = cookie1)#

# 方案二：
session= login({'username':'auto','password':'sdfsdfsdf'})[1]#sessionid值
user_cookie = {'sessionid':session,'token':'123456'}
#其他接口请求
resp = requests.post('路径',cookies = user_cookie)#

login({'username':'auto','password':'sdfsdfsdf'})
'''
data--表单数据   name=tom&age=20---  content-type就是 表单
json--json格式   直接传入字典---     content-type就是 json格式
params---参数到url里的
'''

#https协议
requests.packages.urllib3.disable_warnings()#忽略警告
import requests
def login(inData):
    url = 'https://120.55.190.222/api/mgr/loginReq'#路径
    payload = inData
    resp = requests.post(url,data=payload,verify = False)#
    print(resp.text)

login({'username':'auto','password':'sdfsdfsdf'})
