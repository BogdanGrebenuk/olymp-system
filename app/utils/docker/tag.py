def create_tag(image_title, image_tag=''):
    if image_tag == '':
        return image_title
    return f"{image_title}:{image_tag}"
