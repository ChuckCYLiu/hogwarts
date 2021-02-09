# -*- coding: utf-8 -*-
# @Author   : arthur
# @File     : conftest.py
import pytest

from src.python_code.calc import Calculator


@pytest.fixture(scope='module')
def arrange():
    """测试前置后置工作"""
    print('开始计算')
    yield
    print('计算结束')


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc
