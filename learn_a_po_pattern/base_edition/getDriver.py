# coding=utf-8
"""
# @Author       : Wenqing Nie
# @Date         : 2020-11-04 16:21:56
# @LastEditTime : 2020-11-04 17:53:20
# @Description  : file content
# @FilePath     : /Learn_softwareAutomatedTesting/learn_a_po_pattern/getDriver.py
"""

from selenium import webdriver
from learn_a_po_pattern.base_edition import configs


class Driver:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name='chrome'):
        """
        单例模式获得selenium种webdriver对象。之所以写成一个类，是为了防止以后Driver需要添加功能，那么方便添加。所以需要做到面向未来编程
        @param browser_name:浏览器名称
        @return:浏览器对应的webdriver对象
        """
        if cls._driver is None and browser_name == 'chrome':
            cls._driver = webdriver.Chrome(configs.driverPath[browser_name])
            cls._driver.maximize_window()
            cls._driver.get(url=configs.URL)
        elif cls._driver is None:
            raise RuntimeError(f'未配置{browser_name}浏览器驱动')
        return cls._driver


if __name__ == '__main__':
    driver = Driver.get_driver('chrome')
    driver.quit()
