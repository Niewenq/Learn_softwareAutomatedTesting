# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   selenium_third.py
# @Time    :   2020/11/02 13:39:22
"""
selenium第三次作业：
    1.登录 http://www.51job.com
    2.点击高级搜索
    3.输入搜索关键词 python
    4.地区选择 杭州
    5.职能类别 选 计算机软件 -> 高级软件工程师
    6.工作年限选 1-3 年
    7.搜索职位， 抓取页面信息。 得到如下的格式化信息
        Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
        Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
        on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
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
    driver = webdriver.Chrome(
        executable_path=r'D:\webdrivers\chromedriver.exe')
    # 2、设置全屏
    driver.maximize_window()
    # 3、访问网站
    driver.get(url='https://www.51job.com/')
    # 4、登陆51jobs
    #   4.1 点击登陆按钮
    find_element_explicit_wait(driver=driver, locator=(
        By.CSS_SELECTOR, 'p.op>a:first-child')).click()
    #   4.2 输入账户和密码
    find_element_explicit_wait(driver=driver, locator=(
        By.ID, 'loginname')).send_keys('18321239175')
    find_element_explicit_wait(driver=driver, locator=(
        By.ID, 'password')).send_keys('n4jz4pdhx4')
    #   4.3 点击登陆按钮
    find_element_explicit_wait(
        driver=driver, locator=(By.ID, 'login_btn')).submit()
    # 5、点击高级搜索
    find_element_explicit_wait(driver=driver, locator=(
        By.CSS_SELECTOR, "a.more")).click()
    # 6、输入关键字
    find_element_explicit_wait(driver=driver, locator=(
        By.ID, 'kwdselectid')).send_keys('python')
    find_element_explicit_wait(
        driver=driver, locator=(By.ID, 'KwdSearchResult'))
    ActionChains(driver).move_by_offset(xoffset=0, yoffset=0).click().perform()
    # 7、地区选择：杭州
    #   7.1 点击城市选择按钮
    driver.find_element_by_id(id_='work_position_input').click()
    time.sleep(1)

    # #   7.2 删除已选的城市
    for ele in find_element_explicit_wait(driver=driver,
                                          locator=(
                                              By.CSS_SELECTOR, "[id='work_position_click_multiple_selected'] em"),
                                          method=ec.visibility_of_all_elements_located):
        ele.click()
    time.sleep(1)
    #   7.3 找到杭州地区
    find_element_explicit_wait(driver=driver,
                               locator=(
                                   By.CSS_SELECTOR, "[id='work_position_click_center_left']>li:nth-child(4)")).click()
    for address in find_element_explicit_wait(driver=driver,
                                              locator=(
                                                  By.CSS_SELECTOR,
                                                  "[id='work_position_click_center_right_list_220200'] em"),
                                              method=ec.visibility_of_all_elements_located):
        if address.text == '杭州':
            address.click()
            break
    #   7.4 点击确认按钮保存
    driver.find_element_by_id(id_='work_position_click_bottom_save').click()
    time.sleep(1)

    # 8、职能选择：计算机软件-->高级软件工程师
    driver.find_element_by_id(id_='funtype_click').click()
    time.sleep(1)
    driver.find_element_by_id(
        id_='funtype_click_center_right_list_category_0100_0100').click()
    driver.find_element_by_id(
        id_='funtype_click_center_right_list_sub_category_each_0100_0106').click()
    driver.find_element_by_id(id_='funtype_click_bottom_save').click()
    time.sleep(1)
    # 9、选择工作年限
    driver.find_element_by_id(id_='workyear_list').click()
    time.sleep(1)
    driver.find_element_by_css_selector(css_selector="[title='1-3年']").click()
    # 10、点击搜索
    driver.find_element_by_css_selector(css_selector=".btnbox>.p_but").click()
    time.sleep(1)
    # 11、收集信息
    while True:
        # 11.1 找到当前页面的职业信息
        for job in driver.find_elements_by_css_selector(css_selector='.j_joblist>.e'):
            job_info = []
            # 11.2 鼠标移动到想要收集信息的元素
            ActionChains(driver).move_to_element(to_element=job).perform()
            # 11.3 职位名称
            job_info.append(job.find_element_by_css_selector('.jname.at').text)
            # 11.4 公司名称
            job_info.append(job.find_element_by_css_selector('.cname.at').text)
            # 11.5 地区
            job_info.append(job.find_element_by_css_selector(
                '.d.at').text.split("|")[0].strip())
            # 11.6 薪资
            job_info.append(job.find_element_by_css_selector('.sal').text)
            # 11.7 发布时间
            job_info.append(job.find_element_by_css_selector(
                '.time').text.replace("发布", ''))
            # 11.8 打印
            print('|'.join(job_info))
        # 11.9 如果下一页可以点击，那么点击，否则退出循环
        next_btn = find_element_explicit_wait(
            driver=driver, locator=(By.CSS_SELECTOR, '.next'))
        ActionChains(driver).move_to_element(to_element=next_btn).perform()
        if 'bk' not in next_btn.get_attribute('class'):
            next_btn.click()
            time.sleep(1)
        else:
            break
    # 12、退出浏览器
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    selenium_run()
