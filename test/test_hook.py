#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy

import pytest


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    ''' 收集测试结果 '''
    print("打印详细信息:\n")
    for item in terminalreporter.stats['passed']:
        print(item)
    print('total:{0}'.format(terminalreporter._numcollected))
    print('passed:{0}'.format(terminalreporter.stats.get('passed', [])))
    print('failed:{0}'.format(terminalreporter.stats.get('failed', [])))
    print('error:{0}'.format(terminalreporter.stats.get('error', [])))
    print('skipped:{0}'.format(terminalreporter.stats.get('skipped', [])))


