# -*- conding: utf-8 -*-
# @Time:2020/2/1 16:32
# @Author:lyc
# @File: web_class_page_loc.py
# @Software: PyCharm


from selenium.webdriver.common.by import By

class WebClassPageLoc:

    # web项目实战元素
    web_class_ele = (By.TAG_NAME, 'h1')
    # 作业导航
    homework_button = (By.XPATH, '//a[text()="作业"]')
    # 已提交按钮
    submitted_button = (By.XPATH, '//a[@class="view-work"]')
    # 更新提交按钮
    update_button = (By.XPATH, '//a[@class="new-tj1"]')
    # 更新作业确定按钮
    sure_button = (By.XPATH, '//div[@class="btns"]//a[@class="sure active"]')
    # 添加作业文件按钮
    add_button = (By.XPATH, '//div[@class="shangchuan"]//a[contains(@class, "sc-btn")]')
    # 已上传元素
    succ = (By.XPATH, '//a[@class="succ"]')
    # 上传后的更新提交按钮
    update_button2 = (By.XPATH, '//a[@class="new-tj2 active"]')
    # 更新提交的提示信息
    update_msg= (By.XPATH, '//div[@class="weui_dialog_bd"]')
    # 作业留言
    msg_homework = (By.XPATH, '//div[@id="mess1"]')
    # 作业留言输入框
    msg_homework_input = (By.XPATH, '//textarea[@id="comment"]')
    # # 保存按钮
    # save_button = (By.XPATH, '//a[text()="保存"]')
    # 知道了
    know_button = (By.XPATH, '//a[@class="weui_btn_dialog primary"]')
    # 作业留言展示框
    show_homework_msg = (By.XPATH, '//span[@class="s2"]')



