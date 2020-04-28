""" TEX_VERTS
    short nverts;
    struct {
        float x, y;
    } vertices[nverts];
"""

from struct import unpack
from groups.abstract import AbstractGroup


class TEXVERTS(AbstractGroup):
    """ Stores number of verteces """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        count = unpack("H", data[:2])[0]
        data = data[2:]
        self.vertices = []
        for _ in range(count):
            x_val, y_val = unpack("ff", data[:8])
            data = data[8:]
            self.vertices.append([x_val, 1.0 - y_val])
        self.size = 2 + count * 2 * 4

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"nvertices": len(self.vertices), "vertices": self.vertices}
        return {**super().pov_convert(), **spec_details}
