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
# V0.1      2014-11-11   First version                                 Hugo
# ------------------------------------------------------------------------------

import ConfigParser

from system_opration.file_system import get_ini_path


def get_config(sector, item):
	cf = ConfigParser.ConfigParser()
	cf.read(get_ini_path())
	return cf.get(sector, item)

if __name__ == "__main__":
	print get_config("global", "host")