#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy
import pytest
import requests
import time as t
# import pytest


# @pytest.mark.skip(reason='测试忽略执行')
def test_taobao():
    r = requests.get(url="http://www.taobao.com")
    assert r.status_code == 200


def test_baidu():
    r = requests.get(url="http://www.baidu.com")
    t.sleep(3)
    assert r.status_code == 200


def test_001():
    assert 1 == 1
