# -*- coding=utf-8 -*-

"""
About this module
    All the objects in the login page of Velocity Create

Description of classes
    LoginObject: SAA

Description of methods
    input_username:
        User name input area, converted to property.
    input_password:
        Password input area, converted to property.
    button_login:
        Login button, converted to property.
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

from object.selenium.pagetool import PageTool


class LoginObject(PageTool):

    _element = {
        "input": {
            "username": "input[name='username']",
            "password": "input[name='password']",
        },
        "button": {
            "login_button": "button.btn-default"
        }
    }

    @property
    def input_username(self):
        return self.find_element(self._element["input"]["username"])

    @property
    def input_password(self):
        return self.find_element(self._element["input"]["password"])

    @property
    def button_login(self):
        return self.find_element(self._element["button"]["login_button"])