#!/usr/bin/python3
"""Importing and using the <datetime> module to perform specified
operations with dates and times.
"""
from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
