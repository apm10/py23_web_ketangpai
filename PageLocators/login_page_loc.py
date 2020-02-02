# -*- conding: utf-8 -*-
# @Time:2020/1/31 22:25
# @Author:lyc
# @File: login_page_loc.py
# @Software: PyCharm


from selenium.webdriver.common.by import By


class LoginPageLoc:

    # 用户名输入框
    user_name_input = (By.XPATH, '//input[@name="account"]')
    # 密码输入框
    password_input = (By.XPATH, '//input[@name="pass"]')
    #登录按钮
    login_button = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
