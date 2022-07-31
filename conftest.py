#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy

import pytest
import json
import os
import time as t


# 使用pytest固件request取数据
def readjson():
    jsonpth = os.path.join(os.path.dirname(__file__), 'data', 'sina.json')
    return json.load(open(jsonpth))['sina']


@pytest.fixture(params=readjson())
def data(request):
    return request.param


@pytest.fixture()
def init(selenium):
    selenium.get("https://mail.sina.com.cn/#")
    selenium.maximize_window()
    yield
    selenium.close()


@pytest.fixture(scope='session', autouse=True)
def collected_time():
    startT = t.time()
    print("测试开始执行时间：{0}".format(startT))
    yield
    endT = t.time()
    print("测试结束时间为：{0}".format(endT))
    print("总执行时长为：{0}".format((endT-startT)))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    ''' 收集测试结果 '''
    print("打印详细信息:\n")
    for item in terminalreporter.stats['passed']:
        print(item)
    print('total:{0}'.format(terminalreporter._numcollected))
    # print('passed:{0}'.format(len(terminalreporter.stats.get('passed', []))))
    # print('failed:{0}'.format(len(terminalreporter.stats.get('failed', []))))
    # print('error:{0}'.format(len(terminalreporter.stats.get('error', []))))
    # print('skipped:{0}'.format(terminalreporter.stats.get('skipped', [])))
    # 忽略teardown错误的统计
    print('passed:{0}'.format(len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])))
    print('failed:{0}'.format(len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])))
    print('error:{0}'.format(len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])))
    print('skipped:{0}'.format(len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])))


# @pytest.fixture()
# def set_up():
#     print("this is set_up")
#     yield
#     print('this is set_up')
#     raise TypeError('set up error')
#
#
# @pytest.fixture()
# def teardown():
#     print("this is teardown")
#     yield
#     print("this is teardown")
#     raise TypeError('error')

