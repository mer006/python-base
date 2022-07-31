#! usr/bin/env python
# -*- coding:utf-8 -*-
# author: Mercy

'''
测试用例：最小粒度的测试单位
> 1、初始化
> 2、测试步骤
> 3、结果验证
> 4、清理
测试套件：测试用例的容器/集合
测试固件：初始化、清理
测试执行
测试断言：assert结果验证
测试报告:TestReport

unittest和pytest的区别
1、unittest是面向对象，pytest可以面向对象、函数
2、unittest参数话需要依赖第三方库，pytest不需要依赖
3、测试报告不同，unittest是用htmlreportrunner生成报告，pytest可以用插件生成pytest-html或allure报告，更好看
4、unittest没有插件，pytest插件丰富
5、unittest不支持失败重试，pytest分布式执行，支持失败重试
6、pytest可以兼容unittest

pytest特点：
文件名 规范 test_开头
用例要以test_开头，否则不会执行
类要以Test开头

执行时可以单独执行某些函数或类
python -m pytest -v test_unit.py::TestAdd
'''


def add(a, b):
    return a + b


def test_add_int():
    assert add(1, 1) == 2


# pytest中，测试用例必须是test_开头
def test_add_float():
    assert add(1.0, 1.0) == 2.0


# pytest中 测试类必须是Test开头
class TestAdd:
    def test_add_unit_2(self):
        assert add(2, 3) == 8




