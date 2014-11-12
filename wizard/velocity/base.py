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
# V0.1      2014-11-09   First version                                 Hugo
# ------------------------------------------------------------------------------

from time import sleep

from selenium import webdriver

from object.selenium.velocity_login import LoginObject
from utility.config_parser import get_config


class BaseWizard(LoginObject):
    """
    @summary: All wizards' father class
    """
    def login_as(self, user_name=None, password=None):
        self.input_username.send_keys(user_name)
        self.input_password.send_keys(password)
        self.button_login.click()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("%s:%s" % (
        get_config("global", "host"), get_config("global", "port")))
    bw = BaseWizard(driver) 
    bw.login_as("hding", "Della194310")
    sleep(10)
    driver.quit()
