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
# V0.1      2014-12-18   First version                                 Hugo
# ------------------------------------------------------------------------------

import time
from logging_report.logging_ import print_log


def timer(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result_ = f(*args, **kwargs)
        end = time.time()
        print_log("Function '%s' took %f second(s)." % (f.__name__, end-start))
        return result_
    return f_timer


if __name__ == '__main__':
    def get_number():
        for x in xrange(5000000):
            yield x

    @timer
    def expensive_function():
        for x in get_number():
            i = x ^ x ^ x
            # print i
        return 'some result!'

    result = expensive_function()