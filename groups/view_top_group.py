""" VIEW_TOP
    float target_x, target_y, target_z;
    float view_width;
"""

from struct import unpack
from groups.abstract import AbstractGroup


class VIEWTOP(AbstractGroup):
    """ VIEWTOP stores top view information """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 4 * 4
        self.target_x, self.target_y, self.target_z, self.view_width = unpack(
            "f" * 4, data
        )

    def pov_convert(self):
        """ Returns important information """
        spec_details = {
            "view_width": self.view_width,
            "target_x": self.target_x,
            "target_y": self.target_y,
            "target_z": self.target_z,
        }
        return {**super().pov_convert(), **spec_details}
