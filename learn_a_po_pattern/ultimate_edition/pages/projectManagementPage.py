#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/9 11:27
# @Author     : Wenqing Nie
# @File       : projectManagementPage.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
from selenium.webdriver.common.by import By

from learn_a_po_pattern.ultimate_edition.config import configs
from learn_a_po_pattern.ultimate_edition.pages.basePage import BasePage


class ProjectManagementPage(BasePage):
    def __init__(self, path='/project/manage'):
        super(ProjectManagementPage, self).__init__()
        self.url = configs.host + path

        # 以下封装页面元素寻找方法
        # 项目状态搜索选择下拉框
        self.project_status_locator = (By.NAME, "status")
        # 项目名称搜索输入框
        self.project_name_input_locator = (By.CSS_SELECTOR, "form > input")
        # 搜索按钮
        self.search_button_locator = (By.CSS_SELECTOR, "form > button.btn-primary")
        # 新建项目按钮
        self.create_project_buuton_locator = (By.CSS_SELECTOR, "a.btn.btn-success")
        # 匹配列表当中的每一个项目名称
        self.list_of_project_name_locator = (By.CSS_SELECTOR, "tbody > tr > td:nth-child(1)")
        # 匹配列表当中的每一个项目别名
        self.list_of_project_another_name_locator = (By.CSS_SELECTOR, "tbody > tr > td:nth-child(2)")

    def to_page(self):
        """
        访问此页面的网址
        :return:
        """
        self.driver.get(self.url)

    def project_name_input_box(self):
        return self.find_element_explicit_wait(self.project_name_input_locator)

    def search_button_box(self):
        return self.find_element_explicit_wait(self.search_button_locator)

    def list_of_project_name_boxes(self):
        """匹配列表当中的每一个项目名称, 返回元素列表"""
        return self.find_elements_explicit_wait(self.list_of_project_name_locator)

    def list_of_project_another_name_boxes(self):
        return self.find_element_explicit_wait(self.list_of_project_another_name_locator)


class ProjectManagementPageAction(ProjectManagementPage):
    pass


PMPA = ProjectManagementPageAction()
