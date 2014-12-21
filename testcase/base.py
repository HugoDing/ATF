# -*- coding=utf-8 -*-

"""
About this module
    All kinds of base test cases will be located here, such as Selenium,
Appium, Sikuli and pywinauto.

Description of classes
    BaseTestCase: All test cases should inherit from this class.
    SeleniumBaseTestCase: All Selenium test cases should inherit from this class

Description of methods
    setUP: Things to do before running your test scripts.
    tearDown: Things to do after running your test scripts.
    init_data: Get test data from database(default is MongoDB).
    set_test_result: Set the result to be Pass or Fail.
    fail_test: Set the result of one test case to be Fail.
    drive_data: A decorator to run one test couple of times to implement the
data driven test.

"""

__authors__ = [
    '"Hugo Ding" <dinghuicong@gmail.com>',
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
from selenium.common.exceptions import NoSuchWindowException

from logging_report.logging_ import print_log
from utility.config_parser import get_config
from database.mongo import MongoDB
from wizard.web.base import BaseWizard


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        pass
        # Public things to do before starting a test case should be putted here.

    def init_data(self):
        """
        :summary: Initialize test data for each test case
        :param : None
        :return: Test data dictionary of the current test case
        """
        project = str(self.__module__).split(".")[-2]
        module_name = str(self.__module__).split(".")[-1]
        test_case = str(self.__class__.__name__)
        mongo = MongoDB()
        return mongo.find_data(
            project=project, module=module_name, case=test_case
        )

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
        :summary: Decorator for data driven
        :param:
            f: function
        :bug: If the decorated method has parameters, this function cannot
            handle it for now.
        """
        def _call(f):
            def __call():
                data = self.init_data()
                for key in data['case']['datadrive']:
                    data = data['case']['datadrive'][key]
                    return_ = f(data)
                return return_
            return __call
        return _call


class SeleniumBaseTestCase(BaseTestCase):
    def setUp(self):
        host = get_config("selenium", "host")
        port = get_config("selenium", "port")
        browser = get_config("selenium", "browser").lower()
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
            raise NoSuchWindowException("The browser you set is not supported, "
                                        "please check your config file.")

        self.driver.maximize_window()
        self.driver.implicitly_wait(
            get_config("selenium", "implicitly_wait_time")
        )
        if port:
            self.driver.get(host + ":" + port)
        else:
            print_log("No port is specified.", "debug")
            self.driver.get(host)

    def tearDown(self):
        BaseWizard(self.driver).logout()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()