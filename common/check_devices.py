#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import os
import re
from common.adb_monkey import MonkeyTest
'''
Created on 2017-10-19
@author: luting
Project:基础类CheckDevices，用于检查当前链接手机设备的情况
定义is_success_connect等函数方法。
'''


class CheckDevices(MonkeyTest):

    def is_success_connect(self):
        """
        检查设备是否链接
        :return:
        """
        devices_info = self.command_param('devices')
        devices_list = []
        for value in devices_info:
            if value != '\n':
                devices_list.append(value.strip('\n'))
        is_success_message = ''.join(str(devices_list[-1]).split('\t'))
        pattern = re.compile(r'.*?device')
        match_result = re.findall(pattern, is_success_message)
        if is_success_message != match_result[0]:
            print('尚未链接设备，请检查')
        else:
            device_name = str(os.popen('adb shell getprop ro.serialno').read()).strip('\r\n')
            print('链接设备成功：%s' % device_name)

if __name__ == '__main__':
    devices = CheckDevices()
    devices.is_success_connect()
