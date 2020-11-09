#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/7 21:57
# @Author     : Wenqing Nie
# @File       : configs.py
# @Description: 配置文件
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

# webdriver路径
driverPath = {'Chrome': r'D:\tools\webdrivers\chromedriver_86.exe'}
# 主机
HOST = '127.0.0.1:8088'
# 登陆URL地址
LOGIN_URL = '/login'
# 最长等待时间
TIME_OUT = 10
# 轮询时间
POLL_FREQUENCY = 0.5
# 用户名
USER_NAME = 'libai'
# 密码
USER_PASSWD = 'opmsopms123'
# 登陆cookies保存文件
LOGIN_COOKIES_FILE = './login_cookie.json'
