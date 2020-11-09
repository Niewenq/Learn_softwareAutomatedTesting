#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/7 19:56
# @Author     : Wenqing Nie
# @File       : main.py
# @Description: selenium第六次作业main.py文件
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm

"""
要求：实现一个免登陆的po框架
分析：免登陆，那么先登录获取其中的cookies然后修改即可。
步骤：
    1.先判断login_cookie.json文件是否存在，如果存在则执行步骤2，否则跳到步骤3；
    2.读取login_cookie.json，尝试免登陆；
    3.免登陆成功（通过URL地址判断），sleep5秒退出程序；免登录失败，重新登陆，重写文件保存cookies；
"""
import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_6_homework import configs


class Driver:
    _driver = None

    @classmethod
    def get_driver(cls, browserName):
        if cls._driver is None and browserName == 'Chrome':
            cls._driver = webdriver.Chrome(configs.driverPath[browserName])
            cls._driver.maximize_window()
        elif cls._driver is None:
            raise RuntimeError(f'{browserName}未实现驱动！')
        return cls._driver


class BasePage:
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver('Chrome')

    @staticmethod
    def find_element_explicit_wait(driver, locator, time_out=configs.TIME_OUT, poll_frequency=configs.POLL_FREQUENCY,
                                   method=ec.visibility_of_element_located):
        return WebDriverWait(driver=driver, timeout=time_out, poll_frequency=poll_frequency).until(
            method=method(locator=locator))


class LoginPage(BasePage):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.username_locator = (By.CSS_SELECTOR, "input[name='username']")
        self.password_locator = (By.CSS_SELECTOR, "input[name='password']")
        self.login_btn_locator = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self):
        # 1.打开登陆页面
        self.driver.get(url='http://' + configs.HOST + configs.LOGIN_URL)
        # 2.判断login_cookie.json是否存在
        if os.path.exists(configs.LOGIN_COOKIES_FILE):
            self.driver.delete_all_cookies()
            print('正在尝试使用cookies登陆......')
            # 3.读取cookies
            with open(configs.LOGIN_COOKIES_FILE) as fp:
                cookies = json.load(fp)
            # 4.添加cookies
            for cookie in cookies:
                self.driver.add_cookie(cookie_dict=cookie)
            # 5.刷新登陆
            self.driver.refresh()
            # 6.判断是否登陆成功
            time.sleep(3)
            if 'login' in self.driver.current_url:
                print('通过cookies登陆失败!')
            else:
                print('通过cookies登陆成功!')
                return
        # 3.判断cookies文件不存在或者通过cookies登陆失败
        print('正在尝试使用用户名和密码登陆......')
        #   3.1 输入用户名和密码并登录
        self.find_element_explicit_wait(self.driver, self.username_locator).send_keys(configs.USER_NAME)
        self.find_element_explicit_wait(self.driver, self.password_locator).send_keys(configs.USER_PASSWD)
        self.find_element_explicit_wait(self.driver, self.login_btn_locator).submit()
        #   3.1 去除期限并保存cookies
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
        with open(configs.LOGIN_COOKIES_FILE, mode='w') as fp:
            json.dump(cookies, fp, indent=4, separators=(', ', ': '))
        time.sleep(3)
        if 'login' in self.driver.current_url:
            print('通过用户名和密码登陆失败!')
        else:
            print('通过用户名和密码登陆成功!')


if __name__ == '__main__':
    Driver.get_driver('Chrome')
    import time

    LoginPage().login()
    time.sleep(10)
    Driver.get_driver('Chrome').quit()
