import pathlib
import py_compile
import sys


if len(sys.argv) != 3:
    raise ValueError('Wrong amount of arguments!')

_, input_file, output_file = sys.argv

input_file_path = pathlib.Path(input_file)

if not input_file_path.exists():
    raise ValueError('There is no user file!')

py_compile.compile(input_file, output_file, doraise=True)