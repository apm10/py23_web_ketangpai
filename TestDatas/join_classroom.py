# -*- conding: utf-8 -*-
# @Time:2020/2/1 14:47
# @Author:lyc
# @File: join_classroom.py
# @Software: PyCharm

# 正常场景
success_data = [{'join_class_code': "P69UVV", "check_msg": '加入课堂成功'}]

# 异常场景
error_data = [{'join_class_code': "a", "check_msg": '加课验证码必须是6位字符'},
              {'join_class_code': "asdf1234", "check_msg": '该加课码不存在或者已经失效'},
              {'join_class_code': "!@#abc", "check_msg": '该加课码不存在或者已经失效'},
              {'join_class_code': "P69UVV", "check_msg": '你已经选过此课程'}, ]
