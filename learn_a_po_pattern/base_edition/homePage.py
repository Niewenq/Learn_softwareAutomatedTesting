#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/5 20:43
# @Author     : Wenqing Nie
# @File       : homePage.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
import time

from learn_a_po_pattern.base_edition.getDriver import Driver
from learn_a_po_pattern.base_edition.loginPage import LoginPageAction


# ! selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
# * 上面报错：陈旧的元素引用
# * 当我们找到元素并赋值给变量，然后通过变量操作元素
# * 这两个步骤中间，如果发生了界面刷新，那么第二个步骤通过变量操作元素就会报错
# * 这个错误就是陈旧的元素引用，因为元素已经刷新了（即使定位表达式没有发生变化）
# * 解决方案是，当我们需要操作元素的时候，实时寻找元素并赋值给变量
class HomePage:
    def __init__(self):
        self.driver = Driver.get_driver()

        # 我的主页
        self.homeLocator = "i.fa.fa-home + span"
        # 考勤管理
        self.checkAttendanceLocator = "i.fa.fa-tasks + span"

    # 定位到我的主页元素并返回
    def home_box(self):
        return self.driver.find_element_by_css_selector(self.homeLocator)

    # 定位到考勤管理元素并返回
    def check_attendance_box(self):
        return self.driver.find_element_by_css_selector(self.checkAttendanceLocator)


class HomePageAction(HomePage):
    pass


if __name__ == '__main__':
    LoginPageAction().login()
    time.sleep(3)
    hpa = HomePageAction()
    # 点击考勤管理
    hpa.check_attendance_box().click()
    time.sleep(3)
    # 点击我的主页
    hpa.home_box().click()
    time.sleep(3)
    # 点击考勤管理
    hpa.check_attendance_box().click()
    time.sleep(3)
