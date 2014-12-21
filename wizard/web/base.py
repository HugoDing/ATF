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
    '"Hugo Ding" <dinghuicong@gmail.com>',
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

from object.selenium.web_login import LoginObject
from utility.config_parser import get_config
from logging_report.logging_ import print_log


class BaseWizard(LoginObject):
    """
    @summary: All wizards' father class
    """
    def login_as(self, user_name=None, password=None):
        self.input_username.send_keys(user_name)
        self.input_password.send_keys(password)
        self.button_login.click()

    def logout(self):
        if not self.is_logout():
            self.link_logout.click()
            return self.is_logout()
        else:
            print_log("No need, you are already logging out.")

    def is_logout(self):
        if "logout" in self.driver.current_url.lower():
            print_log("Logout successfully!")
            return True
        else:
            print_log("You are still in the system!", "debug")
            return False


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get("%s" % get_config("selenium", "host"))
    bw = BaseWizard(driver) 
    bw.login_as("atf_test", "itestQA")
    bw.logout()
    sleep(10)
    driver.quit()
