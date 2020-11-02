# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   selenium_1_homework.py
# @Time    :   2020/11/02 15:04:57

"""
selenium第一次作业：
    1.访问：https://m.weibo.cn/
    2.点击：大家都在搜
    3.点击：微博热搜榜
    4.找到：实时热点，每分钟更新一次新闻列表
    5.将其中带有热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种
"""
# here put the import lib
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import re


def find_element_explicit_wait(driver, locator, timeout=5, poll_frequency=0.5, method=ec.visibility_of_element_located):
    return WebDriverWait(driver=driver, timeout=timeout, poll_frequency=poll_frequency).until(
        method=method(locator=locator))


def selenium_run():
    # 1、设置开始时间
    start_time = time.time()
    # 2、获取driver对象
    driver = webdriver.Chrome(executable_path=r'D:\webdrivers\chromedriver.exe')
    # 3、访问网站
    driver.get(url='https://m.weibo.cn/')
    # 4、点击搜索框
    find_element_explicit_wait(driver=driver, locator=(By.CSS_SELECTOR, '.m-search>i')).click()
    # 5、点击'热搜榜'
    find_element_explicit_wait(driver=driver,
                               locator=(By.CSS_SELECTOR, 'div[class~="m-col-2"]>div>div>div:nth-child(8)')).click()
    # 6、获取所有实时热点
    eles = find_element_explicit_wait(driver=driver, locator=(
        By.CSS_SELECTOR, '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)>div>div>div'),
                                      method=ec.visibility_of_all_elements_located)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 7、过滤掉普通的热点
    for ele in eles:
        try:
            img = ele.find_element_by_class_name('m-link-icon')
        except NoSuchElementException:
            continue
        news_title = ele.find_element_by_class_name('main-text').text
        flow_type = re.match(pattern='.+(fei|hot|new)',
                             string=img.find_element_by_tag_name('img').get_attribute('src'))
        if flow_type is not None:
            print(flow_type.group(1) + '\t' + news_title)


if __name__ == '__main__':
    selenium_run()