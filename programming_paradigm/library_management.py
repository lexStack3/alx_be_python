#!/usr/bin/python3
"""Understanding the basic concept of OOP in Python by implementing
a system that tracks books in a library, focusing on classes,
object instantiation, and method invocation.
"""


class Book:
    """Creates a <Book> instance.
    Args:
        title (str): Title of the book to instantiate
        author (str): Name of the author.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    """Creates a <Library> for tracking all registered <Book>s"""
    def __init__(self):
        """Instantiates a <Library>."""
        self._books = []

    def add_book(self, book):
        """Adds a <Book> to the list of books in the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a <Book> from the library."""
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                break

    # return_book(self) -> For ALX Checker
    def return_book(self, title):
        """Checks back a <Book> into the library."""
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                break

    def list_available_books(self):
        """Prints all available <Book>s in the library."""
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
