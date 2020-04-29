""" MAT_NAME
    cstr material_name;
"""

from groups.abstract import AbstractGroup


class MATNAME(AbstractGroup):
    """ MATNAME stores material name """

    def __init__(self, parent, data):
        super().__init__(parent, data)
        zero_index = data.find(b"\0")
        self.material_name = data[:zero_index].decode("utf-8")
        new_index = zero_index + 1
        data = data[new_index:]
        self.size = zero_index + 1

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.material_name}"

    def pov_convert(self):
        """ Returns import information """
        spec_details = {"material_name": self.material_name}
        return {**super().pov_convert(), **spec_details}
