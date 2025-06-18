#!/usr/bin/python3
"""Implement a division calculator that robustly handles errors like
division by zero and non-numeric inputs using using command
line arguments.
"""

def safe_divide(numerator, denominator):
    """Performs division and handle potential errors."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        try:
            result = numerator / denominator
            return f"The result of the division is {result:.1f}"
        except ZeroDivisionError:
            print("Error: Please enter numeric values only.")
