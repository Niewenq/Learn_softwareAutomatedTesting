#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/9 12:06
# @Author     : Wenqing Nie
# @File       : testProjectManagement.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
import time

import pytest

from learn_a_po_pattern.ultimate_edition.pages.projectManagementPage import PMPA


class TestProjectManagement:

    def test_search_project(self):
        # 访问页面
        PMPA.to_page()
        time.sleep(1)
        # 想要搜索的项目名称
        projectName = "作业"

        # 1 按名称去搜索项目
        PMPA.project_name_input_box().send_keys(projectName)
        # 2 点击搜索按钮
        PMPA.search_button_box().click()
        time.sleep(1)
        # 获取项目列表中的每一个项目名称
        projectEleNameSli = PMPA.list_of_project_name_boxes()
        for projectELe in projectEleNameSli:
            assert projectName in projectELe.text


if __name__ == '__main__':
    pytest.main()
