# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   selenium_fourth.py
# @Time    :   2020/11/02 10:47:39

# here put the import lib
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def find_element_explicit_wait(driver, locator, timeout=10, poll_frequency=0.5,
                               method=ec.visibility_of_element_located):
    return WebDriverWait(driver=driver, timeout=timeout, poll_frequency=poll_frequency).until(
        method=method(locator=locator))


def selenium_run():
    # 1、获取driver对象
    driver = webdriver.Chrome(executable_path=r'D:\webdrivers\chromedriver.exe')
    # 2、设置全屏
    driver.maximize_window()
    # 3、访问网站
    driver.get(url='http://localhost:8088')
    # 4、输入用户名和密码并登录
    find_element_explicit_wait(driver=driver, locator=(By.CSS_SELECTOR, '[name="username"]')).send_keys('libai')
    driver.find_element_by_css_selector(css_selector='[name="password"]').send_keys('opmsopms123')
    driver.find_element_by_css_selector(css_selector='.btn-login').submit()
    # 5、点击项目管理
    find_element_explicit_wait(driver=driver, locator=(By.CSS_SELECTOR, '.fa-book')).click()
    time.sleep(1)
    # 6、点击新项目
    find_element_explicit_wait(driver=driver, timeout=10, locator=(By.CSS_SELECTOR, '.btn.btn-success')).click()
    time.sleep(1)
    # 7、填写项目信息
    #   7.1 填写项目名称
    find_element_explicit_wait(driver=driver, timeout=10, locator=(By.CSS_SELECTOR, 'input[name="name"]')).send_keys(
        "selenium作业4")
    time.sleep(1)
    #   7.2 填写项目别名
    driver.find_element_by_css_selector(css_selector='input[name="aliasname"]').send_keys("selenium作业4")
    time.sleep(1)
    #   7.3 选择开始和结束日期
    date_ele = driver.find_element_by_css_selector(css_selector='input.form-control.dpd1')
    ActionChains(driver=driver).click(on_element=date_ele).perform()
    date_ele.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
    date_ele.send_keys("2020-12-1")
    date_ele = driver.find_element_by_css_selector(css_selector='input.form-control.dpd2')
    ActionChains(driver=driver).click(on_element=date_ele).perform()
    date_ele.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
    date_ele.send_keys("2020-12-12")
    #   7.4 添加描述
    driver.switch_to.frame(driver.find_element_by_css_selector(css_selector='.ke-edit-iframe'))
    driver.find_element_by_css_selector(css_selector='.ke-content').send_keys(
        "这是selenium第四次作业，作业要求：使用opms系统，进入项目管理，新建一个项目，添加成功即可，不需要做其他操作。")
    driver.switch_to.default_content()
    # 8、点击提交按钮
    ActionChains(driver).click(driver.find_element_by_css_selector(css_selector='.btn.btn-primary')).perform()
    # 9、点击关闭按钮
    find_element_explicit_wait(driver, (By.CSS_SELECTOR, 'button.close')).click()
    # 10、回到项目管理
    find_element_explicit_wait(driver=driver, locator=(By.CSS_SELECTOR, '.fa-book')).click()
    # # 9、退出浏览器
    time.sleep(100)
    driver.quit()


if __name__ == '__main__':
    selenium_run()