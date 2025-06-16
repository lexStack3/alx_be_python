#!/usr/bin/python3
"""Defines a function <perform_operation>."""

def perform_operation(num1, num2, operation):
    """Executes basic arithmetic operations."""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            num1 * num2
        case "divide":
            if num1 == 0:
                return
            elif num2 == 0:
                return
            else:
                return num1 / num2
