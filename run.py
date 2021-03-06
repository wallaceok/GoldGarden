#!/usr/bin/python3
# coding:utf-8
import unittest
import time
import os
from public import HTMLTestRunnerXL
from config import global_parameters


def run(rule="test_login.py"):
    case_path = global_parameters.case_path
    discover = unittest.defaultTestLoader.discover(
        case_path,
        pattern=rule,
        top_level_dir=None
    )
    day = time.strftime('%Y-%m-%d')
    report_path = global_parameters.report_ptah+'\\'+day
    if not os.path.isdir(report_path):
        os.makedirs(report_path)
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    test_report_name = report_path + '\\' + now + '_TestReport.html'
    with open(test_report_name, 'wb') as fb:
        runner = HTMLTestRunnerXL.HTMLTestRunner(
            stream=fb,
            title='Jyb_Test_Report',
            description='用例测试情况'
        )
        runner.run(discover)

if __name__ == '__main__':
    import fmovice
    print(fmovice.Search_Movice("mysql入门到精通"))
    # run()
