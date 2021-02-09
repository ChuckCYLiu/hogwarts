# -*- coding: utf-8 -*-
# @Author   : arthur
# @File     : test_calc.py
import allure
import pytest
import yaml


with open('../data/calc.yaml') as f:
    param_data = yaml.safe_load(f)
    add = param_data['add']
    add_data = add['data']
    add_ids = add['ids']
    sub = param_data['sub']
    sub_data = sub['data']
    sub_ids = sub['ids']
    mul = param_data['mul']
    mul_data = mul['data']
    mul_ids = mul['ids']
    div = param_data['div']
    div_data = div['data']
    div_ids = div['ids']


@allure.feature('测试计算器')
class TestCalc:
    """计算器测试类"""

    @allure.story('测试加法')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', add_data, ids=add_ids)
    def test_add(self, get_calc, arrange, a, b, expect):
        with allure.step('计算两个数相加的和'):
            result = get_calc.add(a, b)
        print(result)
        # 四舍五入保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @allure.story('测试除法')
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expect', div_data, ids=div_ids)
    def test_div(self, get_calc, arrange, a, b, expect):
        result = get_calc.div(a, b)
        print(result)
        # 四舍五入保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @allure.story('测试减法')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', sub_data, ids=sub_ids)
    def test_sub(self, get_calc, arrange, a, b, expect):
        result = get_calc.sub(a, b)
        print(result)
        # 四舍五入保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @allure.story('测试乘法')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', mul_data, ids=mul_ids)
    def test_mul(self, get_calc, arrange, a, b, expect):
        result = get_calc.mul(a, b)
        print(result)
        # 四舍五入保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
