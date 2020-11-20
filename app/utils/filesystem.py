def save_file_field_image(source, path):
    with open(path, "wb") as file:
        file.write(source.read())


def save_file(destination: str, content):
    with open(destination, 'w') as file:
        file.write(content)


def load_file(destination: str):
    with open(destination) as file:
        return file.read()
