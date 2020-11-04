#!/usr/bin/env python
# coding=utf-8
"""
# @Author       : Wenqing Nie
# @Date         : 2020-11-04 10:57:47
# @LastEditTime : 2020-11-04 11:40:27
# @Description  : 测试、实验一些零散、琐碎的代码
# @FilePath     : /Learn_softwareAutomatedTesting/zzzzzz.py
"""
from selenium import webdriver
import time

# 创建浏览器驱动对象
driver = webdriver.Chrome(r"D:\webdrivers\chromedriver.exe")
# 访问网址
driver.get("https://tinypng.com/")
time.sleep(5)
driver.find_element_by_css_selector(
    css_selector="input[type='file']").send_keys(r'D:\app.png')
time.sleep(10)
driver.quit()
