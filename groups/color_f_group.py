""" COLOR_F
    float red, grn, blu;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class COLORF(AbstractGroup):
    """ COLORF gives red grn blu values """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 3 * 4
        self.red, self.grn, self.blu = unpack("f" * 3, data)

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"red": self.red, "green": self.grn, "blue": self.blu}
        return {**super().pov_convert(), **spec_details}
