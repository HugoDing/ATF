# -*- coding=utf-8 -*-

"""
About wizard.selenium.base
     
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
# V0.1      2014-11-09   First version                                 Hugo
# ------------------------------------------------------------------------------

from selenium import webdriver


class BaseWizard(object):
    '''
    @summary: All wizards' father class
    '''
    def __init__(self, driver):
        '''
        @summary: Transfer browser instance to this wizard
        '''
        self.driver = driver


    def login_as(self, user_name=None, password=None):
        pass
