#!/usr/bin/python3
"""Mastering Python magic methods by implementing a <Book> class
that incorporates constructors (__init__), destructors (__del__), and
the representation methods (__str__ and __repr__).
"""


class Book:
    """Class that uses special magic methods to enhance its
    functionality.
    """
    def __init__(self, title, author, year):
        """Initializes a <Book> instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.__title = title
        self.__author = author
        self.__year = year

    def __del__(self):
        """Deletes the Book instance."""
        print(f"Deleting {self.__title}")
        del self

    def __str__(self):
        """Returns a descriptive string of the book."""
        return f"{self.__title} by {self.__author}, published in {self.__year}"

    def __repr__(self):
        """Returns a string that would recreate the Book instance."""
        return f"Book('{self.__title}', '{self.__author}', '{self.__year}')"
