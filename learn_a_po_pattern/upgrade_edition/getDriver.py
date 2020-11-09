#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/5 21:35
# @Author     : Wenqing Nie
# @File       : getDriver.py
# @Description: 继承抽离出各个页面共有内容组成的BasePage对象的getDriver升级版
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
from learn_a_po_pattern.upgrade_edition import configs
from selenium import webdriver


class Driver:
    # 初始化为 None
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        """
        获取浏览器驱动对象
        只有第一次调用本函数会创建浏览器，然后返回浏览器驱动对象
        第二次及以后都会直接返回浏览器驱动对象，不会重复创建
        :return:
        """
        # 如果不为空，就意味着已经创建过了，不需要再次创建
        if cls._driver is None:
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(configs.driverPath[browser_name])
            elif browser_name == "Firefox":
                cls._driver = webdriver.Firefox(configs.driverPath[browser_name])
            else:
                print("未配置此浏览器驱动%s" % browser_name)
                return
            # 隐式等待五秒钟
            cls._driver.implicitly_wait(5)
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的网页
            cls._driver.get(configs.URL)
            # 执行登录操作
            cls.__login()

        return cls._driver

    @classmethod
    def __login(cls):
        """
        私有方法，只能在类里边使用
        类外部无法使用，子类不能继承
        此函数解决登录问题
        :return:
        """
        cls._driver.find_element_by_name("username").send_keys(configs.username)
        cls._driver.find_element_by_name("password").send_keys(configs.passwd)
        cls._driver.find_element_by_css_selector("button").click()


if __name__ == '__main__':
    driver = Driver.get_driver()
