# -*- conding: utf-8 -*-
# @Time:2020/1/31 22:36
# @Author:lyc
# @File: classroom_page_loc.py
# @Software: PyCharm


from selenium.webdriver.common.by import By


class ClassroomPageLoc:

    # 关闭提醒按钮
    close_button = (By.XPATH, '//a[@class="close"]')
    # web项目实战元素
    class_name = (By.XPATH, '//dt//a[@title="python-web项目实战- 考核项目"]')
    # 加入课程按钮
    join_class_button = (By.XPATH, '//div[@class="ktcon1l fr"]')
    # 加入按钮
    join_button= (By.XPATH, '//li[@class="cjli2"]/a')
    # 加课验证码输入框
    text_input = (By.XPATH, '//div[@class="chuangjiankccon"]//input')
    # 错误提示信息
    error_tip = (By.XPATH, '//div[@id="error-tip"]//span')
    # 成功提示信息
    show_tip = (By.XPATH, '//div[@id="show-tip"]//span')
    # 加入课程的取消按钮
    quxiao_button = (By.XPATH, '//a[@class="btn btn-defalut"]')
    # web项目实战元素
    web_ele = (By.XPATH, '//a[@title="python-web项目实战- 考核项目"]')
    # 更多按钮
    more_button = (By.XPATH, '//dl[@data-id="MDAwMDAwMDAwMLR2vd6Gz8mw"]//span[text()="更多"]')
    # 退课按钮
    exit_class_button = (By.XPATH, '//dl[@data-id="MDAwMDAwMDAwMLR2vd6Gz8mw"]//a[text()="退课"]')
    # 确认页面退课按钮
    exit_class_button_verify = (By.XPATH, '//li[@class = "dli2"]//a')
    # 退课密码输入框
    exit_class_input = (By.XPATH, '//input[@type="password"]')
    # 私信按钮
    msg_button = (By.XPATH, '//div[@class="privateLetter"]//a')