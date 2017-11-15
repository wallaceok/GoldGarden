#!/usr/bin/python3
# coding:utf-8

from po.base_test import BaseTest
from common.log import Log
from po.change_psw_page import ChangePassword
from po.login_page import LoginPage


class ForgetPassword(BaseTest, ChangePassword, LoginPage):

    log = Log()

    def test_A_change_psw(self):
        self.log.info("############################### START ###############################")
        self.forget_password('13679130028', '9999', '12345678')
        self.save_screenshot('ChangePswOK')
        result = self.show_version_text()
        self.assertEqual(result, True)
        self.log.info("###############################  End  ###############################")
