#!/usr/bin/python3
# coding:utf-8
from po.login_page import LoginPage
from po.base_test import BaseTest
from common.log import Log
from po.home_page import HomePage
from po.my_page import MyPage


class Login(BaseTest, LoginPage, HomePage, MyPage):

    log = Log()

    def test_A_success(self):
        self.log.info("############################### START ###############################")
        self.login("15902034568", "12345678")
        result = self.show_home_title()
        self.save_screenshot('LoginSuccess')
        self.log.info("Test results：%s" % result)
        self.logout()
        self.show_version_text()
        self.assertEqual(result, True)
        self.log.info("###############################  End  ###############################")






