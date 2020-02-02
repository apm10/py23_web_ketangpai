import logging
import os

# from scripts.handle_yaml import do_yaml
from Common.handle_path import LOGS_DIR


class MyLogger(object):

    @classmethod
    def create_logger(cls):
        my_log = logging.getLogger("cases")
        my_log.setLevel("DEBUG")
        formater = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        sh.setFormatter(formater)
        my_log.addHandler(sh)

        fh = logging.FileHandler(filename=os.path.join(LOGS_DIR,"test.log"),
                                 encoding='utf8')
        fh.setLevel("DEBUG")
        fh.setFormatter(formater)
        my_log.addHandler(fh)
        return my_log


do_log = MyLogger.create_logger()


if __name__ == '__main__':
    do_log = MyLogger.create_logger()
    do_log.debug("debug")
    pass