#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
from config.read_config import ReadConfig
import os
'''
Created on 2017-10-19
@author: luting
项目相关操作路径配置
'''

read_config = ReadConfig()

'''Mysql数据库参数配置'''
mysql_host = read_config.get_values('Mysql', 'host')
mysql_port = read_config.get_values('Mysql', 'port')
mysql_user = read_config.get_values('Mysql', 'user')
mysql_passwd = read_config.get_values('Mysql', 'passwd')
mysql_db = read_config.get_values('Mysql', 'db')

'''测试机参数配置[vivo6p]'''
vivo6p_appium_server_port = read_config.get_values('Vivo6', 'appium_server_port')
vivo6p_system = read_config.get_values('Vivo6', 'OS_system')
vivo6p_version = read_config.get_values('Vivo6', 'OS_version')
vivo6p_deviceName = read_config.get_values('Vivo6', 'deviceName')

'''apk_参数配置[Jyb]'''
apk_package = read_config.get_values('App', 'package')
apk_activity = read_config.get_values('App', 'activity')

'''文件路径配置'''
project_path = read_config.get_values('projectConfig', 'project_path')
log_path = os.path.join(project_path, 'result', 'log')
excel_path = os.path.join(project_path, 'data', 'loginData.xlsx')
image_path = os.path.join(project_path, 'result', 'image')
report_ptah = os.path.join(project_path, 'result', 'report')
case_path = os.path.join(project_path, 'test_case')
apk_path = os.path.join(project_path, 'apk')
data_path = os.path.join(project_path, 'data')

'''邮箱参数配置'''
receiver_luting = read_config.get_values('Email', 'recvaddress_luting')
receiver_xiaofang = read_config.get_values('Email', 'recvaddress_xiaofang')
receiver_lizhen = read_config.get_values('Email', 'recvaddress_lizhen')
receiver_linyan = read_config.get_values('Email', 'recvaddress_linyan')
sender_name = read_config.get_values('Email', 'sendaddr_name')
sender_psw = read_config.get_values('Email', 'sendaddr_pswd')

