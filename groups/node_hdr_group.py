""" NODE_HDR
    cstr objname;
    short flag1;
    short flag2;
    short heirarchy; ?
"""

from struct import unpack
from groups.abstract import AbstractGroup


class NODEHDR(AbstractGroup):
    """ Stores heirarchy information """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        zero_index = data.find(b"\0")
        self.name = data[:zero_index]
        new_index = zero_index + 1
        data = data[new_index:]
        self.size = zero_index + 1 + 3 * 4
        self.hierarchy = unpack("H", data[4:6])[0]

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.hierarchy}"

    def pov_convert(self):
        """ Returns import information """
        spec_details = {"hierarchy": self.hierarchy}
        return {**super().pov_convert(), **spec_details}
