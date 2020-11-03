#!/usr/bin/env python
# coding=utf-8
"""
# @Author       : Wenqing Nie
# @Date         : 2020-11-02 21:13:55
# @LastEditTime : 2020-11-03 11:04:20
# @Description  : 简单cookies获取以及HTTPS请求的发送
# @FilePath     : /Learn_softwareAutomatedTesting/delivery_system_teacher/cookieTest.py
"""

import requests



def login(inData):
    """
    # @description: 获取cookie值
    # @param {请求参数} inData
    # @return {返回cookies}
    """
    """
    # ? 1、http协议
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'  # 路径
    payload = inData

    # * 请求参数讲解
    # ! data--表单数据  name=tom&age=20 content-type是表单
    # ! json--json格式  直接传入字典    content-type是json格式
    # ! params---get请求的参数，参数添加到url中
    resp = requests.post(url, data=payload)

    # ! 方案一：原生态cookie----如果后续的接口直接使用这个cookies,不增加其他参数--直接使用
    print(resp.cookies)
    # ! 方案二：如果后续的接口使用这个cookie，再增加其他参数认证，重新封装cookies。那么就是取出自己想要的字段，然
    print(resp.cookies['sessionid'])

    return resp.cookies
    """
    
    # ? 2、HTTPS协议请求的发送
    url = 'https://120.55.190.222/api/mgr/loginReq'  # 路径
    payload = inData
    resp = requests.post(url, data=payload, verify=False)
    print(resp.text)


if __name__ == "__main__":
    login(inData={'username': 'auto', 'password': 'sdfsdfsdf'})
    

    # login({'username': 'auto', 'password': 'sdfsdfsdf'})

    # # https协议
    # requests.packages.urllib3.disable_warnings()  # 忽略警告

    # def login(inData):
    #     url = 'https://120.55.190.222/api/mgr/loginReq'  # 路径
    #     payload = inData
    #     resp = requests.post(url, data=payload, verify=False)
    #     print(resp.text)

    # login({'username': 'auto', 'password': 'sdfsdfsdf'})
