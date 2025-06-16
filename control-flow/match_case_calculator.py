#!/usr/bin/python3
"""Using Match Case statements for handling multiple operations
in a simple calculator program.
"""

# Prompt for User Input:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operaiton (+, -, *, /): ")

# Perform the Calculation Using Match Case:
match operator:
    case "+":
        print("The result is {}.".format(num1 + num2))
    case "-":
        print("The result is {}.".format(num1 - num2))
    case "*":
        print("The result is {}.".format(num1 * num2))
    case "/":
        if (num1 == 0) or (num2 == 0):
            print("Cannot divide by zero.")
        else:
            print("The result is {}.".format(num1 / num2))
