#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/5 21:52
# @Author     : Wenqing Nie
# @File       : configs.py
# @Description: 配置文件
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

# 网址
URL = "http://127.0.0.1:8088/login"

# 测试用户，用户名
username = "libai"
# 测试用户，密码
passwd = "opmsopms123"

# 最大超时时间
time_out = 10
# 轮询时间
poll_frequency = 0.5

# driver 路径
driverPath = {
    "Chrome": r"D:\webdrivers\chromedriver.exe",
    "Firefox": r"D:\webdrivers\geckodriver.exe"
}
