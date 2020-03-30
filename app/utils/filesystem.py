from pathlib import Path


def create_dir(path: Path):
    if path.exists():
        return
    return path.mkdir()


def create_dir_chain(*paths: Path):
    for path in paths:
        create_dir(path)
