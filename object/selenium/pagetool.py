# -*- coding=utf-8 -*-

"""
About object.pagetool

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
# V0.1      2014-11-10   First version                                 Hugo
# ------------------------------------------------------------------------------


class PageTool(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)