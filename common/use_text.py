#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
'''
Created on 2017-10-18
@author: luting
Project:基础类UseText，封装文件操作的公用方法，
定义read_text、write_text等函数方法。
'''

'''以下代码尚未测试，勿用！'''


class UseText(object):

    @staticmethod
    def read_text(file_name, file_path):
        """
        读取text文档文本
        :param file_name:    text文档文本名
        :param file_path:    text文档文本路径
        :return:             以list的类型返回text中的内容
        """
        value_lines = []
        try:
            file = open(file_name + '\\' + file_path, 'r')
            try:
                print('读取的文件为:%s' % file_name + '\\' + file_path)
                value_lines = file.readlines()
                for line in value_lines:
                    text_line = line.split('\n')
                    value_lines.append(text_line[0])
            finally:
                file.close()
        except IOError as err:
            print('IOError:{0}'.format(err))
        return value_lines

    @staticmethod
    def write_text(file_name, text_value):
        """
        写入Text文本文档
        :param file_name:   text文本文档名（路径）
        :param text_value:  写入内容（值）
        :return:
        """
        try:
            file = open(file_name, 'a')
            try:
                file.writelines(text_value)
            finally:
                file.close()
        except IOError as err:
            print('IOError:{0}'.format(err))
        else:
            print(u"在%s写入%s成功" % (file_name, text_value))

if __name__ == '__main__':
    ut = UseText
