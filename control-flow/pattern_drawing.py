#!/usr/bin/python3
"""Utilizes while loops and nested for loops to draw a simple
test-based pattern.
"""

# Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern: "))

# Draw the pattern:
count = 0
while (count < size):
    for i in range(size):
        print('*', end='')
    print('')
    count += 1
