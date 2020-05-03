# CSCI 5565 Final Project

Converts 3DS models into pov format

## Installation

Ensure you have python3.7 on your computer. Run:

```bash
python3.7 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m pre-commit install
```

## Usage

```bash
python main.py
python main.py inparallel modelspath /path/to/models jsonspath /path/to/jsons povspath /path/to/povs pngspath /path/to/pngs
```

## Instructions

If you have additional models to run just
drop them into the test_models directory.
Ensure that they have .3ds as the file
extension.


## License
[MIT](https://choosealicense.com/licenses/mit/)
