""" VIEW_CAMERA cstr name; """

from groups.abstract import AbstractGroup


class VIEWCAMERA(AbstractGroup):
    """ Stores the name of the view camera """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        zero_index = data.find(b"\0")
        self.name = data[:zero_index]
        self.size = zero_index + 1

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"
