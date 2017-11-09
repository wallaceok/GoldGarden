#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import os
'''
Created on 2017-10-19
@author: luting
Project:基础类MonkeyTest，测试手机内存、耗电量、耗流量
定义command_param、grow_for、cpu、memory、power、flow等函数方法。
'''


class MonkeyTest(object):

    def __init__(self):
        self.memory_value = None
        self.voltage = None
        self.pid = None
        self.uid = None

    @staticmethod
    def command_param(command_value):
        """
        adb 命令行参数
        :param command_value:   命令行参数
        :return:                返回执行adb命令（string类型）
        """
        command_text = 'adb %s' % command_value
        # print(command_text)
        use_command = os.popen(command_text).readlines()
        return use_command

    def grow_for(self):
        """
        启动时耗
        :return:                ThisTime,TotalTime,WaitTime（tuple类型）
        """
        start_apk = "shell am start -W -n com.tdh.rpms/com.tdh.rpms.ui.activity.SplashActivity_"
        adb_message = []
        for line in self.command_param(start_apk):
            if line != '\n':
                adb_message.append(str(line).strip('\n'))
        time_values = '{0},{1},{2}'.format(str(adb_message[-4]).replace('ThisTime:', ''),
                                           str(adb_message[-3]).replace('TotalTime:', ''),
                                           str(adb_message[-2]).replace('WaitTime:', ''))
        stop_apk = "adb shell am force-stop com.tdh.rpms"
        os.system(stop_apk)
        return time_values

    def cpu(self):
        """
        cpu占有
        :return:                cpu占有率，cpu值tuple类型
        """
        result_apk = self.command_param('shell dumpsys cpuinfo | findstr com.tdh.rpms')
        cpu_value = str(result_apk[0]).split('/')[0].split('%')[1]
        cpu_per = str(result_apk[0]).split('%')[0]
        return str(cpu_per)+'%', cpu_value

    def memory(self):
        """
        获取内存
        :return:                内存值string类型
        """
        result = self.command_param('shell  dumpsys  meminfo com.tdh.rpms')
        for line in result:
            if "TOTAL" in line:
                # global MEMORY_VALUE
                self.memory_value = line.split()[1]
                break
        return '{0}{1}'.format('内存：', self.memory_value)

    def power(self):
        """
        获取耗电量
        :return:                耗电量 string类型
        """
        os.system('adb shell dumpsys battery set status 1 ')
        result = self.command_param('shell dumpsys battery')
        for line in result:
            if line != '\n':
                str(line).strip('\n')
                if ' voltage' in line:
                    # global VOLRAGE
                    self.voltage = line.split()
        else:
            os.system('adb shell dumpsys battery set status 2 ')
            phone_status = str(self.command_param('shell dumpsys battery')[10]).strip('\n')
            print('设备重新充电成功\t%s' % phone_status)
        return '{0}{1}'.format('耗电量：', self.voltage[1])

    def flow(self):
        """
        获取流量
        :return:                上下行流量值tuple类型
        """
        result = self.command_param('shell ps grep com.tdh.rpms')
        # print(result)
        for value in result:
            if value != '\n':
                str(value).strip('\n')
                print(str(value).strip('\n'))
                if 'com.tdh.rpms' in value:
                    # global PID
                    self.pid = value.split()[1]
                    print(self.pid)
        uid_values = self.command_param('shell cat /proc/%s/status' % self.pid)
        for line in uid_values:
            if line != '\n':
                str(line).strip('\n')
                # print(str(line).strip('\n'))
                if 'Uid' in line:
                    # global UID
                    self.uid = line.split()[1]
                    print(self.uid)
        flow_values = self.command_param('shell cat /proc/net/xt_qtaguid/stats | findstr %s' % self.uid)
        flow_list = []
        for flow in flow_values:
            if flow != '\n':
                flow_list.append(str(flow).strip('\n'))
        print(flow_list)
        rx_bytes = str(flow_list[0]).split()
        tx_bytes = str(flow_list[1]).split()
        return '{0},{1}'.format(rx_bytes[5], rx_bytes[7]), '{0},{1}'.format(tx_bytes[5], tx_bytes[7])

if __name__ == '__main__':
    adb = MonkeyTest()
    # print(adb.grow_for())
    # print(adb.cpu())
    print(adb.memory())
    # print(adb.power())
    # print(adb.flow())
