#!/usr/bin/python3
'''Definition of rectangle class'''

from model.base import Base


class Rectangle(Base):
    '''Class rectangle, inherits from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization of rectangle class
    Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Property: Gets the width of the Rectangle
        Returns: The width of the Rectangle
        '''
        return self.__width

    @property
    def height(self):
        '''Property: Gets the geometry of the Rectangle
        Returns: The height of the Rectangle
        '''
        return self.__height

    @property
    def x(self):
        '''Property: Gets the x coordinate of the Rectangle
        Returns: The x coordinate of the Rectangle
        '''
        return self.__x

    @property
    def y(self):
        '''Property: Gets the y coordinate of the Rectangle
        Returns: The y coordinate of the Rectangle
        '''
        return self.__y

    @width.setter
    def width(self, value):
        '''Property: Sets the width of the Rectangle
        Args:
            value (int): The width of the Rectangle'''
        if not isinstance(value, int):
            # either try an empty string or an alpha character
            raise TypeError('width must be integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        '''Property: Sets the height of the Rectangle
        Args:
            value (int): The height of the Rectangle'''
        if not isinstance(value, int):
            # either try an empty string or an alpha character
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height mist be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        '''Property: Sets the coordinate of the x of the
        Args:
            value (int): the x attribute'''
        if not isinstance(value, int):
            # either try an empty string or an alpha character
            raise TypeError('x must be integer')
        self.__x = value

    @y.setter
    def y(self, value):
        '''Property: Sets the coordinate of the y of the
        Args:
            value (int): the y attribute'''
        if not isinstance(value, int):
            # either try an empty string or an alpha character
            raise TypeError('y must be integer')
        self.__y = value

    def area(self):
        # area_cal = self.__width * self.__height
        area = self.__width * self.__height  # static method

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

