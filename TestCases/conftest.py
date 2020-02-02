# -*- conding: utf-8 -*-
# @Time:2020/1/5 19:05
# @Author:lyc
# @File: conftest.py
# @Software: PyCharm

import time
import os
import shutil


import pytest
from selenium import webdriver

from TestDatas import Common_Datas
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from PageObjects.classroom_page import ClassroomPage
from TestDatas.join_classroom import success_data


@pytest.fixture("class")
def init_driver():
    # 创建会话对象
    driver = webdriver.Chrome(r'C:\Users\TR\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    # 窗口最大化
    driver.maximize_window()
    # 打开网址https://www.ketangpai.com/
    driver.get(Common_Datas.home_url)
    # 首页点击登录按钮
    HomePage(driver).click_login_button()
    # 登录页面，登录账号
    LoginPage(driver).login(Common_Datas.username, Common_Datas.password)
    # 课堂页面，关闭提醒
    ClassroomPage(driver).close_notice()

    yield driver
    driver.quit()


@pytest.fixture()
def setup(init_driver):
    time.sleep(1.5)
    ClassroomPage(init_driver).join_classroom(success_data[0]["join_class_code"])
    yield init_driver
    # 返回课堂首页
    init_driver.get("https://www.ketangpai.com/Main/index.html")
    # 退出课堂
    ClassroomPage(init_driver).exit_web_class(Common_Datas.password)


@pytest.fixture("session", autouse=True)
def initialize():
    shutil.rmtree(r"D:\project\py23_web_ketangpai\Outputs\allure_report")  # 能删除该文件夹和文件夹下所有文件
    os.mkdir(r"D:\project\py23_web_ketangpai\Outputs\allure_report")
    yield