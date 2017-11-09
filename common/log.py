#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import logging
import time
import os
from config import global_parameters
'''
Created on 2017-10-19
@author: luting
Project:基础类Log，输出测试日志
'''

day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_path = global_parameters.log_path + "\\" + day
if not os.path.isdir(log_path):
    os.makedirs(log_path)


class Log:

    def __init__(self):
        self.log_name = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d-%H_%M_%S')))

    def console(self, level, message):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.console('debug', message)

    def info(self, message):
        self.console('info', message)

    def warning(self, message):
        self.console('warning', message)

    def error(self, message):
        self.console('error', message)


if __name__ == '__main__':
    log = Log()
    # log.debug('此处有一个靓仔')
    # log.error('宇宙无敌测试仔')
    log.error('一枚测试仔')
