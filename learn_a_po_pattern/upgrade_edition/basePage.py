#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/5 21:50
# @Author     : Wenqing Nie
# @File       : basePage.py
# @Description: 从各个页面抽取出共同的信息建立一个类
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

from learn_a_po_pattern.upgrade_edition.configs import time_out, poll_frequency
from learn_a_po_pattern.upgrade_edition.getDriver import Driver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver()

    @staticmethod
    def find_element_explicit_wait(driver, locator, time_out=time_out, poll_frequency=poll_frequency,
                                   method=ec.visibility_of_element_located):
        return WebDriverWait(driver=driver, time_out=time_out, poll_frequency=poll_frequency).until(
            method=method(locator=locator))


if __name__ == '__main__':
    bp = BasePage()
