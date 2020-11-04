#!/usr/bin/env python
# coding=utf-8
"""
# @Author       : Wenqing Nie
# @Date         : 2020-11-04 16:21:56
# @LastEditTime : 2020-11-04 17:53:20
# @Description  : file content
# @FilePath     : /Learn_softwareAutomatedTesting/learn_a_pattern/get_driver.py
"""

# * 因为driver在整个流程中只需要一个而且最大化窗口只执行一次，所以driver需要单例，创建时直接调整窗口大小

from selenium import webdriver
import configs
class Driver:
    def get_driver(self, browser_name):
        driver=webdriver.Chrome(executable_path=configs.URL)
        driver.find_elements_by_css_selector(css_selector='as')
        
