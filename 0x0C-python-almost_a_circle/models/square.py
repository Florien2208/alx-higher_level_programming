#!/usr/bin/python3
"""
module for the square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This is the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a class instance

        Args:
            size (int): size
            x (int): x position
            y (int): y position
        """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """Customize print for class instance

        Returns: formated string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Accessor for the size property

        Returns: the value of the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Accessor for the size property

        Args:
            value (int): value of the property

        Raises:
            TypeError: if value is not an integer
            ValueError: if the value <= 0
        """
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """
        Updates the value of the attributes of class instance

        Args:
            args (list): array of values
            kwargs (dict): dictionary of key value pairs
        """
        attr = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attr[i], value)
        if len(args) > 0:
            return
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Returns the dictionary representation of the class instance
        """
        prefix1 = f"_{self.__class__.__name__}__"
        prefix2 = f"_{self.__class__.__bases__[0].__name__}__"\
                  if self.__class__.__bases__ else ""
        return {key.replace(prefix1, "")
                if key.startswith(prefix1) else key.replace(prefix2, "")
                if key.startswith(prefix2) else key: value
                for key, value in self.__dict__.items()}

