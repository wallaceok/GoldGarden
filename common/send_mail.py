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
        self.mail_to = [global_parameters.receiver_xiaofang, global_parameters.receiver_luting, global_parameters.receiver_lizhen, global_parameters.receiver_linyan]
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

    @staticmethod
    def get_log():
        day = time.strftime('%Y-%m-%d')
        try:
            dirs = os.listdir(global_parameters.log_path+'\\'+day)
            if dirs is not None:
                dirs.sort()
                new_log = dirs[-1]
                print('最新测试生成的日志：' + new_log)
                return new_log
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
        message["To"] = ','.join(self.mail_to)
        message['Subject'] = Header('Jyb_auto 测试邮件', 'utf-8')
        message.attach(MIMEText(self.html_value(), _subtype='html', _charset='utf-8'))
        # -------------------------------添加附件[测试报告]-----------------------------------------
        day = time.strftime('%Y-%m-%d')
        report_file = os.path.join(global_parameters.report_ptah + '\\' + day, self.get_report())
        att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        message.attach(att1)
        # -------------------------------添加附件[日志log]-----------------------------------------
        day = time.strftime('%Y-%m-%d')
        log_file = os.path.join(global_parameters.log_path + '\\' + day, self.get_log())
        att2 = MIMEText(open(log_file, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="report.log"'
        message.attach(att2)
        try:
            server = smtplib.SMTP_SSL('smtp.163.com', 994)
            server.login(self.sender_name, self.sender_psw)
            server.sendmail(self.sender_name, self.mail_to, message.as_string())
            server.quit()
            print('发送邮件成功-----------------请到邮箱查收!')
        except smtplib.SMTPException:
            print('Error：无法发送邮件')

if __name__ == '__main__':
    send = SendMail()
    # print(send.get_log())
    # print(send.get_report())
    # print(send.html_value())
    send.send_mail()
