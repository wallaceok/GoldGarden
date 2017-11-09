#!/usr/bin/python3
# coding:utf-8
from po.login_page import LoginPage
from po.base_test import BaseTest
from po.safety_page import Safe
from po.my_page import MyPage
from data import safety_data
from common.log import Log
from po.base_page import BasePage


class Safety(LoginPage, BaseTest, Safe, MyPage, BasePage):

    log = Log()

    def test_inspection_normal(self):
        self.log.info("############################### START ###############################")
        safety_data.safety_insert()
        self.login('18912656465', '12345678')
        self.inspection_normal()
        result = self.inspection_normal_result()
        self.save_screenshot('inspection_normal')
        self.log.info("Test results：%s" % result)
        self.key_code(4)
        self.key_code(4)
        self.key_code(4)
        self.key_code(4)
        self.logout()
        self.assertEqual(result, True)
        safety_data.safety_delete()
        self.log.info("###############################  End  ###############################")