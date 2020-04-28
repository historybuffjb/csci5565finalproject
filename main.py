"""
    Description: This is the 3DS file parser, it produces a 3ds file object
        with the File3Ds.open method
    Status: Nearly complete, some bone data missing
    License: AGPLv3, see LICENSE for more details
    Copyright: 2011 Florian Boesch <pyalot@gmail.com>
    Helpful Links:
        http://en.wikipedia.org/wiki/.3ds
        http://www.spacesimulator.net/wiki/index.php?title=Tutorials:3ds_Loader
        http://www.martinreddy.net/gfx/3d/3DS.spec
        http://faydoc.tripod.com/formats/3ds.htm
"""
from pathlib import Path
from traceback import format_exc
from myproject.parser import Parser
from myproject.converter import Converter


# pylint: disable=W0703
def main():
    """ main """
    # pathlist = Path(__file__).resolve().parent / "test_models"
    # pathlist = pathlist.glob("**/*.3ds")
    pathlist = [Path(__file__).resolve().parent / "test_models" / "hubble" / "hst.3ds"]
    for path in pathlist:
        # because path is object not string
        print(f"Getting 3d model for {path}")
        try:
            parser = Parser(path)
            parser.parse()
            # parser.print_chunks()
            converter = Converter(parser.chunks)
            converter.convert()
        except Exception:
            print(f"Failed to load model: {format_exc()}")
        print("*" * 20)


if __name__ == "__main__":
    main()
