#!/usr/bin/env python
# coding=utf-8
"""
# @Author       : Wenqing Nie
# @Date         : 2020-11-03 13:04:49
# @LastEditTime : 2020-11-03 20:36:41
# @Description  : file content
# @FilePath     : /Learn_softwareAutomatedTesting/delivery_system_teacher/lib/api_lib/login.py
"""
import requests
import json
import hashlib
from learn_b_delivery_system.configs.config import HOST


def get_md5(psw):
    """
    # @description:获得字符串MD5加密32位小写
    # @param {输入的字符串} psw
    # @return {返回32位小写MD5加密}
    """
    md5 = hashlib.md5()  # 实例化对象
    md5.update(psw.encode('utf-8'))  # 加密操作
    return md5.hexdigest()


class Login:
    @staticmethod
    def login(inData, getToken=True):  # 实例方法---可以直接接收json字符串
        """
        # @description: 登录类的登录函数
        # @param {*} inData
        # @param {*} getToken
        # @return {*}
        """
        url = f'{HOST}/account/sLogin'  # 路径
        payload = json.loads(inData)  # 字符串---转化---字典
        payload['password'] = get_md5(payload['password'])
        resp = requests.post(url, data=payload)
        if getToken:  # 获取token模式
            return resp.json()['data']['token']
        else:  # 获取响应数据--返回值是---字典格式
            return resp.json()


if __name__ == '__main__':
    print(Login().login('{"username":"sq0106","password":"n4jz4pdhx4"}'))
