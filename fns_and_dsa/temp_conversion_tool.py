#!/usr/bin/python3
"""Illustrate the concept of variable scope by creating a script that
converts temperatures between Celsius and Fahrenheit, using global
variables to store conversion factors.
"""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius."""
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit."""
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return fahrenheit

def main():
    temperature = float(input("Enter the temperature to convert: "))
    type_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    match type_of_temperature:
        case 'C':
            print("{}°C is {}°F".format(temperature,
                                        convert_to_fahrenheit(temperature)))
        case 'F':
            print("{}°F is {}°C".format(temperature,
                                        convert_to_celsius(temperature)))


if __name__ == "__main__":
    main()
