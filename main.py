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
import multiprocessing
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from traceback import format_exc
from prettytable import PrettyTable
from myproject.parser import Parser
from myproject.json_converter import JSONConverter
from myproject.pov_converter import PovConverter
from myproject.pov_runner import PovRunner


# pylint: disable=W0703
def run_converter(path, args):
    """ Runs program for given path """
    time_start = datetime.now()
    # because path is object not string
    try:
        parser = Parser(path)
        parser.parse()
        # parser.print_chunks()
        json_converter = JSONConverter(parser.chunks)
        json_converter.convert_json()
        Path(args.jsonspath).mkdir(parents=True, exist_ok=True)
        json_file = f"{path.stem}.json"
        json_converter.save_json(args.jsonspath, json_file)
        pov_converter = PovConverter(Path(args.jsonspath) / json_file)
        pov_converter.convert_pov()
        Path(args.povspath).mkdir(parents=True, exist_ok=True)
        pov_file = f"{path.stem}.pov"
        pov_converter.save_pov(args.povspath, pov_file)
        input_path = Path(args.povspath) / pov_file
        Path(args.pngspath).mkdir(parents=True, exist_ok=True)
        png_file = f"{path.stem}.png"
        output_path = Path(args.pngspath) / png_file
        pov_runner = PovRunner(args.povpath, input_path, output_path)
        pov_runner.run_pov()
    except Exception:
        print(f"Failed to load model: {format_exc()}")
    finally:
        end_time = datetime.now() - time_start
    return [str(path.stem), f"{end_time.seconds} seconds"]


def in_parallel(args):
    """ Runs in parallel """
    pretty_table = PrettyTable(["name", "run time"])
    pool = multiprocessing.Pool()
    result_async = [
        pool.apply_async(run_converter, args=(path, args))
        for path in Path(args.modelspath).glob("**/*.3ds")
    ]
    results = [r.get() for r in result_async]
    for row in results:
        pretty_table.add_row(row)
    print(pretty_table)


def in_sequence(args):
    """ Runs consecutively """
    pretty_table = PrettyTable(["name", "run time"])
    for path in Path(args.modelspath).glob("**/*.3ds"):
        pretty_table.add_row(run_converter(path, args))
    print(pretty_table)


def main(args):
    """ main """
    if args.inparallel:
        return in_parallel(args)
    return in_sequence(args)


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).resolve().parent
    ROOT_MODELS = ROOT_DIR / "test_models"
    ROOT_JSONS = ROOT_DIR / "jsons"
    ROOT_PNGS = ROOT_DIR / "pngs"
    ROOT_POVS = ROOT_DIR / "povs"
    PARSER = ArgumentParser(description="Process 3DS models into povray output")
    PARSER.add_argument(
        "inparallel",
        type=bool,
        nargs="?",
        default=False,
        help="Allows execution of all models to run in parallel",
    )
    PARSER.add_argument(
        "modelspath",
        type=str,
        nargs="?",
        default=f"{ROOT_MODELS}",
        help="The path to the directory containing all .3ds models",
    )
    PARSER.add_argument(
        "povpath",
        type=str,
        nargs="?",
        default="povray",
        help="Path to the pov executable",
    )
    PARSER.add_argument(
        "jsonspath",
        type=str,
        nargs="?",
        default=f"{ROOT_JSONS}",
        help="Path to the directory that will store the generated json files",
    )
    PARSER.add_argument(
        "povspath",
        type=str,
        nargs="?",
        default=f"{ROOT_POVS}",
        help="Path to the directory that will store the generated pov files ",
    )
    PARSER.add_argument(
        "pngspath",
        type=str,
        nargs="?",
        default=f"{ROOT_PNGS}",
        help="Path to the directory that will store the generated png files",
    )
    main(PARSER.parse_args())
