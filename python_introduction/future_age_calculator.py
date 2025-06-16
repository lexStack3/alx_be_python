#!/usr/bin/python3
"""Receiving user input in Python and perform a simple arithmetic
operation to calculate the user's age in a future year.
"""
age = int(input("How old are you? "))
current_year = 2023
ageIn2050 = (2050 - current_year) + age
print(f"In 2050, you will be {ageIn2050} years old.")
