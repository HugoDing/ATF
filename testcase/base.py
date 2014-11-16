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
# V0.1      2014-11-13   First version                                 Hugo
# ------------------------------------------------------------------------------

import unittest
import os

from selenium import webdriver

from logging_report.logging_ import print_log

from utility.config_parser import get_config


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        pass
        # Public things to do before starting a test case should be putted here.

    def init_data(self):
        """
        @summary: Initialize test data for each test case
        @param : None
        @return: Test data dictionary of the current test case
        """
        module_name = str(self.__module__).split(".")[-1]
        test_case = str(self.__class__.__name__)

        # TODO Get test data from MongoDB

    def tearDown(self):
        pass

    def set_test_result(self, result='pass', message='No more message.'):
        if result.lower() == 'pass':
            print_log("Test case has been executed successfully, "
                      "here is the message: %s" % message, 'pass')
            # self.assertTrue(True, "True")

        elif result.lower() == 'fail':
            print_log(message)
            raise self.failureException("Test case execute failed, "
                                        "here is the message: %s" % message)
        else:
            print_log("The test result should be 'pass' or 'fail',"
                      "your input is not supported.", "error")
            return False

    def fail_test(self, message):
        return self.set_test_result('fail', message)

    def drive_data(self):
        """
        @summary: Decorator for data driven
        @param:
            f: function
        @bug: If the decorated method has parameters, this function cannot
            handle it for now.
        """
        def _call(f):
            def __call():
                # return_ = []
                dict_data = self.init_data()
                for key in dict_data['case']['datadrive']:
                    if key != 'value':
                        data = dict_data['case']['datadrive'][key]
                        return_ = f(data)
                        # return_.append(f(data))

                return return_
            return __call
        return _call


class SeleniumBaseTestCase(BaseTestCase):
    def setUp(self):
        host = get_config("dut", "host")
        port = get_config("dut", "port")
        browser = get_config("dut", "browser").lower()
        if browser == "firefox":
            # Set profile of Firefox
            profile = webdriver.FirefoxProfile()
            profile.set_preference(
                "intl.accept_languages", "en-us, en, en-us, en"
            )
            profile.set_preference(
                "extensions.addonnotification.showDaytip", "false"
            )  # Turn off daily tips of Firefox
            profile.set_preference(
                "account@mozillaonline.com.autoPopNum", "0"
            )  # Turn off the tip of Firefox passport
            self.driver = webdriver.Firefox(profile)
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            print_log("The browser is not supported! "
                      "Please check your AFT.ini!", "error")
            raise Exception
            # TODO Define an exception for browser error.

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(host + ":" + port)

    def tearDown(self):
        #TODO: Method to logout the system.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()