#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/9 10:44
# @Author     : Wenqing Nie
# @File       : basePage.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from learn_a_po_pattern.ultimate_edition.utils.getDriver import Driver
from learn_a_po_pattern.ultimate_edition.config import configs


class BasePage:
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver()

    def find_element_explicit_wait(self, locator, time_out=configs.timeOut, poll_frequency=configs.pollFrequency):
        return WebDriverWait(driver=self.driver, timeout=time_out, poll_frequency=poll_frequency).until(
            method=ec.visibility_of_element_located(locator=locator))

    def find_elements_explicit_wait(self, locator, time_out=configs.timeOut, poll_frequency=configs.pollFrequency):
        return WebDriverWait(driver=self.driver, timeout=time_out, poll_frequency=poll_frequency).until(
            method=ec.visibility_of_all_elements_located(locator=locator))

    def to_page(self):
        pass
