#!/usr/bin/env python
# coding=utf-8
'''
# @Author       : Wenqing Nie
# @Date         : 2020-11-02 21:13:55
# @LastEditTime : 2020-11-03 10:39:22
# @Description  : cookie简单操作的测试
# @FilePath     : /Learn_softwareAutomatedTesting/delivery_system_teacher/cookieTest.py
'''
import requests


def login(inData):
    '''
    # @description: 获取cookie值
    # @param {请求参数} inData
    # @return {返回cookies}
    '''
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'  # 路径
    payload = inData

    # ? 请求参数讲解
    # ! data--表单数据  name=tom&age=20 content-type是表单
    # ! json--json格式  直接传入字典    content-type是json格式
    # ! params---get请求的参数，参数添加到url中
    resp = requests.post(url, data=payload)

    # ! 方案一：原生态cookie----如果后续的接口直接使用这个cookies,不增加其他参数--直接使用
    # print(resp.cookies)
    # # 方案二：如果后续的接口使用这个cookie,再增加其他参数认证，重新封装cookies
    # print(resp.cookies['sessionid'])
    # # print(resp.headers)#响应头

    # return resp.cookies, resp.cookies['sessionid']


if __name__ == "__main__":
    login(inData={'username': 'auto', 'password': 'sdfsdfsdf'})
    # # 方案一：
    # # 原生态cookie
    # cookie1 = login({'username': 'auto', 'password': 'sdfsdfsdf'})[0]
    # # 其他接口请求
    # resp = requests.post('路径', cookies=cookie1)

    # # 方案二：
    # session = login({'username': 'auto', 'password': 'sdfsdfsdf'})[1]  # sessionid值
    # user_cookie = {'sessionid': session, 'token': '123456'}
    # # 其他接口请求
    # resp = requests.post('路径', cookies=user_cookie)

    # login({'username': 'auto', 'password': 'sdfsdfsdf'})

    # # https协议
    # requests.packages.urllib3.disable_warnings()  # 忽略警告

    # def login(inData):
    #     url = 'https://120.55.190.222/api/mgr/loginReq'  # 路径
    #     payload = inData
    #     resp = requests.post(url, data=payload, verify=False)
    #     print(resp.text)

    # login({'username': 'auto', 'password': 'sdfsdfsdf'})
