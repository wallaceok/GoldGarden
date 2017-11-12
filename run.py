#!/usr/bin/python3
# coding:utf-8
import unittest
import time
from public import HTMLTestRunner
from config import global_parameters


def run(rule="test*.py"):
    case_path = global_parameters.case_path
    discover = unittest.defaultTestLoader.discover(
        case_path,
        pattern=rule,
        top_level_dir=None
    )
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_name = global_parameters.report_ptah+'\\'+now+'_TestReport'+'.html'
    with open(report_name, 'wb') as fb:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fb,
            title='Jyb_Test_Report',
            description='用例测试情况'
        )
        runner.run(discover)

if __name__ == '__main__':
    run()







