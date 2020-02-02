# -*- conding: utf-8 -*-
# @Time:2020/2/1 16:07
# @Author:lyc
# @File: test_02_enter_classroom.py
# @Software: PyCharm

import time
from datetime import datetime
import os

import pytest

from PageObjects.classroom_page import ClassroomPage
from PageObjects.web_class_page import WebClassPage
from Common.handle_log import do_log
from Common.handle_path import PAGESHOTS_DIR


class TestEnterClassroom:

    # 进入班级
    @pytest.mark.smoke
    @pytest.mark.usefixtures("setup")
    def test_enter_classroom(self,setup):
        do_log.info("----------进入班级用例开始执行----------")
        ClassroomPage(setup).enter_classroom()
        time.sleep(5)
        file_name = os.path.join(PAGESHOTS_DIR, f"加入课程_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.png")
        try:
            assert WebClassPage(setup).check_ele()
            assert setup.current_url == "https://www.ketangpai.com/Interact/index/courseid/MDAwMDAwMDAwMLR2vd6Gz8mw.html"
        except:
            setup.save_screenshot(file_name)
            do_log.error(f"用例执行失败，截图为：{file_name}")
        else:
            do_log.info("----------进入班级用例执行成功----------")





