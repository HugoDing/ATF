# -*- coding=utf-8 -*-

"""
About this module
    This module contains all the APIs about MySQL.
    
Description of classes
    MySQL:
        Methods to operate MySQL.

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
# V0.1      2014-10-31   First version                                 Hugo
# ------------------------------------------------------------------------------

import mysql.connector

from utility.config_parser import get_config


class MySQL(object):
    
    config = {
        'user': get_config("mysql", "user"),
        'password': get_config("mysql", "pass"),
        'host': get_config("mysql", "host"),
        'database': get_config("mysql", "db"),
        'raise_on_warnings': True,
    }

    def __init__(self):
        try:
            self.cnn = mysql.connector.connect(**self.config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))