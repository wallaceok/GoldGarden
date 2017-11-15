#!/user/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from po import base_page
from common.log import Log


class ChangePassword(base_page.BasePage):

    log = Log()

    forget_psw_loc = (By.ID, 'com.tdh.rpms:id/tv_forget_password')
    change_psw_title_loc = (By.ID, 'com.tdh.rpms:id/tv_title')
    phone_loc = (By.ID, 'com.tdh.rpms:id/et_reset_mobile')
    identify_code_loc = (By.ID, 'com.tdh.rpms:id/et_reset_identify_code')
    new_psw_loc = (By.ID, 'com.tdh.rpms:id/et_new_pwd')
    affirm_btn_loc = (By.ID, 'com.tdh.rpms:id/btn_confrim')

    def click_forget_psw(self):
        self.click(*self.forget_psw_loc)

    def show_psw_title_text(self):
        try:
            title_text = self.get_text(*self.change_psw_title_loc)
            self.log.info("change password page title is： %s" % title_text)
            return True
        except:
            self.log.error("Skip to change password page failed")
            return False

    def input_phone(self, phone):
        self.send_keys(phone, *self.phone_loc)

    def input_code(self, identify_code):
        self.send_keys(identify_code, *self.identify_code_loc)

    def input_new_password(self, new_password):
        self.send_keys(new_password, *self.new_psw_loc)

    def click_affirm_btn(self):
        self.click(*self.affirm_btn_loc)

    def forget_password(self, phone, identify_code, new_password):
        self.click_forget_psw()
        self.show_psw_title_text()
        self.input_phone(phone)
        self.input_code(identify_code)
        self.input_new_password(new_password)
        self.click_affirm_btn()
