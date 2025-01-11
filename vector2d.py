"""
vector2d.py: A simple 2D vector class using magic methods.

This module demonstrates the use of magic methods to create a simple 2D vector class.

add::
    >>> v1 = Vector2D(2, 4)
    >>> v2 = Vector2D(2, 1)
    >>> v1 + v2
    Vector2D(4, 5)

abs::
    >>> v = Vector2D(3, 4)
    >>> abs(v)
    5.0

mul::
    >>> v * 3
    Vector2D(9, 12)
    >>> abs(v * 3)
    15.0
"""

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

