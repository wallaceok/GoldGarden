#!/usr/bin/python3
# coding:utf-8
import smtplib
from config import global_parameters
import os
import time


class SendMail(object):

    def __init__(self):
        self.receiver = global_parameters.receiver
        self.sender_name = global_parameters.sender_name
        self.sender_psw = global_parameters.sender_psw

    @staticmethod
    def get_report():
        day = time.strftime('%Y-%m-%d')
        try:
            dirs = os.listdir(global_parameters.report_ptah+'\\'+day)
            if dirs is not None:
                dirs.sort()
                new_report = dirs[-1]
                print('最新测试生成的报告：' + new_report)
                return new_report
            else:
                print('This directory is empty')
        except FileNotFoundError as error:
            print(' FileNotFoundError:{0}'.format(error))

    def html_value(self):
        try:
            day = time.strftime('%Y-%m-%d')
            html_file = os.path.join(global_parameters.report_ptah + '\\' + day, self.get_report())
            with open(html_file, 'rb') as file:
                html_value = file.read()
            return html_value
        except IOError as error:
            print('IOError:{0}'.format(error))

if __name__ == '__main__':
    send = SendMail()
    # print(send.get_report())
    print(send.html_value())
