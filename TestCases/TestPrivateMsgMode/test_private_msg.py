# -*- conding: utf-8 -*-
# @Time:2020/2/2 15:21
# @Author:lyc
# @File: test_private_msg.py
# @Software: PyCharm
import time

import pytest

from PageObjects.letter_page import LetterPage
from PageObjects.classroom_page import ClassroomPage


@pytest.mark.usefixtures("init_driver")
class TestPrivateMsg:

    @pytest.mark.smoke
    def test_private_msg_success(self, init_driver):
        ClassroomPage(init_driver).enter_msg_page()
        time.sleep(3)
        LetterPage(init_driver).send_letters("表白敏敏")
        assert LetterPage(init_driver).get_content() == "表白敏敏"



