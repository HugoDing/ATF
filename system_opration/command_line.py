# -*- coding=utf-8 -*-

"""
About this module
    Methods about command line should be putted here.

Description of classes
    None

Description of methods
    get_opt: Get options from command line.

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

import getopt
import sys

from logging_report.logging_ import print_log


def get_opt():
    try:
        options, args = getopt.getopt(
            sys.argv[1:], "hm:", ["help", "mode="]
        )
    except getopt.GetoptError:
        print_log("Critical error, please contact the administrator!", "error")
        return None
    else:
        return_value = {}
        for name, value in options:
            if name in ("-h", "--help"):
                usage()
            if name in ("-m", "--mode"):
                return_value["mode"] = value

        if return_value:
            return return_value
        else:
            print_log("No valuable command line option is specified!",
                      "warning")
            return {}


def usage():
    print (
        "Usage:\n"
        "--------------------------------------------------------------------\n"
        "-h, --help: Show this help document.\n"
        "-m=run_mode, --mode=run_mode: Run mode, these modes are supported:\n"
        "    all: Run all testcases under 'testcase' folder\n"
        "    config: Run testcases read from DB\n"
        "    smoke: Run smoke testcases"
    )