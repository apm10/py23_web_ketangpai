# -*- conding: utf-8 -*-
# @Time:2020/1/27 11:58
# @Author:lyc
# @File: main.py
# @Software: PyCharm

import pytest

if __name__ == '__main__':
    # "-m", "smoke",
    pytest.main(["-m", "smoke",
                 "--reruns", "2", "--reruns-delay", "5",
                 "--html=Outputs/reports/result.html",
                 "--alluredir=Outputs/allure_report"])
