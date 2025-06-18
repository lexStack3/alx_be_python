#!/usr/bin/python3
"""Inheritance and Composition in Python: by creating a system
that models a library with different types of books.
"""


class Book:
    def __init__(self, title, author):
        """Instansiates a Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
