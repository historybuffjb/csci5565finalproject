""" Abstract defines basic things stored in every group item """


class AbstractGroup:
    """ AbstractGroup holds details every group member should have """

    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.size = 0
        self.name = None

    def __repr__(self):
        return self.__class__.__name__

    def pov_convert(self):
        """ Converts data chunks into json understood by pov """
        return {
            "name": self.name.decode("utf-8") if self.name else None,
            "size": self.size,
            "parent": self.parent.data.__class__.__name__,
        }
