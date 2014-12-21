# -*- coding=utf-8 -*-

"""
About this module

Description of classes

Description of methods

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-12-21   First version                                 Hugo
# ------------------------------------------------------------------------------

import os

from copy import deepcopy
from utility.HTMLTestRunner import HTMLTestRunner

from utility.config_parser import get_config
from logging_report.logging_ import print_log


def execute_test(test_suite):
    """
    @summary: Execute test cases.
    @param test_suite: Test suite.
    """

    exec_type = get_config("run-time", "mode")

    print_log("Testcase(s) to run is(are): %s" % test_suite)

    result_file = "D:\\test_result.html"
    fp = file(result_file, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u"Automation test report",
        description=(
            u"Automation test report\n"
            u'Execution type is %s' % exec_type
        )
    )

    runner.run(test_suite)

if __name__ == "__main__":
    suite = [
        u"testcase.web.login_demo.ValidLogin",
        u"testcase.web.login_demo.ValidLogin"
    ]
    execute_test(suite)