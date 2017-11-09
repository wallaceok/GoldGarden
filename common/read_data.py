#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import xlrd
from config import global_parameters
'''
Created on 2017-10-19
@author: luting
Project:基础类 Excel，数据驱动读取表格中的数据
定义open_excel，get_values等函数方法。
'''


class Excel(object):

    def __init__(self):
        self.excel_path = global_parameters.excel_path

    def open_excel(self):
        """
        打开表格
        :return:
        """
        try:
            data = xlrd.open_workbook(self.excel_path)
            print("Open table successfully")
            return data
        except FileNotFoundError as e:
            print('FileNotFoundError:{0}'.format(e))

    def get_values(self, sheet_name):
        """
        得到sheet中的行、列的值
        :param sheet_name:   sheet的名称
        :return:             返回list类型，list每一行的值都以dict的形式返回
        """
        try:
            table = self.open_excel().sheet_by_name(sheet_name)
            print("read sheet successfully")
            nrows = table.nrows
            ncols = table.ncols
            key = table.row_values(0)
            if nrows < 1 and ncols < 1:
                print('行数或列数小于1')
            else:
                value_list = []
                for row_num in range(1, nrows):
                    row = table.row_values(row_num)
                    value_dict = {}
                    for index in range(len(key)):
                        value_dict[key[index]] = row[index]
                    value_list.append(value_dict)
                return value_list
        except xlrd.biffh.XLRDError as e:
            print('xlrd.biffh.XLRDError:{0}'.format(e))

if __name__ == '__main__':
    excel = Excel()
    # excel.open_excel()
    # excel.get_values('Sheet122')
    print(excel.get_values('Sheet1'))
