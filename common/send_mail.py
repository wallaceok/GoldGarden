#!/usr/bin/python3
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
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

    def send_mail(self):
        message = MIMEMultipart()
        message["From"] = self.sender_name
        message["To"] = self.receiver
        message['Subject'] = Header('Jyb_auto 测试邮件', 'utf-8')
        message.attach(MIMEText(self.html_value(), _subtype='html', _charset='utf-8'))
        try:
            server = smtplib.SMTP_SSL('smtp.163.com', 994)
            server.login(self.sender_name, self.sender_psw)
            server.sendmail(self.sender_name, self.receiver, message.as_string())
            server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('Error：无法发送邮件')

if __name__ == '__main__':
    send = SendMail()
    # print(send.get_report())
    # print(send.html_value())
    send.send_mail()
