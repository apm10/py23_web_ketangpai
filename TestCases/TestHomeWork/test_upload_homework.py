# -*- conding: utf-8 -*-
# @Time:2020/2/1 21:25
# @Author:lyc
# @File: test_upload_homework.py
# @Software: PyCharm

import pytest
import time

from PageObjects.classroom_page import ClassroomPage
from PageObjects.web_class_page import WebClassPage
from TestDatas.Common_Datas import password
from Common.handle_log import do_log
from PageLocators.web_class_page_loc import WebClassPageLoc



@pytest.fixture()
def setup_enter_classroom(setup):
    # 进入课堂
    ClassroomPage(setup).enter_classroom()
    yield setup



@pytest.mark.usefixtures("setup_enter_classroom")
class TestUploadHomework:

    # 上传文件
    @pytest.mark.smoke
    def test_success_upload_homework(self, setup_enter_classroom):
        do_log.info("----------上传作业用例开始执行----------")
        WebClassPage(setup_enter_classroom).upload_homework_ready()
        # time.sleep(1)
        # ele = setup_enter_classroom.find_element(*WebClassPageLoc.add_button)
        # setup_enter_classroom.execute_script("arguments[0].click();", ele)
        time.sleep(3)
        # do_log.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        WebClassPage(setup_enter_classroom).upload_homework(r'D:\"bbb.txt" "aaa.txt"')
        msg = WebClassPage(setup_enter_classroom).get_msg()
        assert msg == "作业提交成功"
        do_log.info("----------上传作业用例执行完成----------")







