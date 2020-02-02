# -*- conding: utf-8 -*-
# @Time:2020/2/1 9:57
# @Author:lyc
# @File: test_01_join_classroom.py
# @Software: PyCharm

import os
from _datetime import datetime
import time

import pytest

from Common.handle_path import PAGESHOTS_DIR
from Common.handle_log import do_log
from PageObjects import classroom_page, home_page, login_page
from TestDatas.join_classroom import success_data, error_data
from TestDatas.Common_Datas import password


@pytest.mark.usefixtures("init_driver")
class TestJoinClassroom:

    # 成功加入课程
    @pytest.mark.smoke
    def test_01_success_join_classroom(self, init_driver):
        do_log.info("-------------成功加入课程用例开始执行----------------")
        # 加入课程
        classroom_page.ClassroomPage(init_driver).join_classroom(success_data[0]["join_class_code"])
        # 获取提示信息
        show_tip_text = classroom_page.ClassroomPage(init_driver).get_show_tip_text()
        file_name = os.path.join(PAGESHOTS_DIR, f"加入课程_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.png")
        try:
            assert show_tip_text == success_data[0]["check_msg"]
        except:
            init_driver.save_screenshot(file_name)
            do_log.error(f"加入课程用例执行失败，截图：{file_name}")
        else:
            do_log.info("-------------成功加入课程用例执行完毕----------------")

    # 加入课程失败的用例
    @pytest.mark.parametrize("data", error_data)
    def test_02_fail_join_classroom(self, init_driver, data):
        do_log.info("-------------异常场景：加入课程用例开始执行----------------")
        # 加入课程
        classroom_page.ClassroomPage(init_driver).join_classroom(data["join_class_code"])
        # 获取提示信息
        error_tip_text = classroom_page.ClassroomPage(init_driver).get_error_tip_text()
        time.sleep(5)
        file_name = os.path.join(PAGESHOTS_DIR, f"加入课程_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.png")
        try:
            assert error_tip_text == data["check_msg"]
        except:
            init_driver.save_screenshot(file_name)
            do_log.error(f"加入课程用例执行失败，截图：{file_name}")
        else:
            do_log.info("-------------异常场景：加入课程用例执行完毕----------------")
            classroom_page.ClassroomPage(init_driver).click_quxiao_button()

    # 退出课程
    @pytest.mark.smoke
    def test_03_exit_class_success(self, init_driver):
        do_log.info("-------------退课用例开始执行----------------")
        classroom_page.ClassroomPage(init_driver).exit_web_class(password)
        show_tip_text = classroom_page.ClassroomPage(init_driver).get_show_tip_text()
        file_name = os.path.join(PAGESHOTS_DIR, f"加入课程_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.png")
        try:
            assert show_tip_text == "课程退课成功"
        except:
            init_driver.save_screenshot(file_name)
            do_log.error(f"退课用例执行失败，截图：{file_name}")
        else:
            do_log.info("-------------退课用例执行完成----------------")
