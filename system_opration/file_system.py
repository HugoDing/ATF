# -*- coding=utf-8 -*-

"""
About this module

Description of classes
    None

Description of methods

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
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
import sys


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
        dir_ = os.environ("TMP")
    elif platform.system() == "Linux":
        dir_ = "/tmp"

    # return dir_ + os.sep + "ATF"
    return 0


if __name__ == "__main__":
    print get_ini_path()