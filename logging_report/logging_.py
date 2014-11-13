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
# V0.1      2014-11-13   First version                                 Hugo
# ------------------------------------------------------------------------------

import logging


def print_log(log, level="info"):
    logger = logging.getLogger("ATF")
    logger.setLevel(logging.DEBUG)

    # fh = logging.FileHandler('test.log')
    # fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # logger.addHandler(fh)
    logger.addHandler(ch)

    logger.debug(log)


if __name__ == "__main__":
    print_log('foo bar')