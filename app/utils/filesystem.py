def save_file_field_image(source, path):
    with open(path, "wb") as file:
        file.write(source.read())
