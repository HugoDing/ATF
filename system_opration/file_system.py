# -*- coding=utf-8 -*-

"""
About this module

Description of classes

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

if __name__ == "__main__":
    print get_ini_path()