# -*- coding=utf-8 -*-

"""
About this module
    Analyze the test suite

Description of classes
    None

Description of methods
    get_testcase: Get the test cases to execute
    get_testcase_from_module: Analyze the testcase file,
        return all testcases in it
"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2015-01-08   First version                                 Hugo
# ------------------------------------------------------------------------------

import os
import re
import sys
from copy import deepcopy
from unittest import TestSuite, TestLoader

from system_opration.file_system import get_testcase_dir
from database.mongo import MongoDB
from logging_report.logging_ import print_log


test_cases = []


def get_testcase(mode="smoke"):
    mode_lower = mode.lower()
    if mode_lower in ("smoke", "config", "demo"):
        mongo = MongoDB()
        return mongo.get_testcases_from_mongo(mode_lower)

    elif mode == "all":
        global test_cases
        test_case_dir = get_testcase_dir()
        all_folders = os.listdir(test_case_dir)
        all_case_files = []

        for folder in all_folders:
            sub_test_case_dir = test_case_dir + os.sep + folder
            if os.path.isdir(sub_test_case_dir):
                all_case_files.append({folder: os.listdir(sub_test_case_dir)})

        all_case_module = deepcopy(all_case_files)

        for item in all_case_module:
            for product in item:
                for case in item[product]:
                    if ".pyc" not in case and "__init__.py" not in case:
                        get_testcase_from_module(product, case)

        return test_cases

    else:
        print_log("Cannot recognize mode '%s', please take a double check!"
                  % mode,
                  "error")
        sys.exit(-1)


def get_testcase_from_module(product_name, module_name):
    """
    :summary: Return the test suite via the module of testcase
    :param product_name: The name of product
    :param module_name: The name of test module
    :return: Global list test_cases
    """
    global test_cases
    module_path = get_testcase_dir() + os.sep + product_name + \
        os.sep + module_name

    with open(module_path) as f:
        for line in f.readlines():  # Find all the names of testcase
            if re.match("^class", line) and "BaseTestCase)" in line:
                test_cases.append(
                    "testcase.%s.%s.%s"
                    % (
                        product_name,
                        module_name[:-3],
                        re.sub("\(.+\):\n", "", line[6:])
                    )
                )
        f.close()

    return test_cases


def get_test_suite(testcase_name):
    suite = TestSuite()
    loader = TestLoader()
    tests = loader.loadTestsFromNames(testcase_name)
    suite.addTests(tests)
    return suite


if __name__ == "__main__":
    print(get_testcase("all"))