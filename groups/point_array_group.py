""" POINT_ARRAY short npoints; struct { float x, y, z; } points[npoints]; """

from struct import unpack
from groups.abstract import AbstractGroup
from helpers.vectors import Vec3


class POINTARRAY(AbstractGroup):
    """ Stores struct of points in object """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        count = unpack("H", data[:2])[0]
        data = data[2:]
        self.vertices = []
        for _ in range(count):
            x_val, y_val, z_val = unpack("fff", data[: 3 * 4])
            index = 3 * 4
            data = data[index:]
            self.vertices.append(Vec3(x_val, z_val, -y_val))
        self.size = 2 + count * 3 * 4

        for counter_1, value_1 in enumerate(self.vertices):
            index = counter_1 + 1
            for counter_2, value_2 in list(enumerate(self.vertices))[counter_1:]:
                if (
                    value_1.x_val == value_2.x_val
                    and value_1.y_val == value_2.y_val
                    and value_1.z_val == value_2.z_val
                ):
                    self.vertices[counter_2] = value_1

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"vertices": self.vertices, "nvertices": len(self.vertices)}
        return {**super().pov_convert(), **spec_details}
