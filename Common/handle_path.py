import os

one_path = os.path.abspath(__file__)
two_path = os.path.dirname(one_path)
three_path = os.path.dirname(two_path)

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # 获取配置文件所在的路径
# CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
#
# # 获取配置文件所在的路径
# CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, 'testcase.yaml')

# 获取日志文件所在的目录路径
LOGS_DIR = os.path.join(os.path.join(BASE_DIR, "Outputs"), 'logs')

# 获取报告文件所在的目录路径
REPORTS_DIR = os.path.join(os.path.join(BASE_DIR, "Outputs"), 'reports')

# 获取截图文件所在的目录路径
PAGESHOTS_DIR = os.path.join(os.path.join(BASE_DIR, "Outputs"), 'pageshots')



# 获取excel文件所在的目录路径
# DATAS_DIR = os.path.join(BASE_DIR, 'datas')
# print(one_path)

if __name__ == '__main__':


    print(BASE_DIR)
    print(REPORTS_DIR)