# -*- coding=utf-8 -*-

"""
About this module

Description of classes

Description of methods

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.2"

__all__ = [
    "testcase_template"
]

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-23   First version                                 Hugo
# V0.2      2015-01-10   Add test suite template                       Hugo
# ------------------------------------------------------------------------------

# If you want to use data driven, "data" should be like this,
# "data": {"key": [value1, value2, value3]}
testcase_template = {
    "project": "web",
    "module": "login_demo",
    "case": "ValidLogin",
    "description": None,
    "data_driven": False,
    "data": {
        "login_name": "atf_test",
        "password": "itestQA",
    }
}

testcase_data_driven_template = {
    "project": "web",
    "module": "login_demo",
    "case": "InvalidLogin",
    "description": None,
    "data_driven": True,
    "data": {
        "login_name": ["wrong_user_name", "atf_test", "atf_test"],
        "password": ["itestQA", "wrong_password", ""],
        "expected_result": [""]
    }
}

test_suite_template = {
    "type": "smoke",  # or config
    "id": 010203,
    "cases": "testcase.web.login_demo.ValidLogin",
    "summary": [],
}