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
        print "Simple debug: Temp folder is not gotten successfully!"
        dir_ = None

    # TODO: Create this folder if it is not existed.
    # return dir_ + os.sep + "ATF" if dir_ else None


if __name__ == "__main__":
    print get_tmp_dir()