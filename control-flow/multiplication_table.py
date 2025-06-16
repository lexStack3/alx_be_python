#!/usr/bin/python3
"""Uses a for loop to generate and print the multiplication table for a given number.
"""

# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table:
for i in range(1, 11):
    print("{} * {} = {}".format(number, i, number * i))
