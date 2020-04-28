""" MESH_MATRIX
    float matrix[4][3];
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MESHMATRIX(AbstractGroup):
    """ stores mesh matrix information """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 12 * 4
        r11, r12, r13, r21, r22, r23, r31, r32, r33, x_coord, y_coord, z_coord = unpack(
            "f" * 12, data
        )
        self.rot = [r11, r12, r13, r21, r22, r23, r31, r32, r33]
        self.center = [x_coord, z_coord, -y_coord]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"rot": self.rot, "center": self.center}
        return {**super().pov_convert(), **spec_details}
