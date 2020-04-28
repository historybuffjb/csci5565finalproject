""" Chunk is used as a storage container for all 3ds hunks """
from struct import unpack
from myproject.children import Children

from helpers.consts import GROUP_DICT


class Chunk:
    """ Chunk stores all chunks """

    def __init__(self, parent, chunk_id, data):
        self.parent = parent
        self.chunk_id = chunk_id
        self.name = "unknown"
        self.data = None
        self.children = Children()
        if chunk_id in GROUP_DICT:
            self.data = GROUP_DICT[chunk_id](self, data)
            self.name = self.data.__class__.__name__
            self._parse_chunks(data[self.data.size :])

    def _parse_chunks(self, data):
        while data:
            chunk_id = unpack("H", data[:2])[0]
            length = unpack("i", data[2:6])[0]
            self.children.add(Chunk(self, chunk_id, data[6:length]))
            data = data[length:]
