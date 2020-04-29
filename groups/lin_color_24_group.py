""" LIN_COLOR_24
    char red, grn, blu;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class LINCOLOR24(AbstractGroup):
    """ LINCOLOR24 gives red grn blu values """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 3 * 1
        self.red, self.grn, self.blu = unpack("c" * 3, data)
        self.red = str(self.red)
        self.grn = str(self.grn)
        self.blu = str(self.blu)

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"red": self.red, "green": self.grn, "blue": self.blu}
        return {**super().pov_convert(), **spec_details}
