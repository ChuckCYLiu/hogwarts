# -*- coding: utf-8 -*-
# @Author   : arthur
# @File     : calc.py

class Calculator:
    """简单的计算器"""

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return e.__class__.__name__
