# -*- conding: utf-8 -*-
# @Time:2020/2/1 10:08
# @Author:lyc
# @File: login_page.py
# @Software: PyCharm


from PageLocators.login_page_loc import LoginPageLoc
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password):
        self.wait_ele_visible(LoginPageLoc.login_button, "登录页面，等待登录按钮可见")
        self.input_text(LoginPageLoc.user_name_input, username, "登录页面，输入用户名：")
        self.input_text(LoginPageLoc.password_input, password, "登录页面，输入密码：")
        self.click_element(LoginPageLoc.login_button, "登录页面，点击登录按钮：")
