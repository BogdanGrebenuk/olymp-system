import pathlib


def save_python(path: pathlib.Path, code: str):
    code_dir = path / 'code'
    code_dir.mkdir()
    file_path = str((code_dir / 'main.py').resolve())
    with open(file_path, 'w') as file:
        file.write(code)
