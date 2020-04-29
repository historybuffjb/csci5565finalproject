""" MESH_COLOR
    short color_index;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MESHCOLOR(AbstractGroup):
    """ MESHCOLOR does nothing """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.color_index = unpack("i", data)

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"color_index": self.color_index}
        return {**super().pov_convert(), **spec_details}
