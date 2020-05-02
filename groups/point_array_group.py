""" POINT_ARRAY short npoints; struct { float x, y, z; } points[npoints]; """
import sys
from struct import unpack
from groups.abstract import AbstractGroup


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
            if x_val > self._max_x:
                self._max_x = x_val
            if x_val < self._min_x:
                self._min_x = x_val
            if y_val > self._max_y:
                self._max_y = y_val
            if y_val < self._min_y:
                self._min_y = y_val
            if z_val > self._max_z:
                self._max_z = z_val
            if y_val < self._min_z:
                self._min_z = z_val
            index = 3 * 4
            data = data[index:]
            self.vertices.append([x_val, y_val, z_val])
        self.size = 2 + count * 3 * 4

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
