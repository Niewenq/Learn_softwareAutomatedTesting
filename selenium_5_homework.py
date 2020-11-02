# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   selenium_fifth_homework.py
# @Time    :   2020/11/02 13:58:44

# here put the import lib
from selenium import webdriver


class Driver:
    # 初始化为 None
    _driver = None

    @classmethod
    def get_driver(cls):
        """
        获取浏览器对象
        :param browser_name:
        :return:
        """
        # 如果不为空就不需要新建了
        if cls._driver is None:
            cls._driver = webdriver.Chrome(
                executable_path=r'D:\webdrivers\chromedriver.exe')
            # 最大化窗口
            cls._driver.maximize_window()

        return cls._driver


class LoginPage:
    def __init__(self):
        # 创建 driver 对象
        self.driver = Driver.get_driver()

    # 用户名输入框

    def username_input_box(self):
        return self.driver.find_element_by_name("username")

    # 密码输入框
    def password_input_box(self):
        return self.driver.find_element_by_name("password")

    # 登录按钮
    def login_button_box(self):
        return self.driver.find_element_by_tag_name("button")


# 抽离出页面动作类, 继承对应的页面类
class LoginPageAction(LoginPage):

    def login(self):
        """
        访问 opms 登录界面, 登录用户
        :return:
        """
        # 访问登录页面
        self.driver.get(url='http://localhost:8088')
        # 输入用户名
        self.username_input_box().send_keys("libai")
        # 输入密码
        self.password_input_box().send_keys("opmsopms123")
        # 点击登录按钮
        self.login_button_box().click()
        # 阻塞
        input("输入任意字符继续运行>>>")
        self.driver.quit()


if __name__ == "__main__":
    LoginPageAction().login()
