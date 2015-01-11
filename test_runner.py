# -*- coding=utf-8 -*-

"""
About this module
    All tests will start from this module.

Description of classes
    None

Description of methods
    execute_test: Execute the test cases in the test_suite.

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

from logging_report.HTMLTestRunner import HTMLTestRunner

from utility.config_parser import get_config
from utility.test_suite import get_test_suite, get_testcase
from logging_report.logging_ import print_log
from system_opration.command_line import get_opt
from system_opration.file_system import get_test_report_path


def execute_test(test_suite):
    """
    :summary: Execute test cases.
    :param test_suite: Test suite.
    """

    exec_type = get_config("run-time", "mode")

    print_log("Testcase(s) to run is(are): %s" % test_suite)

    result_file = get_test_report_path()
    fp = open(result_file, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="Automation test report",
        description=(
            "Automation test report\n"
            "Execution type is %s" % exec_type
        )
    )

    runner.run(test_suite)

if __name__ == "__main__":
    cmd_mode = get_opt().get("mode")
    mode = cmd_mode if cmd_mode else get_config("run-time", "mode")
    test_cases = get_testcase(mode)
    # test_cases = [
    #     "testcase.web.login_demo.ValidLogin",
    # ]
    suite = get_test_suite(test_cases)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    execute_test(suite)