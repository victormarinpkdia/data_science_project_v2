from PIL.Image import Image as PillowImage, open

from .pillowable_image import IPIllowableImage


class LocalImage(IPIllowableImage):
    def __init__(self, image_local_path: str):
        self.image_local_path: str = image_local_path
        self.name: str = image_local_path.split("/")[-1]
        self.extension: str = self.name.split(".")[-1]

    def _create_pillow_image(self) -> PillowImage:
        return open(self.image_local_path)
