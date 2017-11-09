#!usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.by import By
from common.log import Log
from po import base_page


class Safe(base_page.BasePage):

    log = Log()

    safety_tab_loc = (By.NAME, '安全巡检')
    safety_plan_loc = (By.NAME, 'planTest')
    safety_point1_loc = (By.NAME, 'point1')
    safety_point2_loc = (By.NAME, 'point2')
    safety_go_button_loc = (By.ID, 'com.tdh.rpms:id/tv_sava')
    normal_status_loc = (By.ID, 'com.tdh.rpms:id/rb_normal')
    abnormal_status_loc = (By.ID, 'com.tdh.rpms:id/rb_abnormal')
    remark_text_loc = (By.ID, 'com.tdh.rpms:id/et_des')
    take_picture_loc = (By.ID, 'com.tdh.rpms:id/ll_paizhao')
    sure_picture_loc = (By.ID, 'com.android.camera:id/done_button')
    save_button_loc = (By.ID, 'com.tdh.rpms:id/btn_sava')
    finish_button_loc = (By.ID, 'com.tdh.rpms:id/btn_finish')
    safety_record_loc = (By.ID, 'com.tdh.rpms:id/tv_right_title')
    safety_result_loc = (By.ID, 'com.tdh.rpms:id/btn_state')

    def click_safety_tab(self):
        """
        进入安全巡检界面
        :return:
        """
        self.click(*self.safety_tab_loc)

    def click_plan(self):
        """
        点击巡检计划
        :return:
        """
        self.click(*self.safety_plan_loc)

    def click_point1(self):
        """
        选择第一个巡检点去巡检
        :return:
        """
        self.click(*self.safety_point1_loc)
        self.click(*self.safety_go_button_loc)

    def click_point2(self):
        """
        选择第二个巡检点去巡检
        :return:
        """
        self.click(*self.safety_point2_loc)
        self.click(*self.safety_go_button_loc)

    def click_normal_button(self):
        """
        巡检结果正常
        :return:
        """
        self.click(*self.normal_status_loc)

    def click_abnormal_button(self):
        """
        巡检结果异常
        :return:
        """
        self.click(*self.abnormal_status_loc)

    def input_remark(self, remark):
        """
        添加异常说明
        :param remark:    异常说明
        :return:
        """
        self.send_keys(remark, *self.remark_text_loc)

    def click_take_picture(self):
        """
        拍照
        :return:
        """
        self.click(*self.take_picture_loc)

    def click_sure_button(self):
        """
        拍照→确定按钮
        :return:
        """
        self.click(*self.sure_picture_loc)

    def click_save_button(self):
        """
        保存巡检点记录
        :return:
        """
        self.click(*self.save_button_loc)

    def click_finish_button(self):
        """
        结束巡检
        :return:
        """
        self.click(*self.finish_button_loc)

    def click_safety_record(self):
        self.click(*self.safety_record_loc)

    def inspection_normal_result(self):
        try:
            self.find_element(*self.safety_plan_loc)
            result_text = self.get_text(*self.safety_result_loc)
            self.log.info("plan result is： %s" % result_text)
            return True
        except:
            self.log.error("Test not passed")
            return False

    def inspection_normal(self):
        """
        安全巡检→巡检点[正常]
        :return:
        """
        print('############################### 第一个巡检点 ###############################')
        self.click_safety_tab()
        self.click_plan()
        self.click_point1()
        self.input_remark('No problem point1')
        self.key_code(4)
        self.click_take_picture()
        self.sleep(3)
        self.key_code(27)
        self.click_sure_button()
        self.wait(5)
        self.click_save_button()
        print('############################### 第二个巡检点 ###############################')
        self.click_point2()
        self.input_remark('No problem point2')
        self.key_code(4)
        self.click_take_picture()
        self.sleep(3)
        self.key_code(27)
        self.click_sure_button()
        self.wait(5)
        self.click_save_button()
        self.click_finish_button()
        self.key_code(4)
        self.click_safety_record()
