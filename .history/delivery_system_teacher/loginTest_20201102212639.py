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
    # 定义接口地址
    url = 'http://121.41.14.39:8082/account/sLogin'  # 路径
    # 得到密码参数
    # inData['password'] = get_md5(inData['password'])  # 参数
    payload = inData
    resp = requests.post(url, params=payload)

    # resp = requests.post(url, params=payload, proxies=fiddler_proxies)

    # resp = requests.post(url, data=payload)
    print(resp.text)  # 请求的返回是str类型
    # print(resp.headers)#响应头
    # 获取响应--是一个字典  resp.json()#  返回是字典
    # if getToken:
    #     return resp.json()['data']['token']
    # else:
    #     return resp.json()

    # print(resp.json()['data']['token'])


login({'username': 'sq0001', 'password': '123456'})
