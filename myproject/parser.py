""" Parser reads in a 3ds model and chunks the data """
from struct import unpack
from myproject.chunk import Chunk


class Parser:
    """ Main parser file """

    def __init__(self, file_path):
        self._file_path = file_path
        self.data = None
        self.chunks = None

    def parse(self):
        """ parses data """
        data = None
        with open(self._file_path, "rb") as binary:
            data = binary.read()
        self.data = data
        chunk_id = unpack("H", data[:2])[0]
        # length = unpack("i", data[2:6])[0]
        data = data[6:]
        self.chunks = Chunk(None, chunk_id, data)

    def print_chunks(self):
        """ Prints all chunks """
        if self.chunks:
            self._print_chunk(self.chunks)

    def _print_chunk(self, chunk, indent=0):
        """ Prints a chunks information """
        print("%s%04X: %s" % ("  " * indent, chunk.chunk_id, chunk.name))
        for child in chunk.children:
            self._print_chunk(child, indent + 1)
