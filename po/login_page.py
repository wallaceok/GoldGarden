#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from po import base_page
from common.log import Log


class LoginPage(base_page.BasePage):

    log = Log()

    username_loc = (By.ID, "com.tdh.rpms:id/et_usertel")
    password_loc = (By.ID, "com.tdh.rpms:id/et_password")
    loginBtn_loc = (By.ID, "com.tdh.rpms:id/btn_login")
    version_loc = (By.ID, 'com.tdh.rpms:id/tv_version_number')

    def input_username(self, username):
        self.send_keys(username, *self.username_loc)

    def input_password(self, password):
        self.send_keys(password, *self.password_loc)

    def click_btn(self):
        self.click(*self.loginBtn_loc)

    def show_version_text(self):
        try:
            title_text = self.get_text(*self.version_loc)
            self.log.info("version text is： %s" % title_text)
            return True
        except:
            self.log.error("Skip to login interface failed")
            return False

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.key_code(4)
        self.click_btn()
        self.wait(10)















