#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/9 11:42
# @Author     : Wenqing Nie
# @File       : testPunchClockCase.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
import pytest

from learn_a_po_pattern.ultimate_edition.pages.attendanceManagePage import AMPA
import time


class TestPunchClockCase:

    def test_punch_clock(self):
        # 访问网址
        AMPA.to_page()

        # 获取打卡前的考勤表考勤记录的数量
        numBefore = len(AMPA.sign_table_tr_boxes())
        # 点击打卡按钮
        AMPA.punch_clock()
        time.sleep(1)
        # 主动刷新一下
        AMPA.driver.refresh()
        time.sleep(1)
        # 获取打卡后的考勤表考勤记录的数量
        numAfter = len(AMPA.sign_table_tr_boxes())
        assert numAfter - 1 == numBefore


if __name__ == '__main__':
    pytest.main()
