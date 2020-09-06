import uuid
from typing import Union

from aiohttp.web import FileField

from app.common import PUBLIC_DIR


class ImagePathGenerator:

    def generate(self, image: Union[FileField]):
        image_path = PUBLIC_DIR / f"{uuid.uuid4()}{image.filename}"
        return image_path






