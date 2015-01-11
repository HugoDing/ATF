# -*- coding=utf-8 -*-

"""
About this module
    All operations about file system will be putted here.

Description of classes
    None

Description of methods
    get_ini_path:
        Return the absolute path of ATF.ini file.
    get_tmp_dir:
        Return the temp directory of file system
"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-11   First version                                 Hugo
# ------------------------------------------------------------------------------

import os
import platform

from utility.time_parser import get_current_date, get_current_time


def _get_workspace_path():
    cur_dir = os.path.dirname(__file__)
    # print cur_path
    workspace = os.path.join(cur_dir, os.path.pardir)  # Get father directory.
    if os.path.isdir(workspace):
        return workspace
    else:
        return False


def get_ini_path():
    return _get_workspace_path() + os.sep + "ATF.ini"


def get_tmp_dir():
    if platform.system() == "Windows":
        dir_ = os.getenv("TMP")
    elif platform.system() in ("Linux", "Darwin"):
        dir_ = "/tmp"
    else:
        print("Simple debug: Temp folder is not gotten successfully!")
        dir_ = None

    if dir_:
        tmp_dir = dir_ + os.sep + "ATF"
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
        return tmp_dir
    else:
        print("Failed to get temporary folder!")
        return False


def get_test_report_path():
    report_dir = _get_workspace_path() + \
        os.sep + "logging_report" + os.sep + "reports"
    if not os.path.isdir(report_dir):
        os.mkdir(report_dir)
    return report_dir + os.sep + "%s_%s.html" \
                                 % (get_current_date(),
                                    get_current_time())


def get_log_dir():
    log_dir = _get_workspace_path() + \
        os.sep + "logging_report" + os.sep + "logs"
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    return log_dir


def get_testcase_dir():
    return _get_workspace_path() + os.sep + "testcase"


if __name__ == "__main__":
    print(get_tmp_dir())