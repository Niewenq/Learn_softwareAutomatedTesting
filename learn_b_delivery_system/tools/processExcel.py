#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/8 16:44
# @Author     : Wenqing Nie
# @File       : processExcel.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
import xlrd
from xlutils.copy import copy


def read_data_from_excel(xlDir, sheetName, startRow, endRow):
    resList = []
    # 1-excel表路径
    # 2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(xlDir, formatting_info=True)
    # workSheetNames = workBook.sheet_names()#获取所有的表名
    # print(workSheetNames)
    # 3- 获取某一个指定的表
    workSheet = workBook.sheet_by_name(sheetName)
    # 4- 读取单元格---返回是字符串---cell(行号，列号)  从0开始
    for one in range(startRow - 1, endRow):
        reqBodyData = workSheet.cell(one, 9).value  # 请求body
        respData = workSheet.cell(one, 11).value  # 响应数据
        resList.append((reqBodyData, respData))  # 封装一个列表里嵌套元组
    return resList


def save_data_to_excel(xlDir, sheetName):
    workBook = xlrd.open_workbook(xlDir, formatting_info=True)
    workBookNew = copy(workBook)  # 复制一个新excel文件对象
    workSheetNew = workBookNew.get_sheet(workBook.sheet_names().index(sheetName))  # 取复制出来的新excel文件对象的第一个子表
    return workBookNew, workSheetNew  # 复制出来的excel对象，复制出来excel对象的第一个子表


if __name__ == '__main__':
    # for row in read_data_from_excel('../data/外卖系统接口测试用例-V1.2.xls', '登录模块', 2, 7):
    #     print(row)

    save_data_to_excel('../data/外卖系统接口测试用例-V1.2.xls', '登录模块')