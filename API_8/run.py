# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import sys
import unittest

sys.path.append("./")


from API_8.common import HTMLTestRunnerNew
from API_8.common import contants



discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON15 API TEST REPORT",
                                              description="前程贷API",
                                              tester="tester")
    runner.run(discover)
