#!/usr/bin/python3
""" no module imported"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
