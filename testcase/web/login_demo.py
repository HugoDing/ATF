# -*- coding=utf-8 -*-

"""
About this module
    A demo of test case.

Description of classes
    LoginDemo:
        Demo test case class for login.

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
# V0.1      2014-11-12   First version                                 Hugo
# ------------------------------------------------------------------------------

from testcase.base import SeleniumBaseTestCase
from wizard.web.base import BaseWizard
from logging_report.logging_ import print_log


class ValidLogin(SeleniumBaseTestCase):
    def setUp(self):
        super(ValidLogin, self).setUp()

    def test_valid_login(self):
        dict_data = self.init_data()
        # bw = BaseWizard(self.driver)
        # print_log("Starting to login to the system.")
        # bw.login_as(dict_data["login_name"], dict_data["password"])
        # self.assertIs(bw.is_logout(), False)

    def tearDown(self):
        super(ValidLogin, self).tearDown()


class InvalidLogin(SeleniumBaseTestCase):
    def setUp(self):
        super(InvalidLogin, self).setUp()

    def test_invalid_login(self):
        # dict_data = self.init_data()

        @SeleniumBaseTestCase.drive_data(self)
        def do_test(data):
            bw = BaseWizard(self.driver)
            bw.login_as()
            pass

        do_test()

    def tearDown(self):
        super(InvalidLogin, self).tearDown()