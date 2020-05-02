""" POINT_ARRAY short npoints; struct { float x, y, z; } points[npoints]; """
import sys
from struct import unpack
from groups.abstract import AbstractGroup
from helpers.vectors import Vec3


class POINTARRAY(AbstractGroup):
    """ Stores struct of points in object """

    # pylint: disable=R0914
    def __init__(self, parent, data):
        super().__init__(parent, data)
        count = unpack("H", data[:2])[0]
        data = data[2:]
        self.vertices = []
        self._min_x = sys.maxsize
        self._max_x = ~sys.maxsize
        self._min_y = sys.maxsize
        self._max_y = ~sys.maxsize
        self._min_z = sys.maxsize
        self._max_z = ~sys.maxsize
        for _ in range(count):
            x_val, y_val, z_val = unpack("fff", data[: 3 * 4])
            index = 3 * 4
            data = data[index:]
            self.vertices.append([x_val, z_val, -y_val])
        self.size = 2 + count * 3 * 4

        for counter_1, value_1 in enumerate(self.vertices):
            index = counter_1 + 1
            value_1_vec = Vec3(value_1[0], value_1[1], value_1[2])
            for counter_2, value_2 in list(enumerate(self.vertices))[counter_1:]:
                value_2_vec = Vec3(value_2[0], value_2[1], value_2[2])
                if (
                    value_1_vec.x_val == value_2_vec.x_val
                    and value_1_vec.y_val == value_2_vec.y_val
                    and value_1_vec.z_val == value_2_vec.z_val
                ):
                    self.vertices[counter_2] = value_1

        for vertice in self.vertices:
            if vertice[0] > self._max_x:
                self._max_x = vertice[0]
            if vertice[0] < self._min_x:
                self._min_x = vertice[0]
            if vertice[1] > self._max_y:
                self._max_y = vertice[1]
            if vertice[1] < self._min_y:
                self._min_y = vertice[1]
            if vertice[2] > self._max_z:
                self._max_z = vertice[2]
            if vertice[2] < self._min_z:
                self._min_z = vertice[2]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {
            "nvertices": len(self.vertices),
            "vertices": self.vertices,
            "minx": self._min_x,
            "maxx": self._max_x,
            "miny": self._min_y,
            "maxy": self._max_y,
            "minz": self._min_z,
            "maxz": self._max_z,
        }
        return {**super().pov_convert(), **spec_details}
