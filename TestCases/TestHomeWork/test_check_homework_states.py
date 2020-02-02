# -*- conding: utf-8 -*-
# @Time:2020/2/2 15:05
# @Author:lyc
# @File: test_check_homework_states.py
# @Software: PyCharm



import pytest

from PageObjects.classroom_page import ClassroomPage
from PageObjects.web_class_page import WebClassPage

@pytest.mark.usefixtures("setup")
class TestCheckHomeworkStates:

    @pytest.mark.smoke
    def test_check_homework_states_success(self, setup):
        ClassroomPage(setup).enter_classroom()
        assert WebClassPage(setup).get_homework_states() == "已提交"

