#!/usr/bin/env python
# coding=utf-8

# @Author: Wenqing Nie
# @Date: 2020-11-02 21:13:18
# @LastEditTime: 2020-11-02 22:47:13
# @Description: file content
# @FilePath: \Learn_softwareAutomatedTesting\delivery_system_teacher\loginTest.py

# 登录接口
import hashlib
import requests


# md5加密


def get_md5(psw):
    md5 = hashlib.md5()  # 实例化对象
    md5.update(psw.encode('utf-8'))  # 加密操作
    return md5.hexdigest()


'''
description: 
param {*} inData
param {*} getToken
return {*}
'''
def login(inData, getToken=True):
    """
    # * 1、参数传进来，放在params中，然后访问
    url = 'http://121.41.14.39:8082/account/sLogin'
    payload = inData
    resp = requests.post(url=url, params=payload)
    # * 2、查看响应的内容，发现得到的结果不是自己想要的，有误。
    print(resp.text)
    # ! 这时需要去分析问题，那么就需要去查看HTTP请求：url，请求头，请求体。有两种方法：
    # !   方法一：使用python打印
    print(f"url:\n{resp.request.url}")
    print(f"headers:\n{resp.request.headers}")
    print(f"body:\n{resp.request.body}")
    # !   方法二：使用抓包工具，如果抓不到说明没有走fiddler代理那么需要设置代理。同时也需要注意，使用了fiddler代理，那么fiddler应该打开，否则请求发不出去了。
    # * fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    # * resp = requests.post(url, params=payload, proxies=fiddler_proxies)
    print(resp.text)
    """

    # resp = requests.post(url, data=payload)

    # print(resp.headers)#响应头
    # 获取响应--是一个字典  resp.json()#  返回是字典
    # if getToken:
    #     return resp.json()['data']['token']
    # else:
    #     return resp.json()

    # print(resp.json()['data']['token'])


login({'username': 'sq0001', 'password': '123456'})
