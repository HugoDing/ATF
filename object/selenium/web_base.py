# -*- coding=utf-8 -*-

"""
About this module

Description of classes

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
# V0.1      2014-11-16   First version                                 Hugo
# ------------------------------------------------------------------------------

from object.selenium.pagetool import PageTool
from selenium.webdriver.common.by import By


class BaseObject(PageTool):
    _bo_element = {
        "input": {
        },

        "button": {
            "settings": "span[title='Settings']",
            "user_profile": "span[title='User Profile']",
            "messages": "span[title='Messages']"
        },

        "link": {
            "logout": {"value": "退出", "locator": By.LINK_TEXT},
        }
    }

    @property
    def link_logout(self):
        return self.find_element(**self._bo_element["link"]["logout"])

    @property
    def button_user_profile(self):
        return self.find_element(self._bo_element["button"]["user_profile"])