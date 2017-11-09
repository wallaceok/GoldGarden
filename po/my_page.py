#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from po import base_page
from common.log import Log


class MyPage(base_page.BasePage):

    log = Log()

    my_tab_loc = (By.ID, 'com.tdh.rpms:id/iv_tab_my')
    my_title_loc = (By.NAME, '我的')
    my_logout_loc = (By.ID, 'com.tdh.rpms:id/btn_logout')

    def click_my_tab(self):
        self.click(*self.my_tab_loc)

    def show_my_title(self):
        try:
            title_text = self.get_text(*self.my_title_loc)
            self.log.info("my_title is： %s" % title_text)
            return True
        except:
            self.log.error("Jump to my interface failed")
            return False

    def click_logout(self):
        self.click(*self.my_logout_loc)

    def logout(self):
        self.click_my_tab()
        self.show_my_title()
        self.click_logout()




