# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   selenium_second_homework.py
# @Time    :   2020/11/02 15:00:15

"""
selenium第二次作业：
    1.访问: https://www.vmall.com/
    2.获取一级菜单下包含哪些二级菜单
    3.然后获取底部，热销单品中所有 顶部 带有 爆款字样的产品名称及价格
"""
# here put the import lib
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def find_element_explicit_wait(driver, locator, timeout=5, poll_frequency=0.5, method=ec.visibility_of_element_located):
    return WebDriverWait(driver=driver, timeout=timeout, poll_frequency=poll_frequency).until(
        method=method(locator=locator))


def selenium_run():
    # 1、获取driver对象
    driver = webdriver.Chrome(executable_path=r'D:\webdrivers\chromedriver.exe')
    # 2、访问网站
    driver.get(url='https://www.vmall.com/')
    # 3、滚动页面并强制等待一秒。因为初始页面只有很少的信息，这里可以把页面信息全部加载进来
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(1)
    # 4、使用定位获取元素category-list
    eles = find_element_explicit_wait(driver=driver, locator=(By.CSS_SELECTOR, 'div.b>ol.category-list>*'),
                                      method=ec.visibility_of_all_elements_located)

    for ele in eles:
        print('一级菜单：' + ele.find_element_by_tag_name('span').text)
        for e in ele.find_elements(by=By.ID, value='child_name'):
            print('\t' + e.get_attribute('value'))
    print()
    # 5、获取热销单品中含有'爆款'
    driver.maximize_window()
    eles = driver.find_elements_by_css_selector(css_selector='.home-hot-goods li')
    for ele in eles:
        p = ele.find_elements_by_class_name('grid-tips')
        if p and '爆款' in p[0].text:
            print(p[0].text + ':' + ele.find_element_by_class_name(
                'grid-title').text + ',价格:' + ele.find_element_by_class_name('grid-price').text)


if __name__ == '__main__':
    selenium_run()
