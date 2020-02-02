# -*- conding: utf-8 -*-
# @Time:2020/1/4 10:22
# @Author:lyc
# @File: basepage.py
# @Software: PyCharm

from datetime import datetime
import time
import os

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import win32gui
import win32con

from Common.handle_log import do_log
from Common.handle_path import PAGESHOTS_DIR


class BasePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _save_page_shot(self, img_doc):
        # 截图存放的路径
        file_name = os.path.join(PAGESHOTS_DIR, f"{img_doc}_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.png")
        do_log.info(f"截图保存在：{file_name}")
        try:
            self.driver.save_screenshot(file_name)
        except:
            do_log.exception("保存截图失败。")
        else:
            do_log.info("保存截图成功。")

     # 检查元素是否可见
    def check_element_visible(self,locator,img_doc,timeout=10,poll_fre=0.5):
        """
         # 检测元素是否在页面存在且可见。
         如果退出元素存在，则返回True。否则返回False
        :return: 布尔值
        """
        do_log.info("{}: 检测元素 {} 存在且可见于页面。".format(img_doc,locator))
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            do_log.exception(" {}秒内元素在当前页面不可见。".format(timeout))
            self._save_page_shot(img_doc)
            return False
        else:
            do_log.info(" {}秒内元素可见。".format(timeout))
            return True

    # 等待元素可见
    def wait_ele_visible(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        do_log.info(f"{img_doc}等待{loc}元素可见。")

        try:
            start_time = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 输出异常信息
            do_log.exception("等待可见元素失效")
            # 截图，截图名称要见名知意
            self._save_page_shot(img_doc)
            raise
        else:
            end_time = datetime.now()
            do_log.info(f"起始时间：{start_time}，结束时间：{end_time}，等待时长：{(end_time - start_time).total_seconds()}")

    # 等待元素存在
    def wait_page_contains_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        do_log.info(f"{img_doc}等待{loc}元素可见。")

        try:
            start_time = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except:
            # 输出异常信息
            do_log.exception("等待元素存在失败")
            # 截图，截图名称要见名知意
            self._save_page_shot(img_doc)
            raise
        else:
            end_time = datetime.now()
            do_log.info(f"起始时间：{start_time}，结束时间：{end_time}，等待时长：{(end_time - start_time).total_seconds()}")
    # 查找单个元素
    def get_element(self, loc, img_doc):
        # 记录操作日志
        do_log.info(f"开始查找{loc}元素。")
        # 开始时间
        start_time = datetime.now()
        # 查找元素
        try:
            ele = self.driver.find_element(*(loc))
        except:
            do_log.info(f"查找{loc}元素失败")  # 失败后，记录日志
            self._save_page_shot(img_doc)  # 失败后截图
            raise
        else:
            end_time = datetime.now()
            do_log.info(f"起始时间：{start_time}，结束时间：{end_time}，等待时长：{(end_time - start_time).total_seconds()}")
            return ele

    # 点击操作
    def click_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 记录日志
        do_log.info(f"{img_doc},点击{loc}元素。")
        # 点击元素
        try:
            ele.click()
        # 失败了记录日志
        except:
            do_log.exception(f"点击{loc}元素失败。")
            # 失败了截图
            self._save_page_shot(img_doc)
            raise

    # 清空输入框
    def clear_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 记录日志
        do_log.info(f"{img_doc}在{loc}清空文本值。")
        # 输入文本内容
        try:
            ele.clear()
        # 失败了记录日志
        except:
            do_log.exception(f"{img_doc}在{loc}清空文本值失败。")
            # 失败了截图
            self._save_page_shot(img_doc)
            raise

    # 输入操作
    def input_text(self, loc, text, img_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 记录日志
        do_log.info(f"{img_doc}在{loc}输入文本值：{text}。")
        # 输入文本内容
        try:
            ele.send_keys(text)
        # 失败了记录日志
        except:
            do_log.exception(f"{img_doc}在{loc}输入文本值：{text}失败。")
            # 失败了截图
            self._save_page_shot(img_doc)
            raise

    # 获取元素文本
    def get_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 记录日志
        do_log.info(f"{img_doc}获取元素{loc}的文本值。")
        # 输入文本内容
        try:
            value = ele.text
        # 失败了记录日志
        except:
            do_log.exception(f"{img_doc}获取元素{loc}的文本值失败。")
            # 失败了截图
            self._save_page_shot(img_doc)
            raise
        else:
            do_log.info(f"文本值为：{value}")
            return value

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 记录日志
        do_log.info(f"{img_doc}获取元素{loc}的{attr_name}属性。")
        # 输入文本内容
        try:
            value = ele.get_attribute(attr_name)
        # 失败了记录日志
        except:
            do_log.exception(f"{img_doc}获取元素{loc}的{attr_name}属性值失败。")
            # 失败了截图
            self._save_page_shot(img_doc)
            raise
        else:
            do_log.info(f"属性值为：{value}")
            return value

    # 获取当前url
    def get_current_url(self):
        # 记录日志
        do_log.info("获取当前页面的url。")
        try:
            value = self.driver.current_url
        # 失败了记录日志
        except:
            value = do_log.exception(f"获取当前页面url失败。")
            raise
        else:
            do_log.info(f"当前页面的url为：{value}")
            return value

    # 得到所有的窗口列表
    def get_window_handles(self):
        # 记录日志
        do_log.info("获取当前打开的所有的窗口。")
        try:
            wins = self.driver.window_handles
        # 失败了记录日志
        except:
            do_log.exception("获取打开的窗口列表失败。")
            raise
        else:
            do_log.info(f"窗口列表为：{wins}")
            return wins

    # 切换到最新窗口？ 0）触发新窗口出现 1）获取窗口列表；2）切换到最后一个；
    def switch_to_new_window(self):
        time.sleep(2)
        # 记录日志
        wins = self.get_window_handles()
        do_log.info(f"切换到最新的窗口：{wins[-1]}")
        try:
            self.driver.switch_to.window(wins[-1])

        # 失败了记录日志
        except:
            pass

    # 上传
    # edit - combox - comboBoxEx32 - #32770
    # 1\找到输入框和打开按钮 元素；2、输入地址，点击打开。
    # 前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。
    @staticmethod
    def upload(filePath, browser_type="chrome"):
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    # 切换到iframe


    # 切换到alert的处理




    # 滚动条处理？
# if __name__ == '__main__':
#     import time
#     time.sleep(2)
#     BasePage.upload(r'D:\"bbb.txt" "aaa.txt"')