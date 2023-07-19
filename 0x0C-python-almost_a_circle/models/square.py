#!/usr/bin/python3
"""
Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        creat a Square attributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        return square dimension and infos
        """
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    @property
    def size(self):
        """
        getter to the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter the  size value of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates a square values from extern variables
        """
        d = {}
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary infos
        """
        d = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return d
