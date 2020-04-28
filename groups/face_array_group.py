""" FACE_ARRAY may be followed by smooth_group;
    short nfaces
    struct {
        short vertex1, vertex2, vertex3;
        short flags;
    } facearray[nfaces];
"""

from struct import unpack
from groups.abstract import AbstractGroup


class FACEARRAY(AbstractGroup):
    """ FACEARRAY stores faces of object """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        count = unpack("H", data[:2])[0]
        data = data[2:]
        self.faces = []
        for counter in range(count):
            temp_end = counter + 1
            begin_index = counter * 4 * 2
            end_index = temp_end * 4 * 2
            x_coord, y_coord, z_coord, found_flags = unpack(
                "HHHH", data[begin_index:end_index]
            )
            self.faces.append((x_coord, y_coord, z_coord, found_flags))
        self.size = 2 + count * 4 * 2

    def pov_convert(self):
        """ Returns relevant information """
        spec_details = {"faces": self.faces}
        return {**super().pov_convert(), **spec_details}
