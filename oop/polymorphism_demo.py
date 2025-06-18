#!/usr/bin/python3
"""Enhancing my understanding of polymorphism in Python by
creating a set of classes that demonstrate method overriding and
polymorphic behavior.
"""
from math import pi


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    """A class <Rectangle> that inherites from class <Shape>
    and overrides its method <area>.
    """
    def __init__(self, length, width):
        """Instantiates a <Rectangle> object."""
        super()
        self.length = length
        self.width = width

    def area(self):
        """Returns the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A class <Cricle> that inherites from class <Shape>
    and override its method <area>.
    """
    def __init__(self, radius):
        """Instantiate a <Cricle> object."""
        super()
        self.radius = radius

    def area(self):
        """Returns the area of a circle."""
        return pi * (self.radius ** 2)
