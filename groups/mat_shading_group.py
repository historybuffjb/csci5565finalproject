""" MAT_SHADING
    short shading_value
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MATSHADING(AbstractGroup):
    """ MATSHADING gets the shading_value """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.shading_value = unpack("i", data)

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"shading_value": self.shading_value}
        return {**super().pov_convert(), **spec_details}
