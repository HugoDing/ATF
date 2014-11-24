# -*- coding=utf-8 -*-

"""
About this module
    This module could be used in almost all Selenium object modules.

Description of classes
    PageTool:
        All the methods in this class is nothing to do with business, and can
        be used by other object classes.

Description of methods
    find_element:
        Return an element identified by CSS selector.

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-10   First version                                 Hugo
# ------------------------------------------------------------------------------


class PageTool(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, value, locator=None):
        if not locator:
            return self.driver.find_element_by_css_selector(value)
        else:
            return self.driver.find_element(by=locator, value=value)
