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
from myproject.json_converter import JSONConverter
from myproject.pov_converter import PovConverter
from myproject.pov_runner import PovRunner


# pylint: disable=W0703
def main():
    """ main """
    root_dir = Path(__file__).resolve().parent
    pathlist = root_dir / "test_models"
    pathlist = pathlist.glob("**/*.3ds")
    # pathlist = [root_dir / "test_models" / "shuttle.3ds"]
    for path in pathlist:
        # because path is object not string
        print(f"Getting 3d model for {path}")
        try:
            parser = Parser(path)
            parser.parse()
            parser.print_chunks()
            json_converter = JSONConverter(parser.chunks)
            json_converter.convert_json()
            json_folder = root_dir / "jsons"
            json_folder.mkdir(parents=True, exist_ok=True)
            json_file = f"{path.stem}.json"
            json_converter.save_json(json_folder, json_file)
            pov_converter = PovConverter(json_folder / json_file)
            pov_converter.convert_pov()
            pov_folder = root_dir / "povs"
            pov_folder.mkdir(parents=True, exist_ok=True)
            pov_file = f"{path.stem}.pov"
            pov_converter.save_pov(pov_folder, pov_file)
            input_path = pov_folder / pov_file
            png_folder = root_dir / "pngs"
            png_folder.mkdir(parents=True, exist_ok=True)
            png_file = f"{path.stem}.png"
            output_path = png_folder / png_file
            pov_runner = PovRunner("povray", input_path, output_path)
            pov_runner.run_pov()
        except Exception:
            print(f"Failed to load model: {format_exc()}")
        print("*" * 20)


if __name__ == "__main__":
    main()
