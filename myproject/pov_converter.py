""" Converts a specific json file into a pov file """

from json import load


class PovConverter:
    """ Converts json to pov """

    def __init__(self, json_path):
        self.json_path = json_path
        self.json = {}
        self._important_chunks = {
            "POINTARRAY": None,
            "TEXVERTS": None,
            "MESHMATRIX": None,
            "FACEARRAY": None,
            "MSHMATGROUP": None,
            "SMOOTHGROUP": None,
        }

    def convert_pov(self):
        """ Converts to pov """
        with open(self.json_path, "r") as json_file:
            json_data = load(json_file)
            for chunk in json_data:
                print(chunk)
