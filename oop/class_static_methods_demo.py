#!/usr/bin/python3
"""Defines a class <Calculator> that includes both a class method and a static method.
"""


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two operands."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the products of two operands."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
