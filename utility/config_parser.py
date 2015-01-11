# -*- coding=utf-8 -*-

"""
About this module
    Read and set the configuration files

Description of classes
    _StaticVariable:
        Use class method to implement some static variables.

Description of methods
    get_config:
        Get the value of configuration file using sector name and item name.

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-11   First version                                 Hugo
# V0.2      2014-11-13   Add _StaticVariable class to read config
#                            once during one run                       Hugo
# ------------------------------------------------------------------------------

import configparser

from system_opration.file_system import get_ini_path


def get_config(sector, item):
    is_got = _StaticVariable().check_status(sector, item)
    if is_got:
        return is_got
    else:
        # print "Simple debug: Start to parser %s.%s..." % (sector, item)
        cf = configparser.ConfigParser()
        cf.read(get_ini_path())
        value = cf.get(sector, item)
        _StaticVariable().set_value(sector, item, value)
        return value


class _StaticVariable(object):
    config = {}

    @classmethod
    def check_status(cls, sector, item):
        try:
            return cls.config[sector][item]
        except KeyError:
            return False

    @classmethod
    def set_value(cls, sector, item, value):
        try:
            cls.config[sector][item] = value
        except KeyError:
            cls.config[sector] = {}
            cls.config[sector][item] = value

    @classmethod
    def reload(cls):
        cls.config = {}


if __name__ == "__main__":
    print(get_config("selenium", "host"))
    print(get_config("selenium", "host"))
