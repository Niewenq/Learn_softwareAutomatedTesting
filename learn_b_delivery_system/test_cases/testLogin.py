#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/8 17:42
# @Author     : Wenqing Nie
# @File       : testLogin.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

import json

from learn_b_delivery_system.tools.processExcel import read_data_from_excel, save_data_to_excel
from learn_b_delivery_system.lib.api_lib.login import Login

workBookNew, workSheetNew = save_data_to_excel(xlDir='../data/外卖系统接口测试用例-V1.2.xls', sheetName='登录模块')  # 元组
# 1- 读取数据
# 2- 关联请求
# 3- 写入xl表中
dataList = read_data_from_excel('../data/外卖系统接口测试用例-V1.2.xls', '登录模块', 2, 7)  # [(请求body，响应数据),(),()]

for one in range(len(dataList)):  # one---元组--(请求body，响应数据)
    res = Login().login(dataList[one][0], False)  # 实际响应结果
    # 预期与实际的响应数据进行比较
    if res['msg'] == json.loads(dataList[one][1])['msg']:
        print('---pass---')
        # 列表.index(元素)---求出该元素的下标
        workSheetNew.write(one + 1, 12, 'pass')  # (行号，列号，字符串内容)
    else:
        print('---fail---')
        workSheetNew.write(one + 1, 12, 'fail')
workBookNew.save('../data/res.xls')