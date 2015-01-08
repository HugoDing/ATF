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
        print_log("No command line options are specified.", "debug")
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
            print_log("The options you specified are not supported!", "error")
            usage()
            sys.exit(-1)


def usage():
    print "-h, --help: Show this help document."
    print "-m=run_mode, --mode=run_mode: Run mode, these modes are supported:" \
          "    all: Run all testcases under 'testcase' folder" \
          "    config: Run testcases read from DB" \
          "    smoke: Run smoke testcases"