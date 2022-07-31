#! usr/bin/env python
# _*_ coding:utf-8 _*_
# author: Mercy
from selenium import webdriver
import time as t
import pytest
import json
import os

# driver = webdriver.Chrome()
# driver.get('https://mail.sina.com.cn/#')
# driver.maximize_window()
# driver.find_element_by_link_text('登录')
# # driver.find_element_by_xpath('//div[@class="freeMailbox"]/div[1]/span[1]/text()')


# def test_sina_email_null(selenium):
#     """selenium相当于WebDriver"""
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys('')
#     selenium.find_element_by_id('freepassword').send_keys('')
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == '请输入邮箱名'
#
#
# def test_sina_email_error(selenium):
#     """selenium相当于WebDriver"""
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys('22')
#     selenium.find_element_by_id('freepassword').send_keys('33')
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == '您输入的邮箱名格式不正确'


# # 参数时元组或列表
# def data():
#     return [
#         ('', '', r'请输入邮箱名'),
#         ('22', '33', r'您输入的邮箱名格式不正确')
#     ]
#
#
# @pytest.mark.parametrize('username,password,result', data())
# def test_sina_email_null(selenium, username, password, result):
#     """selenium相当于WebDriver"""
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys(username)
#     selenium.find_element_by_id('freepassword').send_keys(password)
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == result


# # 参数是字典形式
# def data():
#     return [
#         {"username": "", "password": "", "result": "请输入邮箱名"},
#         {"username": "22", "password": "33", "result": "您输入的邮箱名格式不正确"}
#     ]
#
#
# @pytest.mark.parametrize('data', data())
# def test_sina_email_null(selenium, data):
#     """selenium相当于WebDriver"""
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys(data['username'])
#     selenium.find_element_by_id('freepassword').send_keys(data['password'])
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == data['result']


# 从json文件中读取参数
# def readjson():
#     jsonpth = os.path.join(os.path.dirname((os.path.dirname(__file__))), 'data', 'sina.json')
#     return json.load(open(jsonpth))['sina']
# def readjson():
#     return json.load(open('test/sina.json'))['sina']

#
# # @pytest.mark.parametrize('data', readjson())
# def test_sina_email_null(selenium, data):
#     """selenium相当于WebDriver"""
#     selenium.get("https://mail.sina.com.cn/#")
#     selenium.maximize_window()
#     t.sleep(3)
#     selenium.find_element_by_id('freename').send_keys(data['username'])
#     selenium.find_element_by_id('freepassword').send_keys(data['password'])
#     t.sleep(3)
#     selenium.find_element_by_link_text('登录').click()
#     meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
#     assert meresult == data['result']


# 使用pytest固件request取数据
def readjson():
    jsonpth = os.path.join(os.path.dirname((os.path.dirname(__file__))), 'data', 'sina.json')
    return json.load(open(jsonpth))['sina']


@pytest.fixture(params=readjson())
def data(request):
    return request.param


def test_sina_email_null(selenium, data):
    print(type(data))
    print(data)
    """selenium相当于WebDriver"""
    selenium.get("https://mail.sina.com.cn/#")
    selenium.maximize_window()
    t.sleep(3)
    selenium.find_element_by_id('freename').send_keys(data['username'])
    selenium.find_element_by_id('freepassword').send_keys(data['password'])
    t.sleep(3)
    selenium.find_element_by_link_text('登录').click()
    meresult = selenium.find_element_by_xpath('//div[@class="freeError"][1]/span[1]').text
    assert meresult == data['result']


if __name__ == '__main__':
    pytest.main(['-v', '-s', '--driver', 'Chrome', 'test_params.py'])
