""" MAT_WIRESIZE
    float wire_size;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MATWIRESIZE(AbstractGroup):
    """ MATWIRESIZE does nothing """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.wire_size = unpack("f", data)[0]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"wire_size": self.wire_size}
        return {**super().pov_convert(), **spec_details}
