#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy
import time as t
import pytest
#
# def test_baidu_title(selenium):
#     print(type(selenium))
#     selenium.get("http://www.baidu.com")
#     assert selenium.title == "百度一下，你就知道"
#
#
# def test_baidu_find(selenium):
#     selenium.get("https://www.baidu.com")
#     so = selenium.find_element_by_id('kw')
#     so.send_keys('aip test')
#     t.sleep(5)
#     assert so.get_attribute('value') == 'api test'


def test_sina_email_null(selenium, init, data):
    """selenium相当于WebDriver"""
    t.sleep(3)
    selenium.find_element_by_id('freename').send_keys(data['username'])
    selenium.find_element_by_id('freepassword').send_keys(data['password'])
    t.sleep(3)
    selenium.find_element_by_link_text('登录').click()
    meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
    assert meresult == data['result']


