# -*- conding: utf-8 -*-
# @Time:2020/2/2 13:59
# @Author:lyc
# @File: test_msg_homework.py
# @Software: PyCharm

import pytest

from PageObjects.classroom_page import ClassroomPage
from PageObjects.web_class_page import WebClassPage


@pytest.mark.usefixtures("setup")
class TestMsgHomework:

    @pytest.mark.smoke
    def test_msg_homework_success(self, setup):
        ClassroomPage(setup).enter_classroom()
        WebClassPage(setup).upload_homework_ready()
        WebClassPage(setup).send_homework_msg("表白简神")
        assert WebClassPage(setup).get_homework_msg() == "表白简神"




