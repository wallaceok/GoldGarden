#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import os
import time
import re
from config import global_parameters
'''
Created on 2017-10-18
Project:基础类ReadErrorLog，封装读取错误日志的公用方法，
定义get_new_log、log_re、read_log等函数方法。
'''


class ReadErrorLog(object):
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def __init__(self):
        self.log_path = global_parameters.log_path + "\\" + ReadErrorLog.day + '\\'

    def get_new_log(self):
        """
        获取最新的日志log
        :return:    最新的log文件名
        """
        list_dir = os.listdir(self.log_path)
        list_dir.sort()
        new_log_name = list_dir[-1]
        print('The newLog:{0}'.format(new_log_name))
        return new_log_name

    @staticmethod
    def log_re(err_log):
        """
        正则表达式匹配出错误的日志
        :param err_log:    错误的日志（形参）
        :return:             error类型的log
        """
        pattern = re.compile(r'\d\d.*?.*?ERROR.*')
        the_error_log = re.findall(pattern, err_log)
        return the_error_log

    def read_log(self):
        """
        读取当前最新的日志，并匹配出当前错误的log
        :return:          以string的类型返回error_log
        """
        the_log = []
        try:
            file = open(self.log_path+self.get_new_log(), 'r', encoding='utf-8')
            try:
                lines = file.readlines()
                for line in lines:
                    the_line = line.split('\n')
                    the_log.append(the_line[0])
            finally:
                file.close()
        except IOError as err:
            print('IOError:{0}'.format(err))
        new_log = '\n'.join(the_log)
        err_log = self.log_re(new_log)
        return ''.join(err_log)

if __name__ == '__main__':
    error_log = ReadErrorLog()
    print(error_log.read_log())
    # print(error_log.get_new_log())
#     print(error_log.log_re("""2017-10-31 14:48:07,636 - __main__ - DEBUG - 此处有一个靓仔
# 2017-10-31 14:48:07,640 - __main__ - ERROR - 宇宙无敌测试仔
# 2017-10-31 14:48:07,643 - __main__ - ERROR - 宇宙无敌测试仔"""))
