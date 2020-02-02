# -*- conding: utf-8 -*-
# @Time:2020/2/2 16:36
# @Author:lyc
# @File: Letter_page_loc.py
# @Software: PyCharm

from selenium.webdriver.common.by import By


class LetterPageLoc:

    # 信息输入框
    textarea = (By.XPATH, '//textarea[@class="ps-container"]')
    # 发送按钮
    enter_butten = (By.XPATH, '//div[@class="btn-group"]//a')
    # 聊天列表
    letter_msg = (By.XPATH, '//div[@class="main"]//ul//li[last()]//div[@class="text"]')