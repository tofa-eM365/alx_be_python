import math


class Shape:
    """Base class for shapes."""

    def area(self):
        """Calculate the area of the shape. Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class for rectangle shapes."""

    def __init__(self, length, width):
        """Initialize a Rectangle instance."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class for circle shapes."""

    def __init__(self, radius):
        """Initialize a Circle instance."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
