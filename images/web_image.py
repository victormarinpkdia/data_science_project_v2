from io import BytesIO

import requests
from PIL.Image import Image as PillowImage, open

from .pillowable_image import IPIllowableImage


class WebImage(IPIllowableImage):
    def __init__(self, image_url):
        self.url: str = image_url

    def _create_pillow_image(self) -> PillowImage:
        response = requests.get(self.url)
        image_data = response.content
        return open(BytesIO(image_data))
