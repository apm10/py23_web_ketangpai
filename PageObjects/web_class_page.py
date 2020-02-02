# -*- conding: utf-8 -*-
# @Time:2020/2/1 16:35
# @Author:lyc
# @File: web_class_page.py
# @Software: PyCharm

import time

from selenium.webdriver.common.action_chains import ActionChains

from Common.basepage import BasePage
from PageLocators.web_class_page_loc import WebClassPageLoc


class WebClassPage(BasePage):

    # 确定web实战元素存在
    def check_ele(self):
        return self.check_element_visible(WebClassPageLoc.web_class_ele, "web项目页面，查看web实现元素存在：")

    # 上传作业
    def upload_homework_ready(self):
        self.wait_ele_visible(WebClassPageLoc.homework_button, "web课堂页面，等待作业元素可见：")
        self.click_element(WebClassPageLoc.homework_button, "web课堂页面，点击作业元素：")
        self.wait_ele_visible(WebClassPageLoc.submitted_button, "web作业页面，等待已提交按钮可见：")
        self.click_element(WebClassPageLoc.submitted_button, "web作业页面，点击已提交按钮：")
        self.wait_ele_visible(WebClassPageLoc.update_button, "提交作业页面，等待更新提交按钮可见：")
        self.click_element(WebClassPageLoc.update_button, "提交作业页面，点击更新提交按钮：")
        self.wait_ele_visible(WebClassPageLoc.sure_button, "提交作业页面，等待更新作业的确定按钮可见：")
        self.click_element(WebClassPageLoc.sure_button, "提交作业页面，点击更新作业的确定按钮：")

        # time.sleep(2)
        # self.wait_ele_visible(WebClassPageLoc.add_button, "提交作业页面，等待添加作业按钮可见：")
        # self.click_element(WebClassPageLoc.add_button, "提交作业页面，点击添加作业按钮：")


    # 上传作业
    def upload_homework(self,filepath):
        self.click_element(WebClassPageLoc.add_button, "提交作业页面，点击添加作业文件：")
        time.sleep(3)
        BasePage.upload(filepath)
        self.wait_ele_visible(WebClassPageLoc.succ, "提交作业页面，等待已上传元素可见：")
        self.wait_ele_visible(WebClassPageLoc.update_button2, "提交作业页面，等待更新提交元素可见：")
        self.click_element(WebClassPageLoc.update_button2, "提交作业页面，点击更新提交元素：")

    # 获取上传作业的提示信息
    def get_msg(self):
        self.wait_ele_visible(WebClassPageLoc.update_msg, "更新提交作业，等待提示信息出现:")
        return self.get_text(WebClassPageLoc.update_msg, "更新提交作业，获取提示信息:")

    # 输入留言
    def send_homework_msg(self,words):
        self.click_element(WebClassPageLoc.msg_homework, "更新提交作业，点击作业留言区域：")
        time.sleep(1)
        self.clear_text(WebClassPageLoc.msg_homework_input, "更新作业，清空留言输入框")
        self.input_text(WebClassPageLoc.msg_homework_input, words, "更新提交作业，输入留言：")
        # self.click_element(WebClassPageLoc.save_button, "更新提交作业，点击保存按钮")
        self.click_element(WebClassPageLoc.update_button2, "更新提交作业，点击更新提交按钮：")
        self.click_element(WebClassPageLoc.know_button, "更新提交作业，点击知道了按钮：")

    # 获取作业留言内容
    def get_homework_msg(self):
        return self.get_text(WebClassPageLoc.show_homework_msg, "更新提交作业，获取作业留言信息")

    # 获取作业状态
    def get_homework_states(self):
        self.click_element(WebClassPageLoc.homework_button, "web课堂页面，点击作业导航")
        # self.wait_ele_visible(WebClassPageLoc.submitted_button, "web课堂页面，等待已提交按钮可见：")
        return self.get_text(WebClassPageLoc.submitted_button, "web课堂页面，获取按钮文本")









