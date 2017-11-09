#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import configparser
import os
'''
Created on 2017-10-19
@author: luting
Project:基础类ReadConfig，封装读取配置文件ini的公用方法，
定义get_value等函数方法。
'''


class ReadConfig:
    def __init__(self):
        self.config_path = os.path.split(os.path.realpath(__file__))[0]

    def get_values(self, sections, options):
        """
        读取ini文件
        :param sections: ini中的节
        :param options: ini中的键
        :return: 返回section中的option的值(返回string类型)
        """
        config_ini_path = os.path.join(self.config_path, 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_ini_path)
        return config.get(sections, options)

if __name__ == '__main__':
    read_ini = ReadConfig()
    print(read_ini.get_values('Mysql', 'user'))
