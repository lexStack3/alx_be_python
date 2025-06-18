#!/usr/bin/python3
"""Defines a <BankAccount> class."""


class BankAccount:
    """A BankAccount blueprint for banking operations."""
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance

    def deposit(self, amount):
        """Adds a specified <amount> to current balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Deducts the specified <amount> from current balance."""
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Prints the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
