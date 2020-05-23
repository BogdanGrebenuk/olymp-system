import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent
CODE_DIR = pathlib.Path(ROOT_DIR) / 'code'
PUBLIC_DIR = pathlib.Path(ROOT_DIR) / 'public'

# TODO: this stuff to core
DEFAULT_NUMBER_OF_PARTICIPANTS = 3
MAX_NUMBER_OF_PARTICIPANTS = 10

if __name__ == '__main__':
    print(ROOT_DIR)
    print(PUBLIC_DIR)
