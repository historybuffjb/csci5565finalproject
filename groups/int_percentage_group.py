""" INT_PERCENTAGE
    int percentage
"""

from struct import unpack
from groups.abstract import AbstractGroup


class INTPERCENTAGE(AbstractGroup):
    """ INTPERCENTAGE calculates percentage """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.percentage = unpack("i", data)

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"percentage": self.percentage}
        return {**super().pov_convert(), **spec_details}
