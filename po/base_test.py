#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import unittest
from appium import webdriver
from config import global_parameters


class BaseTest(unittest.TestCase):
    vivo6_appium_server = global_parameters.vivo6p_appium_server_port
    vivo6_platformName = global_parameters.vivo6p_system
    vivo6_platformVersion = global_parameters.vivo6p_version
    vivo6_deviceName = global_parameters.vivo6p_deviceName
    app_package = global_parameters.apk_package
    app_activity = global_parameters.apk_activity

    def setUp(self):
        desired_caps_vivo = {'platformName': BaseTest.vivo6_platformName,
                             'platformVersion': BaseTest.vivo6_platformVersion,
                             'deviceName': BaseTest.vivo6_deviceName,
                             'appPackage': BaseTest.app_package,
                             'appActivity': BaseTest.app_activity,
                             'unicodeKeyboard': 'True',
                             'resetKeyboard': 'True'}
        self.driver = webdriver.Remote(BaseTest.vivo6_appium_server, desired_caps_vivo)

    def tearDown(self):
        self.driver.quit()
