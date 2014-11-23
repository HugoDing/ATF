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

__all__ = [
    "testcase_template"
]

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-23   First version                                 Hugo
# ------------------------------------------------------------------------------

# If you want to use data driven, "data" should be like this,
# "data": {"key": [value1, value2, value3]}
testcase_template = {
    "project": "velocity",
    "module": "login_demo",
    "case": "LoginDemo",
    "description": None,
    "data_driven": False,
    "data": {
        "login_name": "",
        "password": "",
        "message": ""
    }
}