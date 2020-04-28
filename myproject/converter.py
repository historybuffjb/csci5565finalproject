""" Converter converts 3ds chunks into pov descriptions """


from helpers.consts import CONVERTER_DICT


class Converter:
    """ Converter converts 3ds chunks into pov objects """

    def __init__(self, chunks):
        self.chunks = chunks

    def convert(self):
        """ Converts chunks to pov format """
        self._iter_chunks(self.chunks)

    @staticmethod
    def _handle_chunk(chunk):
        """ Handles one given chunk """
        if chunk.name in CONVERTER_DICT:
            print(f"Name: {chunk.name} Return: {chunk.data.pov_convert()}")

    def _iter_chunks(self, chunk):
        """ Prints a chunks information """
        self._handle_chunk(chunk)
        for child in chunk.children:
            self._iter_chunks(child)
