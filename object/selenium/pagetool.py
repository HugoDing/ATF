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
        Return an element identified by a specific locator.
    click_button:
        Click a button

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
]

__version__ = "V0.2"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-11-10   First version                                 Hugo
# V0.2      2015-01-08   Add click_button, is_usable, set_text methods to this
#     module.                                                          Hugo
# ------------------------------------------------------------------------------

from selenium.common.exceptions import \
    NoSuchElementException, TimeoutException, StaleElementReferenceException

from logging_report.logging_ import print_log


class PageTool(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, value="", locator=None):
        if not locator:
            return self.driver.find_element_by_css_selector(value)
        else:
            return self.driver.find_element(by=locator, value=value)

    def click_button(self, button):
        """
        @summary: Click the destination button
        @param:
            button: The button element
        @return: Return True if click successfully, else False
        """
        if self.is_usable(button):
            try:
                button.click()
                return True
            except (NoSuchElementException, TimeoutException):
                print_log("Can not find the button by xpath: '%s'.", "Error")
                return False
            except StaleElementReferenceException:
                print_log(
                    "The element(xpath: %s) is not as same as it has been "
                    "located, please check your code." % button,
                    "Error")
                return False
        else:
            print_log("The button is unusable, and can not be clicked!",
                      "Error")
            return False
    
    @staticmethod
    def is_usable(element=None):
        """
        :summary: Assert an element is usable or not
        :param:
            element: The object you want to assert
        :return: Return True if the element is usable，else False
        """
        return element.is_enabled() and element.is_displayed()
    
    @staticmethod
    def set_text(input_=None, text=None):
        """
        :summary: Send text to destination
        :param:
            input: Input text element
            text: The text you want to input
        """
        input_.clear()
        input_.send_keys(text)