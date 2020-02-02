# -*- conding: utf-8 -*-
# @Time:2020/2/1 10:29
# @Author:lyc
# @File: classroom_page.py
# @Software: PyCharm

import time

from Common.basepage import BasePage
from PageLocators.classroom_page_loc import ClassroomPageLoc


class ClassroomPage(BasePage):

    # 关闭公告提醒
    def close_notice(self):
        self.wait_ele_visible(ClassroomPageLoc.close_button, "课堂页面，等待公告提醒出现：")
        self.click_element(ClassroomPageLoc.close_button, "课堂页面，点击公告提醒关闭按钮：")

    # 加入课程
    def join_classroom(self, join_class_code):
        time.sleep(0.5)
        # self.wait_ele_visible(ClassroomPageLoc.join_class_button, "课堂页面，等待加入课程按钮可见：")
        self.click_element(ClassroomPageLoc.join_class_button, "课堂页面，点击加入课程按钮：")
        self.wait_ele_visible(ClassroomPageLoc.join_button, "课堂页面，等待加入按钮可见：")
        self.input_text(ClassroomPageLoc.text_input, join_class_code, "课堂页面,输入加课验证码：")
        time.sleep(1)
        self.click_element(ClassroomPageLoc.join_button, "课堂页面，点击加入按钮：")

    # 获取show-tip提示
    def get_show_tip_text(self):
        self.wait_ele_visible(ClassroomPageLoc.show_tip, "课堂页面，等待成功提示信息元素出现：")
        return self.get_text(ClassroomPageLoc.show_tip, "获取成功提示信息文本：")

    # 获取error-tip提示
    def get_error_tip_text(self):
        self.wait_ele_visible(ClassroomPageLoc.error_tip, "课堂页面，等待错误提示信息元素可见：")
        return self.get_text(ClassroomPageLoc.error_tip, "获取错误提示文本：")

    # 点击加入课程的取消按钮
    def click_quxiao_button(self):
        self.wait_ele_visible(ClassroomPageLoc.quxiao_button, "课堂页面，等待加入课程的取消按钮出现：")
        self.click_element(ClassroomPageLoc.quxiao_button, "课堂页面，点击加入课程的取消按钮")

    # 进入班级
    def enter_classroom(self):
        self.wait_ele_visible(ClassroomPageLoc.web_ele, "课堂页面，等待web实战元素可见：")
        self.click_element(ClassroomPageLoc.web_ele, "课堂页面，点击web实战元素：")

    # 退课
    def exit_web_class(self, password):
        self.wait_ele_visible(ClassroomPageLoc.more_button, "课堂页面，等待更多元素可见：")
        self.click_element(ClassroomPageLoc.more_button, "课堂页面，点击更多元素")
        self.wait_ele_visible(ClassroomPageLoc.exit_class_button, "课堂页面，等待退课按钮可见")
        self.click_element(ClassroomPageLoc.exit_class_button, "课堂页面，点击退课按钮")
        self.wait_ele_visible(ClassroomPageLoc.exit_class_button_verify, "课堂页面，等待退课确认按钮出现：")
        self.input_text(ClassroomPageLoc.exit_class_input, password, "课堂页面，输入退课确认密码：")
        time.sleep(1)
        self.click_element(ClassroomPageLoc.exit_class_button_verify, "课堂页面，点击确认退课按钮")
        self.wait_ele_visible(ClassroomPageLoc.show_tip, "课堂页面，等待show_tip元素出现")

    # 进入私信页面
    def enter_msg_page(self):
        self.click_element(ClassroomPageLoc.msg_button, "课堂页面，点击私信按钮：")
        self.switch_to_new_window()


