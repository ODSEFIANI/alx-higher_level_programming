#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            creates and update a  rectangle

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                y (int): y of the rectangle
                x (int): x of the rectangle
                id (int): id of the rectangle
            """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        gets the value of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        sets the value of the rectangle
        """
        self.__height = value

    @property
    def width(self):
        """
        of the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets of the rectangle  width
        """
        self.__width = value

    @property
    def y(self):
        """
        gets of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets of the rectanglevalue
        """
        self.__y = value

    @property
    def x(self):
        """
        of the rectanglevalue
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        of the rectangle
        """
        self.__x = value

    def __str__(self):
        """Return the print and str of the rectangle representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x, self.y,
                                                    self.width, self.height)

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def display(self):
        """draw the Rectangle using sequence of `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for he in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
            
    def update(self, *args, **kwargs):
        
        """update the value of the Rectangle class.

        Args:
            *args (ints): Nees.
                - 1st argumattribute
            **kwargs (dict): New f attributes.
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
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dict keyy values
        """
        d = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return d
