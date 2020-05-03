""" JSONConverter converts 3ds chunks into a json dict """

from pathlib import Path
from json import dumps
from helpers.consts import CONVERTER_LIST


class JSONConverter:
    """ Converter converts 3ds chunks into a json dict """

    def __init__(self, chunks):
        self.chunks = chunks
        self.data = {}

    def convert_json(self):
        """ Converts chunks to pov format """
        self._iter_chunks(self.chunks)

    def _handle_chunk(self, chunk):
        """ Handles one given chunk """
        if chunk.name in CONVERTER_LIST:
            named_data = chunk.data.pov_convert()
            if chunk.name in self.data:
                self.data[chunk.name].append(named_data)
            else:
                self.data[chunk.name] = [named_data]

    def _iter_chunks(self, chunk):
        """ Prints a chunks information """
        self._handle_chunk(chunk)
        for child in chunk.children:
            self._iter_chunks(child)

    def save_json(self, out_path, out_file):
        """ Save to output path as a json file """
        out_path = Path(out_path)
        out_file = out_path / out_file
        with open(out_file, "w") as outfile:
            outfile.write(dumps(self.data, indent=4, sort_keys=True))
