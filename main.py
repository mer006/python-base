#! usr/bin/env python
# _*_ coding:utf-8 _*_
# author: Mercy

import pytest

# pytest.main(['-v', './test_unit.py::TestAdd'])
# -v是输出详细信息，
# -s 执行print，不带-s会忽略print
# 测试用例分组 -k根据测试用例名称  -m 根据装饰器分组
# -k 执行特定名称的用例，如 -k "login or logout",则用例名中包含login或logout的都会被执行
# pytest.main(['-v', '-s', '-k', 'baidu', 'test/test_time.py'])
# pytest.main(['-v', '-s', 'test/test_time.py'])
pytest.main(['test/test_index.py'])
# pytest.main(['-v', '-s', '--driver', 'Chrome', 'test/test_selenium.py'])
