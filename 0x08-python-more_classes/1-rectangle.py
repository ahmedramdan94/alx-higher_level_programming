#!/usr/bin/python3

'''
Rectangle class.
the module had class Rectangle
use cases :
new_rectangle = Rectangle()
'''
class Rectangle:
    '''define class and his own attribute and methods'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        width getter for private
        Return:
        self.width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        set width after git it
        Return:
        self.width = value
         '''
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        if value < 0:
            raise ValueError('no valid size value')
            self.__width = value

    @property
    def height(self):
        '''
        hight getter for private
        Return:
        self.h
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        set height after git it
        Return:
        self.height = value
    '''
        if not isinstance(value, int):
            raise TypeError(' height must be integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
