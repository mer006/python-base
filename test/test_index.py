#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy
import pytest


@pytest.mark.middle
def test_index_1():
    print('this is a test log')
    assert 1 + 1 == 23


@pytest.mark.login
@pytest.mark.high
def test_login_001():
    assert 1==3


@pytest.mark.skip(reason="功能取消")
@pytest.mark.middle
def test_login_002():
    pass


@pytest.mark.lower
def test_logout_001():
    pass
