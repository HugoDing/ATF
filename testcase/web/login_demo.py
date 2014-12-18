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
    '"Hugo Ding" <huicong.ding@spirent.com>',
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


class LoginDemo(SeleniumBaseTestCase):
    def setUp(self):
        super(LoginDemo, self).setUp()

    @SeleniumBaseTestCase.drive_data
    def test_login(self):
        def do_test():
            bw = BaseWizard()
            bw.login_as()
            pass

        do_test()

    def tearDown(self):
        super(LoginDemo, self).tearDown()
