#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from po import base_page
from common.log import Log


class Register(base_page.BasePage):

    log = Log()

    # -------------------------------注册身份-----------------------------------------

    user_register_loc = (By.ID, 'com.tdh.rpms:id/tv_register')
    register_title_loc = (By.ID, 'com.tdh.rpms:id/tv_title')
    phone_loc = (By.ID, 'com.tdh.rpms:id/et_tel')
    code_loc = (By.ID, 'com.tdh.rpms:id/et_identify')
    password_loc = (By.ID, 'com.tdh.rpms:id/et_register_password')
    person_choose_loc = (By.ID, 'com.tdh.rpms:id/rb_personal')
    enterprise_choose_loc = (By.ID, 'com.tdh.rpms:id/rb_enterprise')
    register_btn_loc = (By.ID, 'com.tdh.rpms:id/btn_shipper_register')

    def click_user_register(self):
        self.click(*self.user_register_loc)

    def show_register_title_text(self):
        try:
            title_text = self.get_text(*self.register_title_loc)
            self.log.info("change register page title is： %s" % title_text)
            return True
        except:
            self.log.error("Skip to change register page failed")
            return False

    def input_phone(self, phone):
        self.send_keys(phone, *self.phone_loc)

    def input_code(self, code):
        self.send_keys(code, *self.code_loc)

    def input_password(self, password):
        self.send_keys(password, *self.password_loc)

    def choose_person(self):
        self.click(*self.person_choose_loc)

    def choose_enterprise(self):
        self.click(*self.enterprise_choose_loc)

    def click_register_btn(self):
        self.click(*self.register_btn_loc)

    def person_register(self, phone, code, password):
        self.click_user_register()
        self.show_register_title_text()
        self.input_phone(phone)
        self.input_code(code)
        self.input_password(password)
        self.choose_person()
        self.click_register_btn()

    def person_enterprise(self, phone, code, password):
        self.click_user_register()
        self.show_register_title_text()
        self.input_phone(phone)
        self.input_code(code)
        self.input_password(password)
        self.choose_enterprise()
        self.click_register_btn()

    # -------------------------------选择完善资料-----------------------------------------

    success_message_loc = (By.ID, 'com.tdh.rpms:id/tv_state')
    complete_register_loc = (By.ID, 'com.tdh.rpms:id/btn_completion_information')
    into_home_page_loc = (By.ID, 'com.tdh.rpms:id/btn_enter_shouye')

    def show_success_message_text(self):
        try:
            message_text = self.get_text(*self.success_message_loc)
            self.log.info("change register message is： %s" % message_text)
            return True
        except:
            self.log.error("Skip to register complete page failed")
            return False

    def click_complete_register(self):
        self.click(*self.complete_register_loc)

    def click_into_home(self):
        self.click(*self.into_home_page_loc)

    def complete_register(self):
        self.show_success_message_text()
        self.click_complete_register()

    def into_home(self):
        self.show_success_message_text()
        self.click_into_home()

    # -------------------------------个人信息[完善]-----------------------------------------

    complete_title_loc = (By.ID, 'com.tdh.rpms:id/tv_title')
    choose_garden_loc = (By.ID, 'com.tdh.rpms:id/et_garden')
