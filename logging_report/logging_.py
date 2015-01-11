# -*- coding=utf-8 -*-

"""
About this module
    Log related methods.

Description of classes
    None

Description of methods
    print_log:
        Print logs with logging module with log level, logs can be printed to
        console and log file.

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-13   First version                                 Hugo
# ------------------------------------------------------------------------------

import logging
import os

from utility.config_parser import get_config
from system_opration.file_system import get_log_dir
from utility.time_parser import get_current_date


def _get_num_level(level):
    level_dict = {
        "CRITICAL": 50,
        "FATAL": 50,
        "ERROR": 40,
        "WARNING": 30,
        "WARN": 30,
        "INFO": 20,
        "DEBUG": 10,
        "NOTSET": 0,
    }

    return level_dict[level.upper()]


def print_log(log, level="info"):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger("ATF")
    logger.setLevel(logging.DEBUG)

    config_path = get_config("logging", "path")
    log_path = config_path if config_path else get_log_dir()
    if log_path:
        fh = logging.FileHandler(
            log_path + os.sep + "%s.log" % get_current_date()
        )
        fh.setLevel(int(get_config("logging", "level")))
        fh.setFormatter(formatter)
        if "FileHandler" not in str(logger.handlers):
            logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    if "StreamHandler" not in str(logger.handlers):
        logger.addHandler(ch)

    logger.log(_get_num_level(level), log)

    if "FileHandler" in str(logger.handlers):
        fh.close()
    ch.close()

if __name__ == "__main__":
    print_log('foo bar')
    print_log('foo bar')