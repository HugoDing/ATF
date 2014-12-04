# -*- coding=utf-8 -*-

"""
About this module
    This module contains basic business logic of velocity.

Description of classes
    BaseWizard:
        Almost all the other wizards inherit from this one.
    
Description of methods
    login_as:
        Login to the system as someone.

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

    def logout(self):
        self.button_user_profile.click()
        self.link_logout.click()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("%s" % get_config("dut", "host"))
    bw = BaseWizard(driver) 
    bw.login_as("spirent", "spirent")
    bw.logout()
    sleep(10)
    driver.quit()
