#!/usr/bin/python3
"""no module to import"""

class Square:
    """ this class represents a square
    Attributes:
    __size (int): size of the square
    """
    
    def __init__ (self, size=0):
        """ initializes a new instance of the Square class. """
        self.size = size
    
    @property
    def size(self):
        """ 
        Getter method to retrieve the size of the square.
        
        returns: 
            int: the size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the squeare
        
        Parameters:
            value (init): the size to set
        Reises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2