""" N_CAMERA
    float camera_x, camera_y, target_z;
    float target_x, target_y, target_z;
    float bank_angle;
    float focus;
"""

from struct import unpack
from groups.abstract import AbstractGroup
from helpers.vectors import Vec3


class NCAMERA(AbstractGroup):
    """ NCAMERA stores information about an object's camera """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 8 * 4
        (
            camera_x,
            camera_y,
            camera_z,
            target_x,
            target_y,
            target_z,
            bank_angle,
            focus,
        ) = unpack("f" * 8, data)
        self.camera_pos = Vec3(camera_x, camera_y, camera_z)
        self.target_pos = Vec3(target_x, target_y, target_z)
        self.bank_angle = bank_angle
        self.focus = focus
