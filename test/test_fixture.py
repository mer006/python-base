#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy
import pytest


@pytest.fixture()
def login(username='wuya',password='123'):
    if username=='wuya' and password=='123':
        return 'asabbb'


@pytest.fixture()
def headers(login):
    return {'auth:{0}'.format(login)}


def test_profile(headers):
    print('headers:{0}'.format(headers))