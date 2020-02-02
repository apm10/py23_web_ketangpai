# -*- conding: utf-8 -*-
# @Time:2019/12/29 16:48
# @Author:lyc
# @File: home_page.py
# @Software: PyCharm


from PageLocators.home_page_loc import HomePageLoc

from Common.basepage import BasePage


class HomePage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def click_login_button(self):
        self.wait_ele_visible(HomePageLoc.login_button, "首页，等待登录按钮可见")
        self.click_element(HomePageLoc.login_button, "首页，点击登录按钮：")

