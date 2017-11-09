#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from po import base_page
from common.log import Log


class HomePage(base_page.BasePage):

    log = Log()

    home_title_loc = (By.NAME, "首页")

    def show_home_title(self):
        try:
            title_text = self.get_text(*self.home_title_loc)
            self.log.info("home_title is： %s" % title_text)
            return True
        except:
            self.log.error("login failure")
            return False



