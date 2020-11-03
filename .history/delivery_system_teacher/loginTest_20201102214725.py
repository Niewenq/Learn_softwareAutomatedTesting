# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   loginTest.py
# @Time    :   2020/11/02 21:13:35


# 登录接口
import hashlib
import requests
fiddler_proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

# md5加密


def get_md5(psw):
    md5 = hashlib.md5()  # 实例化对象
    md5.update(psw.encode('utf-8'))  # 加密操作
    return md5.hexdigest()


print('md5--->', get_md5('123456'))


def login(inData, getToken=True):
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
    # !   方法二：使用抓包工具，但是抓包工具需要代理，所以需要设置

    # resp = requests.post(url, params=payload, proxies=fiddler_proxies)

    # resp = requests.post(url, data=payload)

    # print(resp.headers)#响应头
    # 获取响应--是一个字典  resp.json()#  返回是字典
    # if getToken:
    #     return resp.json()['data']['token']
    # else:
    #     return resp.json()

    # print(resp.json()['data']['token'])


login({'username': 'sq0001', 'password': '123456'})
