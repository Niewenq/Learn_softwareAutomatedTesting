#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/9 10:29
# @Author     : Wenqing Nie
# @File       : configs.py.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

# 网址
host = "http://127.0.0.1:8088"
# 测试用户，用户名
userName = "libai"
# 测试用户，密码
password = "opmsopms123"
# 显示等待超时时间
timeOut = 10
# 显示等待轮询时间
pollFrequency = 0.5
# driver 路径
driverPath = {
    "Chrome": r"D:\tools\webdrivers\chromedriver_86.exe",
    "Firefox": r"D:\tools\webdrivers\geckodriver.exe"
}
