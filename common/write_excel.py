#!/usr/bin/python3
# coding:utf-8
import xlsxwriter
import os
import time
from config import global_parameters


class WriteExcel(object):

    def __init__(self):
        self.title = ['应用名称', '启动时耗', '应用占内存', '应用占用CPU率', 'CPU总使用率', '耗电量', '耗流量']

    @staticmethod
    def excel_name():
        """
        excel命名
        :return:根据当前时间戳返回最新的时间戳文件名
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        monkey_result = global_parameters.monkey_result + '\\' + day
        if not os.path.isdir(monkey_result):
            os.makedirs(monkey_result)
        monkey_report = os.path.join(monkey_result, '{0}_{1}.xlsx'.format(time.strftime('%Y-%m-%d-%H_%M_%S'), 'monkeyReport'))
        return monkey_report

    def make_excel(self):
        work_book = xlsxwriter.Workbook(self.excel_name())
        work_sheet = work_book.add_worksheet('monkey_result')
        work_sheet.write_row('A1', self.title)

if __name__ == '__main__':
    write = WriteExcel()
    write.make_excel()
