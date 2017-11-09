#!/usr/bin/python3
# coding:utf-8
import unittest
from config import global_parameters


def add_test(rule="test*.py"):
    case_path = global_parameters.case_path
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    run = unittest.TextTestRunner()
    run.run(discover)

if __name__ == '__main__':
    import fmovice
    print(fmovice.Search_Movice('QTP视频'))
    # add_test()







