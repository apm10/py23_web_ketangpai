# -*- conding: utf-8 -*-
# @Time:2020/2/2 16:39
# @Author:lyc
# @File: letter_page.py
# @Software: PyCharm

from Common.basepage import BasePage
from PageLocators.letter_page_loc import LetterPageLoc


class LetterPage(BasePage):

    # 点击信息输入框
    def send_letters(self, words):
        self.click_element(LetterPageLoc.textarea, "私信页面，点击信息输入框：")
        self.input_text(LetterPageLoc.textarea, words, "私信页面，输入发送的信息内容：")
        self.click_element(LetterPageLoc.enter_butten, "私信页面，点击发送按钮")

    # 获取发送内容
    def get_content(self):
        return self.get_text(LetterPageLoc.letter_msg, "私信页面，获取最后一条私信内容")
