# -*- coding: utf-8 -*-
# @Author   : arthur
# @File     : test_calc.py
import pytest

from python_code.Calculator import Calculator


class TestCalc:
    """计算器测试类"""

    def setup_class(self):
        print('开始测试')
        self.calc = Calculator()

    def teardown_class(self):
        print('测试结束')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a, b, expect',
                             [
                                 (1, 1, 2),
                                 (0.1, 0.2, 0.3),
                                 (-1, -1, -2)
                             ],
                             ids=['int', 'float', 'negative'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        print(result)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    def test_sub(self):
        pass

    def test_mul(self):
        pass

    @pytest.mark.parametrize('a, b, expect',
                             [
                                 (6, 2, 3),
                                 (1, 2, 0.5),
                                 (1, 3, 0.33),
                                 (2, -1, -2),
                                 (1, 0, ZeroDivisionError)
                             ],
                             ids=['int', 'float', 'float2', 'negative', 'divided_by_zero'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        print(result)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
