""" SMOOTH_GROUP
    short grouplist[n]; determined by length seems to be 4 per face
"""

from struct import unpack
from groups.abstract import AbstractGroup


class SMOOTHGROUP(AbstractGroup):
    """ Smoothgroup stores mysterious information """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        self.size = len(data)
        self.groups = []
        for _ in range(len(parent.parent.data.faces)):
            group_id = unpack("i", data[:4])[0]
            self.groups.append(group_id)
            data = data[4:]

    def pov_convert(self):
        """ Returns important information """
        spec_details = {"groups": self.groups}
        return {**super().pov_convert(), **spec_details}
