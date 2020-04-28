""" MSH_MAT_GROUP mesh_material_group
    cstr material_name;
    short nfaces;
    short facenum[nfaces];
"""

from struct import unpack
from groups.abstract import AbstractGroup


class MSHMATGROUP(AbstractGroup):
    """ Stores mesh material information """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        zero_index = data.find(b"\0")
        self.name = data[:zero_index]
        index = zero_index + 1
        data = data[index:]
        count = unpack("H", data[:2])[0]
        data = data[2:]
        self.faces = []
        for _ in range(count):
            face_index = unpack("H", data[:2])[0]
            data = data[2:]
            self.faces.append(face_index)
        self.size = zero_index + 1 + 2 + count * 2

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"faces": self.faces}
        return {**super().pov_convert(), **spec_details}
