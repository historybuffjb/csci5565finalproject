""" MESH_VERSION; """

from struct import unpack
from groups.abstract import AbstractGroup


class MESHVERSION(AbstractGroup):
    """ MESHVERSION does nothing """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = 1 * 4
        self.version = unpack("i", data)[0]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"version": self.version}
        return {**super().pov_convert(), **spec_details}
