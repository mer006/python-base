#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy
import pytest
import json
import os
import time as t


# 使用pytest固件request取数据
# def readjson():
#     jsonpth = os.path.join(os.path.dirname((os.path.dirname(__file__))), 'data', 'sina.json')
#     return json.load(open(jsonpth))['sina']
#
#
# @pytest.fixture(params=readjson())
# def data(request):
#     return request.param
#
#
# @pytest.fixture()
# def init(selenium):
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     yield
#     selenium.close()
#
#
# def test_sina_email_null(selenium, init, data):
#     """selenium相当于WebDriver"""
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys(data['username'])
#     selenium.find_element_by_id('freepassword').send_keys(data['password'])
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == data['result']


@pytest.fixture(name='aad')
def init():
    print('start')
    yield
    print('end')


def test_hello_fixture(aad):
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_fixture_init.py'])
