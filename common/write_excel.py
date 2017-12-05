#!/usr/bin/python3
# coding:utf-8
import xlsxwriter
import os
import time
from config import global_parameters


class WriteExcel(object):

    def __init__(self):
        self.title = 'Jyb_Monkey'
        self.col_name = ['启动时耗', '应用占内存', '应用占用CPU率', 'CPU总使用率', '耗电量', '耗流量']
        self.go_time = ['', 'start_time', 'end_time']

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

    def make_excel(self, stat_time, end_time):
        """
        创建表格  生成monkey运行结果数值，以及monkey_result图表
        :param stat_time:起始值 请将参数值转换为list类型再入参
        :param end_time: 终止值 请将参数值转换为list类型再入参
        :return:
        """
        work_book = xlsxwriter.Workbook(self.excel_name())
        work_sheet = work_book.add_worksheet('monkey_result')
        # -------------------------------添加excel样式-----------------------------------------
        # sheet_title
        title_formatter = work_book.add_format()
        title_formatter.set_font_name('华文行楷')
        title_formatter.set_font_size(25)
        title_formatter.set_align('center')
        # sheet_value
        value_formatter = work_book.add_format()
        value_formatter.set_font_name('方正姚体')
        value_formatter.set_font_size(10)
        value_formatter.set_align('center')
        value_formatter.set_border(1)
        # row&column gap
        work_sheet.set_column('A:C', 20)
        work_sheet.merge_range('A1:C1', self.title, title_formatter)
        # -------------------------------table_value-----------------------------------------
        work_sheet.write_row('A2', self.go_time, value_formatter)
        work_sheet.write_column('A3', self.col_name, value_formatter)
        work_sheet.write_column('B3', stat_time, value_formatter)
        work_sheet.write_column('C3', end_time, value_formatter)
        # -------------------------------定义图表-----------------------------------------
        chart = work_book.add_chart({'type': 'column'})
        chart.add_series({'values': '=monkey_result!$B$3:$B$8',
                          'categories': '=monkey_result!$A$3:$A$8',
                          'name': '=monkey_result!$B$2'})
        chart.add_series({'values': '=monkey_result!$C$3:$C$8',
                          'name': '=monkey_result!$C$2'})
        chart.set_size({'width': 577, 'height': 287})
        chart.set_title({'name': 'Monkey_Result'})
        work_sheet.insert_chart('A13', chart)
        work_book.close()

if __name__ == '__main__':
    write = WriteExcel()
    write.make_excel([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
