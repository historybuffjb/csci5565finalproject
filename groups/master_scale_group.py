""" MASTER_SCALE
    float scale;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MASTERSCALE(AbstractGroup):
    """ MASTERSCALE does nothing """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.scale = unpack("f", data)[0]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"scale": self.scale}
        return {**super().pov_convert(), **spec_details}
