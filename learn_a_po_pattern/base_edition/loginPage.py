#!/usr/bin/env python
# coding=utf-8
# @Time       : 2020/11/5 20:32
# @Author     : Wenqing Nie
# @File       : loginPage.py
# @Description: TODO
# @Project    : Learn_softwareAutomatedTesting
# @Software   : PyCharm
from learn_a_po_pattern.base_edition.getDriver import Driver


class LoginPage:
    def __init__(self):
        # 创建 driver 对象
        self.driver = Driver.get_driver()
        # 封装用户名输入框
        self.usernameLocator = "username"
        # 封装密码输入框
        self.passwdLocator = "password"
        # 封装登录按钮
        self.loginButtonLocator = "button"

    def username_box(self):
        return self.driver.find_element_by_name(self.usernameLocator)

    def passwd_box(self):
        return self.driver.find_element_by_name(self.passwdLocator)

    def login_button_box(self):
        return self.driver.find_element_by_css_selector(self.loginButtonLocator)


# 抽离出页面动作类，继承对应的页面类
class LoginPageAction(LoginPage):

    def login(self):
        self.username_box().send_keys("libai")
        self.passwd_box().send_keys("opmsopms123")
        self.login_button_box().click()


if __name__ == '__main__':
    LoginPageAction().login()

