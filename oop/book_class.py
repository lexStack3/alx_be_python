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
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Deletes the Book instance."""
        print(f"Deleting {self.title}")
        del self

    def __str__(self):
        """Returns a descriptive string of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that would recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', '{self.year}')"
